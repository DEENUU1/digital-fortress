from langchain import OpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

load_dotenv()


template = PromptTemplate.from_template(
    "You are part of the system that helps the user create a mind map, "
    "based on the given data you must return the best possible next scenario. "
    "{input}, take it into account: "
    "Previous scenarios: "
    "{scenarios}"
)

model = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
chain = LLMChain(llm=model, prompt=template)
x = chain.run(input="It must be written in Python", scenarios="I want to create a mind map")
print(x)