from pathlib import Path

from PIL import Image
import base64
import io

from fastapi import HTTPException


def decode_image(path: str) -> str | Exception:
    if not Path(path).exists():
        raise HTTPException(status_code=404, detail="File not found")
    try:
        im = Image.open(path)
        im_data = io.BytesIO()
        im.save(im_data, "JPEG")
        encoded_img_data = base64.b64encode(im_data.getvalue())
        return encoded_img_data.decode('utf-8')
    except Exception as err:
        return err
