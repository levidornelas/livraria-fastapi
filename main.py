from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager
import uvicorn

from db import create_db_and_tables
from resources import books, users, author

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    print("Banco de dados inicializado")
    yield
    print("Encerrando aplicação...")

app = FastAPI(title="Books API", lifespan=lifespan)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(books.router)
app.include_router(users.router)
app.include_router(author.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)