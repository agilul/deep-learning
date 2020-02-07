from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from starlette.staticfiles import StaticFiles
from io import BytesIO
import aiohttp
from app.guitars import guitars


class UrlRequest(BaseModel):
    url: str


app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")


@app.post("/api/guitars/url")
async def guitars_route(urlRequest: UrlRequest):
    async with aiohttp.ClientSession() as session:
        async with session.get(urlRequest.url) as response:
            return guitars.handle(BytesIO(await response.read()))


@app.post("/api/guitars/upload")
async def guitars_upload(file: UploadFile = File(...)):
    return guitars.handle(BytesIO(await file.read()))
