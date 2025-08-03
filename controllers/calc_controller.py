from fastapi import APIRouter, Query
from services.calc_service import evaluate_math_question

router = APIRouter()

@router.get("/calculate")
async def calculate(question: str = Query(..., description="Math expression in natural language")):
    try:
        result = evaluate_math_question(question)
        return {"response": result}
    except Exception as e:
        return {"error": str(e)}
