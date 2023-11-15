from datetime import datetime

from pydantic import BaseModel


class TokenPayloadSchema(BaseModel):
    iat: datetime
    exp: datetime
    sub: str
    role: str
    email: str
    org: int
