
import pandas as pd
import logging
import os 
from config_loader import Base_path


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

log = logging.getLogger(__name__)


base_path = Base_path


def extract_multi_files(base_path):
    dataframes ={}
    try:
        files = os.listdir(base_path)
        log.info(f"found {len(files)} files")

        for file in files:
            if file.endswith(".csv"):
                file_path = os.path.join(base_path, file)
                
                try:
                    df = pd.read_csv(file_path, sep=",")                                        #df = pd.read_csv(file_path, sep=None, engine="python")
                    dataframes[file] = df
                    log.info(f"loaded {file} successfully")
                except Exception as e:
                    log.error(f"error loading {file}: {e}")

    except Exception as e:
        log.critical(f"Folder access failed: {e}")

    return dataframes


