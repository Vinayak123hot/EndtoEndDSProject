import os
import yaml
from src.datascience import logger
import json
import joblib
from box import ConfigBox
from pathlib import Path
from typing import Any

import yaml
from typing import Any
from ensure import ensure_annotations
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents.

    Args:
        path_to_yaml: Path: Path to the YAML file.

    Returns:
        ConfigBox: The contents of the YAML file, typically a dictionary or list.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)  
            logger.info(f"yaml file : {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        return content
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


#create directories

@ensure_annotations
def create_directories(path_o_directories: list, verbose=True):
    
    
    for path in path_o_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"create directory at: {path}")
            
            
@ensure_annotations
def save_json(path: Path, data: dict):
    
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"json file saved at : {path}")
    
    
@ensure_annotations
def load_json(path: Path):
    with open(path) as f:
        content=json.load(f)
        
    logger.info(f"json file loaded successfully from : {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at : {path}")
    
    
@ensure_annotations
def load_bin(path: Path) ->Any:
    data=joblib.load(path)
    logger.info(f"Binary file loaded from : {path}")
    return data


