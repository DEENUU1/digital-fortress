from typing import Optional

from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain_core.tools import Tool

from file.embedding.pinecone import get_pinecone


class AIClient:
    def __init__(self, openai_key: str, model: str):
        self.__openai_key = openai_key
        self.__model = model

    def __get_llm(self) -> ChatOpenAI:
        return ChatOpenAI(openai_api_key=self.__openai_key, model=self.__model)

    @staticmethod
    def __get_prompt(_input, scenarios) -> str:
        return f""" 
            You are part of the system that helps the user create a mind map, 
            based on the given data you must return the best possible next scenario. 
            {_input}, take it into account: 
            Previous scenarios: 
            {scenarios}
        """

    def __get_retrieval_qa(self, project_slug: str) -> RetrievalQA:
        __llm = self.__get_llm()

        return RetrievalQA.from_chain_type(
            llm=__llm,
            chain_type="stuff",
            retriever=get_pinecone(self.__openai_key, project_slug).as_retriever(
                search_type="similarity",
                search_kwargs={"k": 3}
            ),
        )

    def __get_tools(self, project_slug: str):
        qa = self.__get_retrieval_qa(project_slug)

        return [
            Tool(
                name="User-private-data",
                func=qa.run,
                description="Useful when you need more data to answer question"
            ),
        ]

    def run(self, project_slug: str, user_input: Optional[str] = "", scenarios: Optional[str] = "") -> str:
        prompt_agent = OpenAIFunctionsAgent.create_prompt(
            system_message=SystemMessage(content=self.__get_prompt(user_input, scenarios))
        )

        agent = OpenAIFunctionsAgent(llm=self.__get_llm(), prompt=prompt_agent, tools=self.__get_tools(project_slug))
        return AgentExecutor(
            agent=agent,
            tools=self.__get_tools(project_slug),
            verbose=False,
            handle_parsing_errors=True
        ).run(input=user_input)
