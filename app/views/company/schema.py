from enum import Enum
from typing import Optional, Dict, List
from pydantic import PositiveInt, BaseModel


class CompanySearchParameter(BaseModel):
    words: str


class TagSearchParameter(BaseModel):
    tags: str


class CompanyPostParameter(BaseModel):
    company: str
    tag: str
    type: str
