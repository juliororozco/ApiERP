# app/services/enterprise_service.py
from typing import Optional
from uuid import UUID
from app.models.enterprise_model import Enterprise
from app.schemas.enterprise_schema import EnterpriseCreate, EnterpriseUpdate

class EnterpriseService:
    @staticmethod
    async def create_enterprise(data: EnterpriseCreate, owner_id: UUID) -> Enterprise:
        enterprise = Enterprise(
            name=data.name,
            address=data.address,
            phone=data.phone,
            email=data.email,
            tax_id=data.tax_id,
            owner_id=owner_id
        )
        await enterprise.insert()  # Usamos insert en lugar de save para nuevos documentos
        return enterprise

    @staticmethod
    async def get_enterprise_by_id(enterprise_id: UUID) -> Optional[Enterprise]:
        return await Enterprise.find_one(Enterprise.enterprise_id == enterprise_id)

    @staticmethod
    async def update_enterprise(enterprise_id: UUID, data: EnterpriseUpdate) -> Optional[Enterprise]:
        enterprise = await Enterprise.find_one(Enterprise.enterprise_id == enterprise_id)
        if enterprise:
            if data.name is not None:
                enterprise.name = data.name
            if data.address is not None:
                enterprise.address = data.address
            if data.phone is not None:
                enterprise.phone = data.phone
            if data.email is not None:
                enterprise.email = data.email
            if data.tax_id is not None:
                enterprise.tax_id = data.tax_id
            await enterprise.save()  # Usamos save para actualizar documentos existentes
        return enterprise
