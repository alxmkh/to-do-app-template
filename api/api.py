from pathlib import Path

import requests
from fastapi import APIRouter, HTTPException, Request
from starlette.responses import FileResponse

router = APIRouter()

mockResult: dict = {
    "message": "Welcome to your todo list"
}


@router.get('/app', tags=['Application'])
async def get_root() -> dict:
    return mockResult


# prod
# volume_path = '/usr/src/app/files/image.jpeg'
# test
volume_path = 'static/images/image.jpeg'


@router.get('/download-image', tags=['Images'])
async def download_new_image_from_picsum() -> dict:
    page = requests.get('https://picsum.photos/1200')
    with open(volume_path, 'wb') as f:
        f.write(page.content)
    return {"result": "Image downloaded"}


@router.get('/get-image', tags=['Images'])
async def get_image():
    if not Path(volume_path).exists():
        raise HTTPException(status_code=404, detail="Item not found")
    return FileResponse(volume_path)
