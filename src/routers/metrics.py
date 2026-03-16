from fastapi import APIRouter
from src.models import Metric

router = APIRouter()

@router.get("/metrics")
def read_metrics():
    return [Metric(index=1, value=10.0), Metric(index=2, value=20.0)]