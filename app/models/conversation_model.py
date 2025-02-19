from pydantic import BaseModel
from datetime import datetime

class Conversation(BaseModel):
    id: int
    user: str
    message: str
    response: str
    timestamp: datetime
