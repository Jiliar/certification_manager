import app.models.db as db
from app.utils.log import Log
from app.models.certificates_user_audit import CertificateUserAudit
from app.utils.error import Error

class CertificateUserAuditController:
    
    
    def __init__(self):
        self.logging = Log.init_log_config()
    
    def create_table(self):
        try:
            if not db.engine.dialect.has_table(db.engine.connect(), CertificateUserAudit.__tablename__):
                db.Base.metadata.create_all(db.engine)
                self.logging.info("create_table(): table was created successfully "+CertificateUserAudit.__tablename__)
                db.session.close
            else:
                self.logging.info("create_table(): table "+CertificateUserAudit.__tablename__+" wasn't created, because it already exists")
        except Exception as e:
           self.logging.error("create_table(): {0} - Details: {1}".format(Error.E004.value, str(e)))
    
    
    def insert(self, obj:CertificateUserAudit):
        try:
            db.session.add(obj)
        except Exception as e:
            self.logging.error("insert(): {0} - Details: {1}".format(Error.E005.value, str(e)))
            db.session.rollback()
            raise
        else:
            db.session.commit()
        db.session.close
    
    def get(self, id):
        res = None
        try:
            res = db.session.query(CertificateUserAudit).get(id)
            db.session.close
        except Exception as e:
            self.logging.error("get(): {0} - Details: {1}".format(Error.E006.value, str(e)))
        return res
    
    def list(self):
        res = []
        try:
            res = db.session.query(CertificateUserAudit).all()
            db.session.close
        except Exception as e:
            self.logging.error("list(): {0} - Details: {1}".format(Error.E007.value, str(e)))
        return res   
            
    
    def update(self, id, obj: CertificateUserAudit):
        res = None
        try:
             res = db.session.update(obj).filter_by(id=id)
        except Exception as e:
            self.logging.error("update(): {0} - Details: {1}".format(Error.E008.value, str(e)))
            db.session.rollback()
            raise
        else:
            db.session.commit()
        db.session.close
        return res
    
    def delete(self, obj: CertificateUserAudit):
        res = None
        try:
             res = db.session.delete(obj)
        except Exception as e:
            self.logging.error("delete(): {0} - Details: {1}".format(Error.E009.value, str(e)))
            db.session.rollback()
            raise
        else:
            db.session.commit()
        db.session.close
        return res