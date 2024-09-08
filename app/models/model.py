import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox


class YoloModel:
    def __init__(self, model_name="yolov3-tiny"):
        self.model_name = model_name

    def predict(self, image):
        # Detect objects using cvlib's YOLO model
        bbox, label, conf = cv.detect_common_objects(image, model=self.model_name)
        output_image = draw_bbox(image, bbox, label, conf)
        return output_image, label, conf