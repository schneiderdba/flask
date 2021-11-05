# config.py you can put this file anywhere in the project
# https://stackoverflow.com/questions/9845102/using-mysql-in-flask
class Config(object):
    DEBUG   = False
    TESTING = False

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = ''
    MYSQL_DATABASE_HOST = '127.0.0.1'
    MYSQL_DATABASE_DB = 'flask'  # can be any

    DEBUG = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = ''
    MYSQL_DATABASE_HOST = '127.0.0.1' # eg to amazone db :- yourdbname.xxxxxxxxxx.us-east-2.rds.amazonaws.com
    MYSQL_DATABASE_DB = 'flask'

    DEBUG = False