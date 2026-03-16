from pydantic import BaseModel

class Metric(BaseModel):
    index: int
    value: float