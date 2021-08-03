from sqlalchemy import Column, Integer, String
from app.DB.database import Base


class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    company_ko = Column(String(200), nullable=True)
    company_en = Column(String(200), nullable=True)
    company_ja = Column(String(200), nullable=True)
    tag_ko = Column(String(200), nullable=True)
    tag_en = Column(String(200), nullable=True)
    tag_ja = Column(String(200), nullable=True)

    def __init__(self, company_ko=None, company_en=None, company_ja=None, tag_ko=None, tag_en=None, tag_ja=None):
        self.company_ko = company_ko
        self.company_en = company_en
        self.company_ja = company_ja
        self.tag_ja = tag_ja
        self.tag_en = tag_en
        self.tag_ko = tag_ko

    def __repr__(self):
        return '<Id %r / Company_ko %r / Company_en %r / Company_ja %r / Tag_ko %r / Tag_en %r / Tag_ja %r/>' \
               % (self.id, self.company_ko, self.company_en, self.company_ja, self.tag_ko, self.tag_en, self.tag_ja)

    def __json__(self):
        return ['id', 'company_ko', 'company_en', 'company_ja', 'tag_ja', 'tag_en', 'tag_ko']
