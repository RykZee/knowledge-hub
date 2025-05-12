from fastapi import FastAPI, APIRouter, UploadFile, File, BackgroundTasks
from uuid import uuid4
from app.service.llm_service import query_llm
import os
from app.model.models import QuestionPayload

router = APIRouter()

def noop(file_path, document_id, metadata):
    pass

@router.post("/documents")
async def upload_document(
    file: UploadFile = File(...), background_tasks: BackgroundTasks = None
):
    """Upload and process a document of type PDF/docx to be used for RAG"""
    document_id = str(uuid4())
    file_path = os.path.join("/", "tmp", f"{document_id}_{file.filename}")

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    background_tasks.add_task(
        noop,
        # document_processor.process_document,
        file_path=file_path,
        document_id=document_id,
        metadata={"filename": file.filename},
    )

    return {"document_id": document_id, "status": "processing"}


@router.post("/query")
async def query(payload: QuestionPayload):
    return query_llm(payload.question)


def create_app():
    app = FastAPI(title="Knowledge Hub")

    return app
