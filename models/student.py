from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class StudentModel(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(...)
    gpa: float = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Elon Musk",
                "email": "elon@gmail.com",
                "course_of_study": "Rocket Science",
                "year": 2,
                "gpa": "3.0"
            }
        }


class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Elon Musk",
                "email": "elon@gmail.com",
                "course_of_study": "Rocket Science",
                "year": 4,
                "gpa": "5.0"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [
            data
        ],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }
