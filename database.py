from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de SQLite
DATABASE_URL = "sqlite:///./cotizacion.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo de datos
class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    numero_cotizacion = Column(String)
    precio_servicio = Column(String)
    fecha_creacion = Column(String)
    nombre = Column(String)
    correo = Column(String)
    servicio = Column(String)
    descripcion = Column(String)

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)