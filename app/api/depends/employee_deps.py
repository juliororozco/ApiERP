from fastapi import Depends, HTTPException, status
from uuid import UUID
from app.models.employee_model import Employee
from app.services.employee_service import EmployeeService

async def get_employee_by_id(employee_id: UUID) -> Employee:
    employee = await EmployeeService.get_employee_by_id(employee_id)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    return employee
