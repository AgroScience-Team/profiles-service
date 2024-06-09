from pydantic import BaseModel


class ConsumerMessage(BaseModel):
    organization_id: int | None = None
    worker_ids: list[int]
