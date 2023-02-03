import configparser

filename = "settings.ini"
section = "APP"
config = configparser.ConfigParser()

config.read(filename)

CLIENT_ID = config.get(section, "CLIENT_ID")
CLIENT_SECRET = config.get(section, "CLIENT_SECRET")
REDIRECT_URI = config.get(section, "REDIRECT_URI")
TOKEN = config.get(section, "TOKEN")

