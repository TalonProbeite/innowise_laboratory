from fastapi import FastAPI
import uvicorn
from sqlalchemy.ext.asyncio import create_async_engine , async_sessionmaker
from sqlalchemy.orm import DeclarativeBase , Mapped , mapped_column 


engine = create_async_engine(r"sqlite+aiosqlite:///lecture_5\book_api\Book.db")


new_session = async_sessionmaker(engine,expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session


class Base(DeclarativeBase):
    pass

class BookModel(Base):
    __tablename__ = "Book"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    author: Mapped[str]
    year: Mapped[int]


async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


app = FastAPI()

@app.post("/books/")
async def add_book():
    pass


@app.get("/books/")
async def get_books():
    pass


@app.delete("/books/{book_id}")
async def delet_book_by_id():
    pass


@app.put("/books/{book_id}")
async def update_book_details():
    pass

@app.get("/books/search/")
async def get_books2():
    pass

