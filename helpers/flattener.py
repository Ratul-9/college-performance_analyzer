import sys, os
import pandas as pd
import numpy as np
import json
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from helpers.data_loader import load_json,save_csv

logging.basicConfig(
    filename='logs/flattening.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def flatten_data():
    json_data = load_json()
    data = pd.json_normalize(json_data)
    save_csv(data)
    logging.info("Data flattened and saved successfully")

if __name__ == "__main__":
    flatten_data()