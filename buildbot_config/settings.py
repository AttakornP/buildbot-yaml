import os
import yaml

config_all = {}  
config_file = os.listdir("buildbot_config/config/")
for config in config_file:
    infile = open("buildbot_config/config/" + config, "r")
    config_data = yaml.load(infile)

    for key in config_data:
        if not config_all.has_key(key):
            config_all.setdefault(key)
            config_all[key] = config_data[key]
        if type(config_data[key]) == list:
            if config_all[key] != config_data[key]:
                config_all[key].extend(config_data[key])
        else:
            if config_all[key] != config_data[key]:
                config_all[key].update(config_data[key])

outfile = open("buildbot_config/config.yml", "w")
yaml.dump(config_all, outfile)
outfile.close()

infile = open("buildbot_config/config.yml", "r")
data = yaml.load(infile)

BUIDER = data["builder"]
FACTORY = data["factory"]
GIT = data["git"]
MAIL_LIST = data["mail_list"]
MASTER_HOST = data["master_host"][0]
PROJECT_NAME = data["project_name"][0]
RELATION = data["relation"]
