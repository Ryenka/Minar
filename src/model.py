from pydantic import BaseModel, Field


class Repository(BaseModel):
    full_name: str = Field(
        ..., description="Nombre completo en formato 'owner/repo'"
    )


class DetectionResult(BaseModel):
    full_name: str
    uses_gh_aw: int