import app.models.db as db
import datetime
from sqlalchemy import Column, Integer, String, DateTime

class User(db.Base):
    
    __tablename__ = 'auth_usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_id = Column(Integer, nullable=False)
    identificacion = Column(String(255), nullable=False)
    nombre1 = Column(String(255), nullable=False)
    nombre2 = Column(String(150), nullable=True)
    apellido1 = Column(String(150), nullable=False)
    apellido2 = Column(String(150), nullable=False)
    email = Column(String(255), nullable=False)
    telefono = Column(String(30), nullable=True)
    direccion = Column(String(255), nullable=True)
    id_perfil_tributario = Column(Integer, nullable=False)
    id_ciudad = Column(Integer, nullable=False)
    usuario = Column(String(80), nullable=True)
    password = Column(String(500), nullable=True)
    password_app = Column(String(500), nullable=True)
    archivo = Column(String(500), nullable=True)
    id_perfil = Column(Integer, nullable=False)
    acceso = Column(String(1000), nullable=True)
    inactivo = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user_create = Column(Integer, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    user_update = Column(Integer, nullable=True)
    deleted_at = Column(DateTime, default=datetime.datetime.utcnow)
    user_inactive = Column(Integer, nullable=True)
    
    def __init__(self, id, tipo_id, identificacion, nombre1, nombre2, apellido1,
                    apellido2, email, telefono, direccion, id_perfil_tributario, 
                    id_ciudad, usuario, password, password_app, archivo,
                    id_perfil, acceso, inactivo, created_at, user_create,
                    updated_at, user_update, deleted_at, user_inactive):
        self.id = id
        self.tipo_id = tipo_id
        self.identificacion = identificacion
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.id_perfil_tributario = id_perfil_tributario
        self.id_ciudad = id_ciudad 
        self.usuario = usuario 
        self.password = password
        self.password_app = password_app
        self.archivo = archivo 
        self.id_perfil = id_perfil 
        self.acceso = acceso 
        self.inactivo = inactivo 
        self.created_at = created_at 
        self.user_create = user_create 
        self.updated_at = updated_at 
        self.user_update = user_update 
        self.deleted_at = deleted_at 
        self.user_inactive = user_inactive
        
    def __repr__(self):
        return f" User({self.id}, {self.tipo_id}, {self.tipo_id}, {self.identificacion}, {self.nombre1}, {self.nombre2}, {self.apellido1}, {self.apellido2},  {self.email})"