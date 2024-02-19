from langchain.document_loaders import PyPDFLoader, CSVLoader, JSONLoader, UnstructuredMarkdownLoader, TextLoader


class DataLoaderFactory:
    @staticmethod
    def split_docs(file_path: str):
        if file_path.endswith(".pdf"):
            return PyPDFLoader(file_path)
        elif file_path.endswith(".csv"):
            return CSVLoader(file_path)
        elif file_path.endswith(".json"):
            return JSONLoader(file_path)
        elif file_path.endswith(".md"):
            return UnstructuredMarkdownLoader(file_path)
        elif file_path.endswith(".txt"):
            return TextLoader(file_path, encoding="utf-8")
        else:
            raise ValueError("Invalid file type")
