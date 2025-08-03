from langchain_core.tools import tool

@tool
def calculate(expression: str) -> str:
    """Evaluates a simple math expression like '2 + 3 * 4'."""
    try:
        result = eval(expression)
        return f"The result is {result}"
    except Exception as e:
        return f"Error: {str(e)}"
