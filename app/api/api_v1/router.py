from fastapi import APIRouter
from app.api.api_v1.handlers import user, enterprise, employee, financial_record
from app.api.auth.jwt import auth_router

router = APIRouter()
router.include_router(user.user_router, prefix='/users', tags=['users'])
router.include_router(auth_router, prefix='/auth', tags=['auth'])
router.include_router(enterprise.enterprise_router, prefix='/enterprises', tags=['enterprises'])
router.include_router(employee.employee_router, prefix='/employees', tags=['employees'])
router.include_router(financial_record.financial_record_router, prefix='/financial-records', tags=['financial-records'])
