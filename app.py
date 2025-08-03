from fastapi import FastAPI
from dotenv import load_dotenv
from controllers.calc_controller import router as calc_router
from controllers.agent_controller import router as agent_router

load_dotenv()

app = FastAPI()

app.include_router(calc_router)
app.include_router(agent_router)
