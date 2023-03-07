import app.models.db as db
import datetime
from sqlalchemy import Column, Integer, String, DateTime

class CertificateUserAudit(db.Base):
    
    __tablename__ = 'logic_certificates_user_audit'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    message  = Column(String(300), nullable=False)
    created_date  = Column(DateTime, default=datetime.datetime.utcnow)
    
    def __init__(self, id, message, created_date):
        self.id = id
        self.message = message
        self.created_date = created_date
        
    def __repr__(self):
        return f" CertificateUserAudit({self.id}, {self.message}, {self.created_date})"