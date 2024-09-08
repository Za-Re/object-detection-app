from fastapi import APIRouter, File, UploadFile, HTTPException
from app.models.model import YoloModel
from app.config import settings
from app.utils.file_utils import validate_file_extension
from enum import Enum
from starlette.responses import StreamingResponse
import io
import os
import numpy as np
import cv2


router = APIRouter()


class Model(str, Enum):
    yolov3tiny = "yolov3-tiny"
    yolov3 = "yolov3"


@router.get("/")
def home():
    return "This API serves object detection using yolov3 model. Visit /docs to try it out."


@router.post("/predict")
def prediction(model: Model, file: UploadFile = File(...)):
    validate_file_extension(file.filename)

    image_stream = io.BytesIO(file.file.read())
    image_stream.seek(0)

    file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if image is None:
        raise HTTPException(status_code=400, detail="Failed to decode image")

    yolo_model = YoloModel(model_name=model)
    output_image, _, _ = yolo_model.predict(image)

    output_path = os.path.join(settings.images_predicted_dir, file.filename)
    cv2.imwrite(output_path, output_image)

    file_image = open(output_path, mode="rb")
    return StreamingResponse(file_image, media_type="image/jpeg")