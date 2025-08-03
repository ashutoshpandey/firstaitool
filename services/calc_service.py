import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()  # ✅ Load .env file manually

llm = ChatOpenAI(
    temperature=0.2,
    api_key=os.getenv("OPENAI_API_KEY")
)

# Prompt template for math evaluation
prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You are a math expert. Answer the following math question accurately.
You have to return answer in json without any text.

Question: {question}
Answer:
"""
)

# LLM Chain with the prompt
math_chain = LLMChain(llm=llm, prompt=prompt)

# Service method
def evaluate_math_question(question: str) -> str:
    response = math_chain.run({"question": question})
    return response.strip()
