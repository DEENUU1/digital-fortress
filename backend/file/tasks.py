from file.processor.split import split_files
from file.embedding.pinecone import save_to_pinecone
from user.repository.user import UserAccountRepository
from celery import shared_task
from file.models import File


@shared_task()
def process_uploaded_file(file: File, user_id: int):
    file.status = 'Processing'
    file.save()

    chunks = split_files(file.file)

    user_repo = UserAccountRepository()
    user = user_repo.get_by_id(user_id)

    save_to_pinecone(chunks, user.openai_key, file.project.slug)

    file.status = 'Processed'
    file.save()
