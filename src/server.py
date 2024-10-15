from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from excgrouper import ExcGrouper
from datetime import datetime

app = FastAPI()
grouper = ExcGrouper()

class ExceptionInput(BaseModel):
    message: str
    type: str = "Unknown"
    timestamp: datetime = None
    context: dict = {}

class GroupResult(BaseModel):
    group_id: str

@app.post("/process", response_model=GroupResult)
async def process_exception(exception: ExceptionInput):
    try:
        group_id = grouper.group_exception(
            message=exception.message,
            type_name=exception.type,
            timestamp=exception.timestamp or datetime.now(),
            **exception.context
        )
        return GroupResult(group_id=group_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/top_exceptions")
async def get_top_exceptions(limit: int = 10, days: int = 1):
    try:
        return grouper.get_top_exceptions(limit=limit, days=days)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))