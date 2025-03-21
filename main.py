from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers import users

app = FastAPI()

app.include_router(users.router, tags=['users'], prefix='/api')

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})