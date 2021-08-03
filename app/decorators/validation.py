from enum import Enum
from functools import wraps
from typing import Type
from flask import request
from pydantic import BaseModel
from app.decorators.context import context_property


def args_preprocessor(func_name, request_args, payload):
    if func_name == "RecentMarketMapList.get":
        if payload["themeId"]:
            payload["themeId"] = request_args.getlist("themeId")
        return payload
    return payload


class PayloadLocation(Enum):
    ARGS = "args"
    JSON = "json"


def from_validator(concat_payload_key, payload):
    if concat_payload_key in "from":
        payload["FROM"] = payload.pop("from")
    return payload


def validate_with_pydantic(
        *,
        payload_location: PayloadLocation,
        model: Type[BaseModel],
        json_force_load: bool = False,
):
    query_string_list_funcs = {"RecentMarketMapList.get"}

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if payload_location == PayloadLocation.JSON:
                if json_force_load:
                    payload = request.get_json(force=True)
                else:
                    payload = request.json
            else:
                payload = request.args
                if hasattr(payload, "to_dict"):
                    payload = payload.to_dict()
                    if fn.__qualname__ in query_string_list_funcs:
                        payload = args_preprocessor(
                            func_name=fn.__qualname__,
                            request_args=request.args,
                            payload=payload,
                        )

            concat_payload_key = "".join(list(payload.keys()))
            try:
                payload = from_validator(
                    concat_payload_key=concat_payload_key,
                    payload=payload,
                )
                instance = dict(model(**payload))
            except:
                instance = None
            context_property.request_payload = instance
            return fn(*args, **kwargs)

        return wrapper

    return decorator
