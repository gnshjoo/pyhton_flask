from http import HTTPStatus
from sqlalchemy import or_
from flask_restful import Resource
from app.DB.database import db_session as sql_session
from app.models.company import Company
from app.views.company.schema import CompanySearchParameter, TagSearchParameter, CompanyPostParameter
from app.decorators.validation import validate_with_pydantic, PayloadLocation
from app.decorators.context import context_property
from humps import decamelize
from app.json_encoder import AlchemyEncoder
import json


class SearchCompany(Resource):
    @validate_with_pydantic(
        payload_location=PayloadLocation.ARGS, model=CompanySearchParameter
    )
    def get(self):
        args = decamelize(context_property.request_payload)
        words = args['words']
        try:
            search_result = sql_session.query(Company).filter(
                or_(Company.company_ko.like('%' + words + '%'),
                    Company.company_ja.like('%' + words + '%'),
                    Company.company_ko.like('%' + words + '%'))).all()
            resp = json.dumps(search_result, cls=AlchemyEncoder, ensure_ascii=False)
            return {"msg": resp}, HTTPStatus.OK
        except Exception as e:
            return {"msg": e}, HTTPStatus.INTERNAL_SERVER_ERROR


class SearchTag(Resource):
    @validate_with_pydantic(
        payload_location=PayloadLocation.ARGS, model=TagSearchParameter
    )
    def get(self):
        args = decamelize(context_property.request_payload)
        tags = args['tags']
        try:
            tag_result = sql_session.query(Company).filter(
                or_(Company.tag_ko.like('%' + tags + '%'),
                    Company.tag_ja.like('%' + tags + '%'),
                    Company.tag_en.like('%' + tags + '%'))).all()

            resp = json.dumps(tag_result, cls=AlchemyEncoder, ensure_ascii=False)

            return {"msg": resp}, HTTPStatus.OK
        except Exception as e:
            return {"msg": e}, HTTPStatus.INTERNAL_SERVER_ERROR


class PostTag(Resource):

    @validate_with_pydantic(
        payload_location=PayloadLocation.JSON, model=CompanyPostParameter
    )
    def post(self):

        args = context_property.request_payload
        company = args['company']
        tags = args['tag']
        types = args['type']
        try:
            company_info = None
            if types == "ja":
                company_info = sql_session.query(Company).filter(Company.company_ja == company).one_or_none()
            elif types == "ko":
                company_info = sql_session.query(Company).filter(Company.company_ko == company).one_or_none()
            elif types == 'en':
                company_info = sql_session.query(Company).filter(Company.company_en == company).one_or_none()

            if company_info == None:
                return {"msg": "cannot search company"}, HTTPStatus.NOT_FOUND

            company_info.tag_ja = company_info.tag_ja + "|タグ_" + tags
            company_info.tag_ko = company_info.tag_ko + "|태그_" + tags
            company_info.tag_en = company_info.tag_en + "|tag_" + tags
            sql_session.commit()
            return {"msg": json.dumps(company_info, cls=AlchemyEncoder, ensure_ascii=False)}, HTTPStatus.OK
        except Exception as e:
            sql_session.rollback()
            return {"msg": e}, HTTPStatus.INTERNAL_SERVER_ERROR

    @validate_with_pydantic(
        payload_location=PayloadLocation.JSON, model=CompanyPostParameter
    )
    def delete(self):
        args = context_property.request_payload
        company = args['company']
        tags = args['tag']
        types = args['type']
        try:
            company_info = None
            if types == "ja":
                company_info = sql_session.query(Company).filter(Company.company_ja == company).one_or_none()
            elif types == "ko":
                company_info = sql_session.query(Company).filter(Company.company_ko == company).one_or_none()
            elif types == 'en':
                company_info = sql_session.query(Company).filter(Company.company_en == company).one_or_none()

            if company_info == None:
                return {"msg": "cannot search company"}, HTTPStatus.NOT_FOUND
            tag_ja = company_info.tag_ja.split("|")
            if "タグ_" + tags in tag_ja:
                tag_ja.remove("タグ_" + tags)
            tag_en = company_info.tag_en.split("|")
            if "tag_" + tags in tag_en:
                tag_en.remove("tag_" + tags)
            tag_ko = company_info.tag_ko.split("|")
            if "태그_" + tags in tag_ko:
                tag_ko.remove("태그_" + tags)

            company_info.tag_ja = '|'.join(tag_ja)
            company_info.tag_ko = '|'.join(tag_ko)
            company_info.tag_en = '|'.join(tag_en)
            sql_session.commit()
            return {"msg": json.dumps(company_info, cls=AlchemyEncoder, ensure_ascii=False)}, HTTPStatus.OK
        except Exception as e:
            sql_session.rollback()
            return {"msg": e}, HTTPStatus.INTERNAL_SERVER_ERROR
