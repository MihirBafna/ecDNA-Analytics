class Config(object):
    DEBUG = False
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    
    ALLOWED_INPUT_IMAGE_EXTENSIONS = ["TIF", "TIFF"]
    ALLOWED_OUTPUT_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG", "TIF", "TIFF"]

    IMAGE_UPLOADS = "app/static/img"

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True



