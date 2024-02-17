import streamlit as st
import numpy as np
from src.CardVista.pipeline.prediction import PredictionPipeline
import pandas as pd
from sklearn.decomposition import PCA
import plotly.express as px


st.set_page_config(
    page_title="CardVista",
    page_icon=":credit_card:",
    layout="centered",
    initial_sidebar_state="collapsed"
)


st.title("Customer's Cluster Predictor")
st.markdown("Enter the user's details, and our model will predict which cluster the user belongs to.")

# Create a form using Streamlit
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

    # Create an instance of the PredictionPipeline
    obj = PredictionPipeline()
    # Make a prediction based on user input
    cluster = obj.predict(data)

    st.markdown(f"Based on above details, customer belong to Cluster  =  {cluster[0]}")

    # Load data for 3D cluster visualization
    df = pd.read_csv('artifacts\data_transformation_and_clustering\data.csv')
    scaled_data = pd.read_csv('artifacts\data_transformation_and_clustering\scaled_data.csv')

    # Apply PCA for dimensionality reduction
    pca_scaled_std = PCA(n_components=3, random_state=42)
    pca_scaled_data = pca_scaled_std.fit_transform(scaled_data)

    # Create a 3D scatter plot using Plotly Express
    fig = px.scatter_3d(
    x=pca_scaled_data[:, 0],
    y=pca_scaled_data[:, 1],
    z=pca_scaled_data[:, 2],
    color_continuous_scale='Viridis',
    title='3D Cluster Visualization',
    labels={
        'x': 'Principal Component 1',
        'y': 'Principal Component 2',
        'z': 'Principal Component 3',
        'color': 'Cluster'
    },color=df['CLUSTER']
    )
    st.plotly_chart(fig)

    # Display statistical description of the selected cluster
    st.markdown("Statistical description of this particular cluster ")

    df=df[df['CLUSTER']==cluster[0]]
    statistics = df.apply(lambda x: pd.Series({'mean': x.mean(), 'median': x.median(), 'std': x.std(), 'min': x.min(), '25%': np.quantile(x, q=0.25), '75%': np.quantile(x, q=0.75), 'max': x.max()}))
    st.dataframe(statistics.transpose())

  


  
