from pydantic import BaseModel, Field
from typing import List, Literal, Optional


class ImageData(BaseModel):
    type: Optional[Literal["table", "picture"]] = Field(None, description="The type of the image")
    filename: Optional[str] = Field(None, description="The filename of the image")
    image: Optional[bytes] = Field(None, description="The image data")


class ConversionResult(BaseModel):
    filename: str = Field(None, description="The filename of the document")
    markdown: str = Field(None, description="The markdown content of the document")
    images: List[ImageData] = Field(default_factory=list, description="The images in the document")


class BatchConversionResult(BaseModel):
    conversion_results: List[ConversionResult] = Field(
        default_factory=list, description="The results of the conversions"
    )


class ConverstionJobResult(BaseModel):
    job_id: str = Field(..., description="The id of the conversion job")
    result: ConversionResult = Field(None, description="The result of the conversion job")
    error: Optional[str] = Field(None, description="The error that occurred during the conversion job")
    status: Literal["IN_PROGRESS", "SUCCESS", "FAILURE"] = Field(None, description="The status of the conversion job")


class BatchConversionJobResult(BaseModel):
    job_id: str = Field(..., description="The id of the conversion job")
    result: BatchConversionResult = Field(None, description="The result of the conversion job")
    completed: Optional[int] = None
    total: Optional[int] = None
    progress: Optional[str] = None
