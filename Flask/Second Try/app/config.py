class Config(object):
    IMAGE_UPLOADS = "./app/static/uploads"
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG", "GIF"]
    MAX_IMAGE_FILESIZE = 0.5 * 1024 * 1024
    CLIENT_IMAGES = "./static/client/img"
    CLIENT_CSV = "/home/gabriel/Programação/Python-Learning/Flask/Second Try/app/app/static/client/csv/"
    CLIENT_PDF = "/home/gabriel/Programação/Python-Learning/Flask/Second Try/app/app/static/client/pdf/"
    CLIENT_REPORTS = "/home/gabriel/Programação/Python-Learning/Flask/Second Try/app/app/static/client/reports/"

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    IMAGE_UPLOADS = "./app/static/uploads"

class TestingConfig(Config):
    pass