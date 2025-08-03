from pydantic import BaseModel
from fastapi import APIRouter, Query
from services.agent_service import agent

router = APIRouter()

class Query(BaseModel):
    question: str

@router.post("/ask")
async def ask_agent(query: Query):
    try:
        answer = agent.run(query.question)
        return {"response": answer}
    except Exception as e:
        return {"error": str(e)}
