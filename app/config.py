from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Object Detection API"
    debug: bool = True
    host: str = "127.0.0.1"
    port: int = 8000
    base_url: str = "http://localhost:8000"
    endpoint: str = "/predict"
    images_uploaded_dir: str = "../images_uploaded"
    images_predicted_dir: str = "../images_predicted"
    model_default: str = "yolov3-tiny"

    class Config:
        env_file = ".env"
        protected_namespaces = ('settings_',)


settings = Settings()
