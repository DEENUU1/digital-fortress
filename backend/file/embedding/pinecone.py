from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone
from typing import List
from langchain.docstore.document import Document
import os
from django.conf import settings


os.environ["PINECONE_API_KEY"] = settings.PINECONE_API_KEY


def get_embedding_func(openai_key: str) -> OpenAIEmbeddings:
    return OpenAIEmbeddings(openai_api_key=openai_key)


def get_pinecone(openai_key: str, project_slug: str) -> Pinecone:
    return Pinecone.from_existing_index(
        index_name=settings.PINECONE,
        embedding=get_embedding_func(openai_key),
        namespace=project_slug
    )


def save_to_pinecone(data: List[Document], openai_key: str, project_slug: str):
    vector_db = Pinecone.from_documents(
        data,
        get_embedding_func(openai_key),
        index_name=settings.PINECONE,
        namespace=project_slug
    )
    return vector_db
