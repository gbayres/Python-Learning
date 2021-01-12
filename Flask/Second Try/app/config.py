class Config(object):
    IMAGE_UPLOADS = "./app/static/uploads"
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG", "GIF"]
    MAX_IMAGE_FILESIZE = 0.5 * 1024 * 1024

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    IMAGE_UPLOADS = "./app/static/uploads"

class TestingConfig(Config):
    pass