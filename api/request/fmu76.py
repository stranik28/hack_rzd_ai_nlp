from api.request.base import RequestBase
from pydantic import Field
from typing import Optional


class fmu76Request(RequestBase):
    act_number: Optional[str] = Field(None)
    organization: Optional[str] = Field(None)
    organization_structure: Optional[str] = Field(None)
    ocud_code: Optional[str] = Field(None)
    okpo_code: Optional[str] = Field(None)
    code_be: Optional[str] = Field(None)
    boss: Optional[str] = Field(None)
    sign_encode: Optional[str] = Field(None)
    subdivision: Optional[str] = Field(None)
    operation_code: Optional[str] = Field(None)
    sender_org_str: Optional[str] = Field(None)
    check: Optional[str] = Field(None)
    expense_direction: Optional[str] = Field(None)
    financially_responsible_person: Optional[str] = Field(None)
