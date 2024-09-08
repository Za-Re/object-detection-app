from config import settings
import os
import io
import cv2
import requests
import numpy as np


full_url = f"{settings.base_url}{settings.endpoint}?model={settings.model_default}"


def response_from_server(url, image_file, verbose=True):
    # Send a POST request to the server with the image file
    files = {'file': image_file}
    response = requests.post(url, files=files)
    status_code = response.status_code

    if verbose:
        if status_code == 200:
            msg = f"The file {image_file.name} is processed successfully."
        else:
            msg = "There was an error when handling the request."
    print(msg)

    return response


if not os.path.exists(settings.images_predicted_dir):
    os.mkdir(settings.images_predicted_dir)


def display_image_from_response(response, filename="apple.jpg"):
    # Check the status code and content type of the response
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        print(f"Response content: {response.text}")
        return

    content_type = response.headers.get('Content-Type')
    if 'image' not in content_type:
        print(f"Error: Expected image but received {content_type}")
        print(f"Response content: {response.text}")
        return

    image_stream = io.BytesIO(response.content)
    image_stream.seek(0)
    file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if image is None or image.size == 0:
        print("Error: Failed to decode image from server response.")
        return

    cv2.imwrite(f'{settings.images_predicted_dir}/{filename}', image)


def main():
    images_dir = settings.images_uploaded_dir

    image_files = [
        'car2.jpg',
        'clock3.jpg',
        'apples.jpg'
    ]

    for image_file_name in image_files:
        image_path = os.path.join(images_dir, image_file_name)

        with open(image_path, "rb") as image_file:
            prediction = response_from_server(full_url, image_file, verbose=True)

        display_image_from_response(prediction, filename=image_file_name)


if __name__ == "__main__":
    main()