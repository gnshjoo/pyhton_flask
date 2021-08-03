from flask import Blueprint, Flask
from flask_restful import Api
from app.views.company.api import SearchCompany, SearchTag, PostTag
from app.json_encoder import AlchemyEncoder


def route(flask_app: Flask):
    handle_exception_func = flask_app.handle_exception
    handle_user_exception_func = flask_app.handle_user_exception
    flask_app.json_encoder = AlchemyEncoder
    api_blueprint = Blueprint("api", __name__)
    api = Api(api_blueprint)
    flask_app.register_blueprint(api_blueprint)
    api.add_resource(SearchCompany, "/search/company")
    api.add_resource(SearchTag, "/search/tag")
    api.add_resource(PostTag, '/tag')

    flask_app.handle_exception = handle_exception_func
    flask_app.handle_user_exception = handle_user_exception_func
