import json

class Config():
    
    def get_param(node, key):
        config_file = open('config/params.json')
        config = json.load(config_file)
        return config[node][key]