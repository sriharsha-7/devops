from pydantic import BaseModel
from typing import Optional
from pydantic import EmailStr
from pydantic import BaseModel, ValidationError, validator

def validate_string(v):
    trim = v.strip()
    if not trim:
        raise ValidationError("empty string")
    return v

class PrInfo(BaseModel):
    repo: str
    owner: str
    email: Optional[EmailStr]

    @validator('repo')
    def validate_repo(cls, v):
        return validate_string(v)
    
    @validator('owner')
    def validate_owner(cls, v):
        return validate_string(v)



