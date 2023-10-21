from typing import Union
from fastapi import FastAPI,  File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
import io
from PIL import Image
import torchvision.transforms as transforms
import torch

from model.classifaer import Predictor

app = FastAPI()


@app.get("/")
async def read_root():
    return RedirectResponse("/docs#/default/get_root__post", status_code=302)

@app.post("/")
async def get_root(file: UploadFile):
    with open(file.filename, "wb") as f:
        f.write(file.file.read())
    img = Image.open(file.filename)
    transform = transforms.Compose([transforms.Resize((224, 224)),
                                    transforms.ToTensor()])
    img = transform(img)


    model =  Predictor()
    output = model.pred(img.unsqueeze(0))
    return {"prediction": output}