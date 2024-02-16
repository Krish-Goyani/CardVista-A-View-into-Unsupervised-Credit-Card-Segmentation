import pandas as pd
import os
import catboost
import joblib
from src.CardVista.entity.config_entity import ModelTrainerConfig



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]


        cbc = catboost.CatBoostClassifier(loss_function=self.config.loss_function, verbose=self.config.verbose, random_state=42)
        cbc.fit(train_x, train_y)

        joblib.dump(cbc, os.path.join(self.config.root_dir, self.config.model_name))

