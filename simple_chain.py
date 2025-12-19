from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model=ChatGoogleGenerativeAI(api_key=api_key, model="gemini-2.5-flash")

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})

print(result)
# chain.get_graph().print_ascii()  # Requires grandalf: pip install grandalf
