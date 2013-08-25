
DEBUG = True
SECRET_KEY = 'temporary_secret_key' # make sure to change this

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/flaskular.db'

#we send the angular main page with send_file so if we're in debug
#mode set the caching low. Otherwise it can be a week (or more).
SEND_FILE_MAX_AGE_DEFAULT = 0 if DEBUG else (60 * 60 * 24 * 7)
