import yaml


infile = open("buildbot_config/config.yml", "r")
data = yaml.load(infile)

BUIDER = data["builder"]
FACTORY = data["factory"]
GIT = data["git"]
MAIL_LIST = data["mail_list"]
MASTER_HOST = data["master_host"][0]
PROJECT_NAME = data["project_name"][0]
RELATION = data["relation"]
