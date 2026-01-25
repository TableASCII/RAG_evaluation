from pydantic import BaseModel

class Doc(BaseModel):
    text: str
    score: float | None

class RAGRecord(BaseModel):
    query: str
    retrieved_docs: list[Doc]
    prompt: str| None
    answer: str

