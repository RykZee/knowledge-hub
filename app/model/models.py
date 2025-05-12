from pydantic import BaseModel


class QuestionPayload(BaseModel):
    question: str
