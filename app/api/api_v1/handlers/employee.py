from fastapi import APIRouter, HTTPException, status, Depends
from uuid import UUID
import pymongo
from app.models.employee_model import Employee
from app.schemas.employee_schema import EmployeeCreate, EmployeeOut, EmployeeUpdate
from app.services.employee_service import EmployeeService
from app.services.financial_record_service import FinancialRecordService
from app.api.depends.user_deps import get_current_user
from app.api.depends.employee_deps import get_employee_by_id
from app.models.user_model import User

employee_router = APIRouter()

@employee_router.post('/create', summary="Create new employee", response_model=EmployeeOut)
async def create_employee(data: EmployeeCreate, current_user: User = Depends(get_current_user)):
    employee = await EmployeeService.create_employee(data)
    
    # Actualizar registros financieros
    description = f"Nuevo empleado contratado: {data.name}"
    await FinancialRecordService.update_financial_record_on_employee_change(
        enterprise_id=data.enterprise_id, 
        type="expense", 
        amount=data.salary, 
        description=description
    )
    return employee

@employee_router.get('/{employee_id}', summary="Get employee by ID", response_model=EmployeeOut)
async def get_employee_by_id_route(employee: Employee = Depends(get_employee_by_id)):
    return employee

@employee_router.put('/{employee_id}', summary="Update employee", response_model=EmployeeOut)
async def update_employee(employee_id: UUID, data: EmployeeUpdate, current_user: User = Depends(get_current_user), employee: Employee = Depends(get_employee_by_id)):
    # Optionally, check if the user has permission to update the employee
    updated_employee = await EmployeeService.update_employee(employee_id, data)
    return updated_employee

@employee_router.put('/{employee_id}/terminate', summary="Terminate employee", response_model=EmployeeOut)
async def terminate_employee(employee_id: UUID, current_user: User = Depends(get_current_user)):
    terminated_employee = await EmployeeService.terminate_employee(employee_id)
    
    # Actualizar registros financieros
    description = f"Empleado despedido: {terminated_employee.name}"
    await FinancialRecordService.update_financial_record_on_employee_change(
        enterprise_id=terminated_employee.enterprise_id, 
        type="expense", 
        amount=terminated_employee.salary, 
        description=description
    )
    return terminated_employee
