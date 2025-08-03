from tools.math_tool import calculate
from langchain_openai import ChatOpenAI
from tools.weather_tool import get_weather
from langchain.agents import initialize_agent, AgentType

from dotenv import load_dotenv
load_dotenv()  # ✅ Load .env before anything else

# Define tools and LLM
tools = [get_weather, calculate]
llm = ChatOpenAI(temperature=0.3)

# Expose the initialized agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)
