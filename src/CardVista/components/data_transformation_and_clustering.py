from src.CardVista.logging import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.metrics import davies_bouldin_score, silhouette_score, calinski_harabasz_score
from src.CardVista.utils.common import read_yaml, save_json
from src.CardVista.entity.config_entity import DataTransformationandClusteringConfig
import os
from pathlib import Path
from src.CardVista.constants import *

class ReplaceOutliers(BaseEstimator, TransformerMixin):

    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self 
    
    

    def transform(self, X):
        schema_filepath = SCHEMA_FILE_PATH
        schema = read_yaml(schema_filepath)
        df = pd.DataFrame(X, columns=schema.COLUMNS)
        
        for col in list(df.columns):
            q1 = df[col].quantile(0.15)
            q3 = df[col].quantile(0.85)
            iqr = q3 - q1
            
            upper_limit = q3 + 1.5 * iqr
            lower_limit = q1 - 1.5 * iqr
            
            df.loc[df[col] > upper_limit, col] = upper_limit
            df.loc[df[col] < lower_limit, col] = lower_limit
            
        return df.to_numpy()

class DataTransformationandClustering:
    def __init__(self, config: DataTransformationandClusteringConfig):
        self.config = config
        
    def eval_metrics(self,data,labels):
        silhouette = silhouette_score(data, labels)
        calinski_harabasz = calinski_harabasz_score(data, labels)
        davies_bouldin = davies_bouldin_score(data, labels)

        return silhouette,calinski_harabasz ,davies_bouldin



    def data_transformation_and_clustering(self):

        logger.info("data transformation started")

        data = pd.read_csv(self.config.data_path)

        data.drop('CUST_ID',axis=1,inplace=True)
        temp = data.copy()

        replace_outliers = ReplaceOutliers()

        trf1 = SimpleImputer(strategy='median')
        trf2 = replace_outliers
        trf3 = StandardScaler()
        trf4 = KMeans(n_clusters=3,random_state = 42,n_init = "auto")

        pipe = Pipeline([('trf1',trf1),
                 ('trf2',trf2),
                 ('trf3',trf3),
                 ('trf4',trf4)
                ])
        
        logger.info("data fitted in pipeline")

        pipe.fit(data)


        partial_pipe = Pipeline([('trf1', trf1), 
                         ('trf2',trf2),
                         ('trf3', trf3)])
        
        logger.info("data transformed in partial pipeline")

        scaled_data = partial_pipe.transform(temp)

        labels = pipe.fit_predict(data)
        
        logger.info("clusters generated")

        (silhouette,calinski_harabasz,davies_bouldin) = self.eval_metrics(scaled_data,labels)

        scores = {"silhouette_score" : silhouette,"calinski_harabasz_score" : calinski_harabasz,"davies_bouldin_score" : davies_bouldin}
        save_json(path=Path(self.config.metrics_file_name),data=scores)

        logger.info("KMeans evalution metrics saved")
    
        data['CLUSTER'] = labels+1

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)
        data.to_csv(os.path.join(self.config.root_dir, "data.csv"),index=False)
        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
        

        