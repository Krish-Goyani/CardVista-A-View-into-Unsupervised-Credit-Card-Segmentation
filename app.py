import streamlit as st
import numpy as np
from src.CardVista.pipeline.prediction import PredictionPipeline
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)
st.title("Prediction")
st.set_option('deprecation.showPyplotGlobalUse', False)

with st.form(key= "CardVista_form", clear_on_submit = True, border = True):

  BALANCE = st.number_input("Enter balance", placeholder="Outstanding amount owed", step=None)

  BALANCE_FREQUENCY = st.number_input("Enter balance frequency", placeholder="How often balance is updated", step=None)  

  PURCHASES = st.number_input("Enter total purchases", placeholder="Total amount spent on card", step=None)

  ONEOFF_PURCHASES = st.number_input("Enter highest single purchase", placeholder="Shows spending capacity", step=None)

  INSTALLMENTS_PURCHASES = st.number_input("Enter installment purchases", placeholder="Amount spent using credit financing", step=None)

  CASH_ADVANCE = st.number_input("Enter cash advances", placeholder="Cash withdrawn from credit line", step=None)

  PURCHASES_FREQUENCY = st.number_input("Enter purchase frequency", placeholder="How often purchases occur", step=None)

  ONEOFF_PURCHASES_FREQUENCY = st.number_input("Enter one-off purchase frequency", placeholder="Frequency of big ticket purchases", step=None)

  PURCHASES_INSTALLMENTS_FREQUENCY = st.number_input("Enter installment frequency", placeholder="Frequency of installment transactions", step=None)

  CASH_ADVANCE_FREQUENCY = st.number_input("Enter cash advance frequency", placeholder="Frequency of cash advance transactions", step=None)

  CASH_ADVANCE_TRX = st.number_input("Enter cash advance transactions",  placeholder="Number of cash advance transactions", step=None)

  PURCHASES_TRX = st.number_input("Enter total purchase transactions", placeholder="Total number of purchases", step=None)

  CREDIT_LIMIT = st.number_input("Enter credit limit", placeholder="Maximum credit amount available", step=None)

  PAYMENTS = st.number_input("Enter payments made", placeholder="Amount paid back against balance", step=None)

  MINIMUM_PAYMENTS = st.number_input("Enter minimum payments", placeholder="Minimum repayments made", step=None)

  PRC_FULL_PAYMENT = st.number_input("Enter percentage fully paid", placeholder="Percent of balance paid off", step=None)

  TENURE = st.number_input("Enter tenure", placeholder="How long account has been open", step=None)

  submitted = st.form_submit_button("Submit")

if submitted:
  
    data = [BALANCE, BALANCE_FREQUENCY, PURCHASES,
            ONEOFF_PURCHASES, INSTALLMENTS_PURCHASES, CASH_ADVANCE,
            PURCHASES_FREQUENCY, ONEOFF_PURCHASES_FREQUENCY,
            PURCHASES_INSTALLMENTS_FREQUENCY, CASH_ADVANCE_FREQUENCY,
            CASH_ADVANCE_TRX, PURCHASES_TRX, CREDIT_LIMIT, PAYMENTS,
            MINIMUM_PAYMENTS, PRC_FULL_PAYMENT, TENURE]

    data = np.asarray(data)

    obj = PredictionPipeline()

    cluster = obj.predict(data)

    st.markdown(f"Data Belongs to Cluster = {cluster[0]}")

    df=pd.read_csv('artifacts\data_transformation_and_clustering\data.csv')
  
    cluster_df=df[df['CLUSTER']==cluster[0]]

    plt.rcParams["figure.figsize"] = (20,3)

    for c in cluster_df.drop(['CLUSTER'],axis=1):
        fig, ax = plt.subplots()
        grid= sns.FacetGrid(cluster_df, col='CLUSTER')
        grid= grid.map(plt.hist, c)
        plt.show()
        st.pyplot()


