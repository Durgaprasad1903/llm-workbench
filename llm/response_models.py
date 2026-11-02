from pydantic import BaseModel, Field


class TopicResponse(BaseModel):
    topic: str
    difficulty: str
    score: int = Field(ge=0, le=100)