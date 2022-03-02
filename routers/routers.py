from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request, APIRouter

from helpers import helpers

router = APIRouter()
templates = Jinja2Templates(directory='templates')
tasks: list = ['task 1', 'task 2', 'task 3', 'task 4']


@router.get('/', response_class=HTMLResponse, tags=['UI'])
async def index(request: Request):
    data: dict = {
        "image": helpers.decode_image('static/images/image.jpeg'),
        "tasks": tasks,
    }
    return templates.TemplateResponse('index.html', {'request': request, 'data': data})
