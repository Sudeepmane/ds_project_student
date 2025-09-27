# src/components/data_ingestion.py
import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

from src.logger import logger
from src.exception import CustomException

class DataIngestion:
    def __init__(self):
        self.dataset_path = os.path.join("notebook", "data", "stud.csv")
        self.artifact_folder = os.path.join("artifacts")
        self.train_data_path = os.path.join(self.artifact_folder, "train.csv")
        self.test_data_path = os.path.join(self.artifact_folder, "test.csv")
        os.makedirs(self.artifact_folder, exist_ok=True)

    def initiate_data_ingestion(self):
        logger.info("Starting data ingestion...")
        try:
            df = pd.read_csv(self.dataset_path)
            logger.info(f"Dataset loaded from {self.dataset_path}, shape: {df.shape}")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.train_data_path, index=False)
            test_set.to_csv(self.test_data_path, index=False)
            logger.info("Train/test data saved successfully")
            return self.train_data_path, self.test_data_path
        except Exception as e:
            logger.error("Data ingestion error")
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()
    print("Data ingestion completed!")
    print("Train Path:", train_path)
    print("Test Path:", test_path)


             
         

