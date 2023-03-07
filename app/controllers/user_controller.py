import app.models.db as db
from app.utils.log import Log
from app.models.user import User
from app.utils.error import Error

class UserController:
    
    
    def __init__(self):
        self.logging = Log.init_log_config()
    
    def create_table(self):
        try:
            if not db.engine.dialect.has_table(db.engine.connect(), User.__tablename__):
                db.Base.metadata.create_all(db.engine)
                self.logging.info("create_table(): table was created successfully "+User.__tablename__)
                db.session.close
            else:
                self.logging.info("create_table(): table "+User.__tablename__+" wasn't created, because it already exists")
        except Exception as e:
           self.logging.error("create_table(): {0} - Details: {1}".format(Error.E004.value, str(e)))
    
    
    def insert(self, obj:User):
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
            res = db.session.query(User).get(id)
            db.session.close
        except Exception as e:
            self.logging.error("get(): {0} - Details: {1}".format(Error.E006.value, str(e)))
        return res
    
    def get_by_identification(self, identificacion):
        res = None
        try:
            res = db.session.query(User).filter_by(identificacion = identificacion).all()
            db.session.close
        except Exception as e:
            self.logging.error("get(): {0} - Details: {1}".format(Error.E006.value, str(e)))
        return res
    
    def list(self):
        res = []
        try:
            res = db.session.query(User).all()
            db.session.close
        except Exception as e:
            self.logging.error("list(): {0} - Details: {1}".format(Error.E007.value, str(e)))
        return res   
            
    
    def update(self, id, obj: User):
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
    
    def delete(self, obj: User):
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