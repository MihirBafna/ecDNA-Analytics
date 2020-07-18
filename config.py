import secrets
import os

class Config(object):
    DEBUG = False
    
    ALLOWED_INPUT_IMAGE_EXTENSIONS = ["TIF", "TIFF"]
    ALLOWED_OUTPUT_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG", "TIF", "TIFF"]

    IMAGE_UPLOADS = "app/static/img"
    IMAGE_DOWNLOADS = "app/static/client/img"
    EMAIL_USERNAME=os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD')
    # ECSEG_LOCATION = "/Users/MihirBafna/Documents/CS/Projects/ecSeg"
    # METADETECT_LOCATION=""

class ProductionConfig(Config):
    SECRET_KEY = secrets.token_urlsafe(16)

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/' #development secret key
    # ECSEG_LOCATION = "/Users/MihirBafna/Documents/CS/Projects/ecSeg"



