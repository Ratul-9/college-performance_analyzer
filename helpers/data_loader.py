import pandas as pd
import json
import yaml

def load_config(config_path="config/config.yaml"):
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def load_json():
    config = load_config()
    json_path = config["raw_json_path"]
    with open(json_path, "r") as file:
        data = json.load(file)
    return data

def load_csv(csv_path):
    return pd.read_csv(csv_path)

def save_csv(data):
    config = load_config()
    save_path = config["flattened_csv_path"]
    data.to_csv(save_path, index=False)

def save_json(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"✅ Saved JSON to {path}")