import configparser

filename = "settings.ini"
section = "APP"
config = configparser.ConfigParser()

config.read(filename)

CLIENT_ID = config.get(section, "CLIENT_ID")
TOKEN = config.get(section, "TOKEN")

