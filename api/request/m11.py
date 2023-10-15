from api.request.base import RequestBase
from pydantic import Field
from typing import Optional


class m11Table1(RequestBase):
    act_date: Optional[str] = Field(None)
    operation_code: Optional[str] = Field(None)
    sender_org_str: Optional[str] = Field(None)
    sender_tabl_numb: Optional[str] = Field(None)
    receiver_org_str: Optional[str] = Field(None)
    receiver_tabl_numb: Optional[str] = Field(None)
    check: Optional[str] = Field(None)
    analytic_report_code: Optional[str] = Field(None)
    accounting_unit: Optional[str] = Field(None)


class m11Request(RequestBase):
    act_number: Optional[str] = Field(None)
    organization: Optional[str] = Field(None)
    organization_structure: Optional[str] = Field(None)
    ocud_code: Optional[str] = Field(None)
    okpo_code: Optional[str] = Field(None)
    code: Optional[str] = Field(None)
    table1: Optional[list[m11Table1]] = Field(None)
    throw_person: Optional[str] = Field(None)
    requested: Optional[str] = Field(None)
    approved: Optional[str] = Field(None)
