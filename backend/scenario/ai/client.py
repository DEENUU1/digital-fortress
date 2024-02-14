from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from typing import Optional


class AIClient:
    def __init__(self, openai_key: str, model: str):
        self.__openai_key = openai_key
        self.__model = model

    def __get_llm(self) -> ChatOpenAI:
        return ChatOpenAI(openai_api_key=self.__openai_key, model=self.__model)

    @staticmethod
    def __get_prompt() -> PromptTemplate:
        return PromptTemplate.from_template(
            "You are part of the system that helps the user create a mind map, "
            "based on the given data you must return the best possible next scenario. "
            "{input}, take it into account: "
            "Previous scenarios: "
            "{scenarios}"
        )

    def __get_chain(self) -> LLMChain:
        __llm = self.__get_llm()
        __prompt = self.__get_prompt()

        return LLMChain(llm=__llm, prompt=__prompt)

    def run(self, user_input: Optional[str] = "", scenarios: Optional[str] = "") -> str:
        __chain = self.__get_chain()
        return __chain.run(input=user_input, scenarios=scenarios)
