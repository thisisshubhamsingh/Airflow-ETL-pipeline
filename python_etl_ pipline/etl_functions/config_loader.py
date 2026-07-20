import yaml

def load_config(path = "config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)
    
#load once
config = load_config()

Base_path  = config["paths"]["base_path"]


#print(base_path)