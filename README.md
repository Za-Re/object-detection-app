## Overview
This project demonstrates the deployment of an object detection machine learning model using FastAPI. The project leverages pre-trained YOLO models (e.g., YOLOv3-tiny) for detecting objects in images, providing an API to send images and receive the detected objects in response.

The client side can interact with the server by sending images, receiving object detection results, and saving the processed images locally.

The project idea is inspired by an example from [Machine Learning in Production Course by Andrew Ng](https://www.coursera.org/learn/introduction-to-machine-learning-in-production)

## How to Run the Project
### Install Dependencies

```pip install -r requirements.txt```

### Running FastAPI Server
To start the FastAPI server, run the main.py:

```python app/main.py```

If you encounter an error when running `python app/main.py` stating that the `app` module cannot be found, it may be due to an issue with the PYTHONPATH not being set correctly.
To fix this, set the PYTHONPATH environment variable before running the script: `export PYTHONPATH=.`


The server will start on localhost:8000 by default. You can access the FastAPI auto-generated documentation at:
```http://localhost:8000/docs```

### Running the Client
Once the server is up and running, you can use the client.py file to send images for object detection. The client interacts with the server by sending POST requests to the /predict endpoint.

```
cd app
python client.py
```

The client will process images located in the `../images_uploaded` directory and save the object-detected images to the `../images_predicted` directory.

