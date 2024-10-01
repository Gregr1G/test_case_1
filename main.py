import uvicorn
from fastapi import FastAPI
from src.api.routers import get_routers


app = FastAPI(
    title="Тестовое задание"
)


app.include_router(get_routers())


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)