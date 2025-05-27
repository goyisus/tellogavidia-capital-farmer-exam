from fastapi import FastAPI, Depends, Form
from starlette.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import date
from localStoragePy import localStoragePy
from sqlalchemy.orm import Session
from database import SessionLocal, Cliente

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Obtener la sesion de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Carga formulario
@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# Envia datos de formulario a guardar en la BD
@app.post("/submit")
async def submit_form(
    nombre: str = Form(...),
    correo: str = Form(...),
    servicio: str = Form(...),
    descripcion: str = Form(...),
    db: Session = Depends(get_db)
):
    localStorage = localStoragePy("mi_app", "sqlite")
    numeroCotizacion = 0
    if localStorage.getItem("numeroCotizacion") is None:
        localStorage.setItem("numeroCotizacion", "1")
        numeroCotizacion = localStorage.getItem("numeroCotizacion")
    else:
        numeroCotizacion = localStorage.getItem("numeroCotizacion")
        nuevoValor = int(numeroCotizacion) + 1
        localStorage.setItem("numeroCotizacion", str(nuevoValor))
    numeroFormateado = numeroCotizacion.zfill(4)
    nroCotizacionTxt = "COT-2025-"+ numeroFormateado
    
    match servicio:
        case "1":
            servicioCalculado = "S/. 1,500"
        case "2":
            servicioCalculado = "S/. 2,000"
        case "3":
            servicioCalculado = "S/. 800"

    fechaActual = date.today()

    nuevo_cliente = Cliente(numero_cotizacion=nroCotizacionTxt, precio_servicio=servicioCalculado, fecha_creacion=fechaActual, nombre=nombre, correo=correo, servicio=servicio, descripcion=descripcion)

    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)

    return {
    "numeroCotizacion": nroCotizacionTxt,
    "precioServicio": servicioCalculado,
    "fechaCreacion": fechaActual,
    "datosIncresados": {
        "nombre": nombre,
        "correo": correo,
        "servicio": servicio,
        "descripcion": descripcion
    }
}

# Obtiene las cotizaciones guardadas en la bd
@app.get("/cotizaciones")
async def obtener_cotizaciones_db(db: Session = Depends(get_db)):
    cotizaciones = db.query(Cliente).all()
    return cotizaciones