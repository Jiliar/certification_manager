import app.models.db as db
import datetime
from sqlalchemy import Column, Integer, String, DateTime, MetaData

class CertificateUser(db.Base):
    
    __tablename__ = 'logic_certificates_user'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user  = Column(Integer, nullable=False)
    year  = Column(Integer, nullable=False)
    url_ftp  = Column(String(255), nullable=False)
    status  = Column(Integer, nullable=False)
    created_date  = Column(DateTime, default=datetime.datetime.utcnow)
    
    def __init__(self, id, id_user, year, url_ftp, status, created_date):
        self.id = id
        self.id_user = id_user
        self.year = year
        self.url_ftp = url_ftp
        self.status = status
        self.created_date = created_date

    def __repr__(self):
        return f" CertificateUser({self.id}, {self.id_user}, {self.year}, {self.url_ftp}, {self.status}, {self.created_date})"
