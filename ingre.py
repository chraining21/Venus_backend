import optional as optional
from pydantic import BaseModel
from typing import List
class ingres(BaseModel):
    name: str
    whatitdoes: List[str] = []
    irritancy: str
    comedogenicity: str
    tier: str
    class Config:
        orm_mode = True