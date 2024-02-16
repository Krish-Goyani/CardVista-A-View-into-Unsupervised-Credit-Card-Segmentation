
import pandas as pd
from sklearn.metrics import f1_score
from src.CardVista.utils.common import save_json
import joblib
from src.CardVista.entity.config_entity import ModelEvaluationConfig
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual, pred):
        f1 = f1_score(y_true=actual,y_pred=pred,average='micro')
        return f1

    
    def save_results(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        predicted_qualities = model.predict(test_x)

        f1 = self.eval_metrics(test_y, predicted_qualities)
        
        # Saving metrics as local
        scores = {"F1 score for our CatBoostClassifier" : f1}
        save_json(path=Path(self.config.metric_file_name), data=scores)


    