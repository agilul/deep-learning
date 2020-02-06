from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from app.guitars import guitars

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")


@app.get("/api/guitars")
async def guitars_route():
    return await guitars.handle()
