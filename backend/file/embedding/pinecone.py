from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone


def get_embedding_func(openai_key: str) -> OpenAIEmbeddings:
    return OpenAIEmbeddings(openai_api_key=openai_key)


def get_pinecone(pinecone_index: str, openai_key: str) -> Pinecone:
    return Pinecone.from_existing_index(
        index_name=pinecone_index,
        embedding=get_embedding_func(openai_key),
    )
