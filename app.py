from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path


app = FastAPI()


BASE_DIR = Path(__file__).resolve().parent


app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


@app.get("/", response_class=HTMLResponse)
async def home():
    html_file = BASE_DIR / "templates" / "index.html"

    with open(html_file, "r", encoding="utf-8") as file:
        return file.read()


@app.get("/api/hello")
async def hello():
    return {"message": "Hello World"}