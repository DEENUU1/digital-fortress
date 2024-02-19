from processor.split import split_files
from embedding.pinecone import save_to_pinecone
from file.repository.file import FileRepository
from user.repository.user import UserAccountRepository
from celery import shared_task


@shared_task()
def process_uploaded_file(_id: int, user_id: int):

    file_repo = FileRepository()
    file = file_repo.get_by_id(_id)

    chunks = split_files(file.file)

    user_repo = UserAccountRepository()
    user = user_repo.get_by_id(user_id)

    save_to_pinecone(chunks, user.openai_key)
