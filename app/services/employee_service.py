from datetime import datetime
from typing import Optional
from uuid import UUID
from app.models.employee_model import Employee
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate

class EmployeeService:
    @staticmethod
    async def create_employee(data: EmployeeCreate) -> Employee:
        employee = Employee(
            enterprise_id=data.enterprise_id,
            name=data.name,
            email=data.email,
            phone=data.phone,
            position=data.position,
            salary=data.salary,
            cedula=data.cedula
        )
        await employee.insert()
        return employee

    @staticmethod
    async def get_employee_by_id(employee_id: UUID) -> Optional[Employee]:
        return await Employee.find_one(Employee.employee_id == employee_id)

    @staticmethod
    async def update_employee(employee_id: UUID, data: EmployeeUpdate) -> Optional[Employee]:
        employee = await Employee.find_one(Employee.employee_id == employee_id)
        if employee:
            if data.name is not None:
                employee.name = data.name
            if data.email is not None:
                employee.email = data.email
            if data.phone is not None:
                employee.phone = data.phone
            if data.position is not None:
                employee.position = data.position
            if data.salary is not None:
                employee.salary = data.salary
            if data.termination_date is not None:
                employee.termination_date = data.termination_date
            if data.cedula is not None:
                employee.cedula = data.cedula
            await employee.save()
        return employee

    @staticmethod
    async def terminate_employee(employee_id: UUID) -> Optional[Employee]:
        employee = await Employee.find_one(Employee.employee_id == employee_id)
        if employee:
            employee.termination_date = datetime.utcnow()
            await employee.save()
        return employee
