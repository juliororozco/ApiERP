from fastapi import FastAPI
from app.core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.models.user_model import User
from app.models.enterprise_model import Enterprise
from app.models.employee_model import Employee
from app.models.financial_record_model import FinancialRecord
from app.api.api_v1.router import router

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.on_event("startup")
async def app_init():
    """
    Inicializando los servicios
    """
    db_client = AsyncIOMotorClient(settings.MONGO_DB_CONNECTION)

    # Intenta establecer la conexión a la base de datos
    try:
        await db_client.server_info()  # Realiza una solicitud al servidor de la base de datos
        print("¡Conexión a la base de datos exitosa!")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

    # Inicializa Beanie con los modelos User, Enterprise, Employee y FinancialRecord
    await init_beanie(
        database=db_client["ERP"],  # especificamos en qué base de datos queremos trabajar.
        document_models=[User, Enterprise, Employee, FinancialRecord]
    )

app.include_router(router, prefix=settings.API_V1_STR)
