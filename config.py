import configparser

filename = "settings.ini"
section_app= "APP"
section_db = "DDBB"

config = configparser.ConfigParser()
config.read(filename)

#APP
TOKEN = config.get(section_app, "TOKEN")

#DDBB
HOST_NAME= config.get(section_db, "HOST_NAME")
USER= config.get(section_db, "USER")
PW = config.get(section_db, "PASSWORD")
DB_NAME = config.get(section_db, "DB_NAME")



