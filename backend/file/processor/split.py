from typing import Optional, List
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from .data_loader_factory import DataLoaderFactory


def split_files(file_path: Optional[str] = None) -> List[Document]:
    """
    Split files into chunks
    """
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    loader = DataLoaderFactory().split_docs(file_path=file_path)
    document = loader.load()
    documents = text_splitter.split_documents(document)

    return documents
