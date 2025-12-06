from fastapi import FastAPI , Depends
from typing import Annotated , Optional
import uvicorn
from sqlalchemy.ext.asyncio import create_async_engine , async_sessionmaker , AsyncSession
from sqlalchemy.orm import DeclarativeBase , Mapped , mapped_column 
from pydantic import BaseModel, Field
from sqlalchemy import select


engine = create_async_engine(r"sqlite+aiosqlite:///Book.db")


new_session = async_sessionmaker(engine,expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session

sessionDep = Annotated[AsyncSession , Depends(get_session)]

class Base(DeclarativeBase):
    pass

class BookModel(Base):
    __tablename__ = "Book"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    author: Mapped[str]
    year: Mapped[Optional[int]] = mapped_column(nullable=True)


async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


app = FastAPI()


class BookAddSchema(BaseModel): 
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: Optional[int] = None

class BookSchema(BookAddSchema):
    id: int



@app.post("/books/")
async def add_book(data: BookAddSchema, session: sessionDep):
    new_book = BookModel(
        title = data.title,
        author = data.author,
        year = data.year
    )
    session.add(new_book)
    await session.commit()
    return {"success": True}

@app.get("/books/")
async def get_books(session:sessionDep):
    query = select(BookModel)
    result = await session.execute(query)
    books = result.scalars().all()
    return books

    


@app.delete("/books/{book_id}")
async def delet_book_by_id():
    pass


@app.put("/books/{book_id}")
async def update_book_details():
    pass

@app.get("/books/search/")
async def get_books2():
    pass
