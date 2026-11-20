from os import getenv

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

AZURE_OPENAI_DEPLOYMENT = getenv("AZURE_OPENAI_DEPLOYMENT")
AZURE_OPENAI_ENDPOINT = getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = getenv("AZURE_OPENAI_API_KEY")

llm = ChatOpenAI(
    model=AZURE_OPENAI_DEPLOYMENT,
    base_url=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
)
