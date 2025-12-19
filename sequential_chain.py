from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

prompt1 = PromptTemplate(
    template='Generate a detailed report about {topic}',
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template='Summarize the following report in 5 bullet points:\n\n{report}',
    input_variables=['report']
)

model=ChatGoogleGenerativeAI(api_key=api_key, model="gemini-2.5-flash")

parser = StrOutputParser()

chain = prompt1 | model | prompt2 | model | parser

result = chain.invoke({'topic':'Sustainable Energy Innovations'})

print(result)
# chain.get_graph().print_ascii()  # Requires grandalf: pip install grandalf
