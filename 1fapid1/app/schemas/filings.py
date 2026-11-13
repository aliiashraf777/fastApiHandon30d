# 2fastApi\1fastApiHandon30d\1fapid1\app\4pydanticSchemas.py

from typing import Literal
from pydantic import BaseModel, Field

filing_status = Literal[
    "pending",
    "submitted",
    "approved"
]

class FilingResponseData(BaseModel):
    # BaseModel - this creates Pydantic Schema Model, It defines the expected structure and types of a filing response.
    id: int
    taxpayer_id: int
    tax_year: int = Field(ge=2020, le=2100)
    # Field - adds validation constraints to the field
    status: filing_status
    # filing_status - restricts the status to the predefined literal string values
    
class FilingResponseList(BaseModel):
    status: Literal["success"]
    count: int = Field(ge=0)
    data: list[FilingResponseData]
    # Nested Schemas - this means data must contain a list of filling objects that follow the filing_response_data schema data structure