from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone
from typing import List
from langchain.docstore.document import Document


def get_embedding_func(openai_key: str) -> OpenAIEmbeddings:
    return OpenAIEmbeddings(openai_api_key=openai_key)


def get_pinecone(openai_key: str) -> Pinecone:
    return Pinecone.from_existing_index(
        index_name=..., # todo add index here
        embedding=get_embedding_func(openai_key),
    )


def save_to_pinecone(data: List[Document], openai_key: str):
    vector_db = Pinecone.from_documents(
        data,
        get_embedding_func(openai_key),
        index_name=..., # todo add index here
    )
    return vector_db
