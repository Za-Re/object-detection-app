from fastapi import HTTPException


def validate_file_extension(filename: str, allowed_extensions=("jpg", "jpeg", "png")):
    """Utility function to validate file extension"""
    file_extension = filename.split(".")[-1].lower()  # case-insensitive comparison
    if file_extension not in allowed_extensions:
        raise HTTPException(status_code=415, detail="Unsupported file provided.")