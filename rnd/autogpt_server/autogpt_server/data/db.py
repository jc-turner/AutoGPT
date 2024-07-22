from uuid import uuid4

from prisma import Prisma
from pydantic import BaseModel, Field, field_validator
from dotenv import load_dotenv
import os

load_dotenv()

PRISMA_SCHEMA = os.getenv("PRISMA_SCHEMA", "schema.prisma")
os.environ['PRISMA_SCHEMA_PATH'] = PRISMA_SCHEMA

prisma = Prisma(auto_register=True)


async def connect():
    if not prisma.is_connected():
        await prisma.connect()


async def disconnect():
    if prisma.is_connected():
        await prisma.disconnect()


class BaseDbModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

    @field_validator("id", mode="before")
    def set_model_id(cls, id: str) -> str:
        # In case an empty ID is submitted
        return id or str(uuid4())
