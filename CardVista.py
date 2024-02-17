import streamlit as st

st.set_page_config(
    page_title="CardVista",
    page_icon=":credit_card:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add title and header
st.header("💳 CardVista: Unlocking Customer Insights with Data 📊", divider='rainbow')
st.subheader("Welcome to CardVista, a data-driven solution for Goyani Bank")

# Problem Statement
st.subheader("The Challenge", divider='gray')
st.write("""
Goyani Bank, a leading financial institution, faced the challenge of providing personalized services and targeted marketing campaigns to its diverse customer base. With a vast portfolio of credit card customers, it became difficult to understand their varying preferences and behavior patterns. This problem hindered the bank's ability to enhance customer satisfaction, retention, and ultimately, drive growth.
""")

# Project Story
st.subheader("The Project Story",divider='violet')
st.write("""
- As a data scientist at Goyani Bank, I was assigned the task of analyzing the bank's customer credit card data, including transactional information, credit limits, payment histories, and other relevant details. The primary objective was to identify distinct customer segments.

- To accomplish this, I used unsupervised machine learning  to group customers with similar characteristics. This provided valuable insights into the different customer personas and their financial behaviors.

- Once the customer segments were identified, the next step was to train a predictive model on this clustered data. The goal was to develop a robust model that could accurately classify new customers into the appropriate segments. This would enable the bank to proactively tailor their product offerings, marketing strategies, and customer service initiatives to meet the specific needs and preferences of each customer segment.

""")

# Approach
st.subheader("My Approach",divider='gray')
st.write("""
1. **Data Exploration and Preprocessing**: I began by conducting an in-depth exploration of the customer credit card data to gain insights into its structure, quality, and potential issues. This step involved data cleaning, handling missing values, and performing necessary transformations to prepare the data for subsequent analysis.

2. **Unsupervised Learning for Customer Segmentation**: I used unsupervised machine learning techniques,  to group customers based on relevant features. This allowed me to identify distinct customer segments with similar characteristics and behaviors.

3. **Predictive Modeling**: Once the customer segments were identified, I trained a predictive model on the clustered data. This model was designed to accurately classify new customers into the appropriate segments, enabling the bank to tailor its offerings and strategies accordingly.

4. **Model Evaluation and Optimization**: I evaluated the performance of the predictive model. I optimized the model through techniques such as feature engineering, hyperparameter tuning, or ensemble methods to improve its accuracy and robustness.

5. **Deployment and Feedback**: Goyani Bank and others will use this projecti according to their feedback i will improve it.
""")

# Additional Content
st.subheader("Why Customer Segmentation Matters",divider='violet')
st.write("""
Customer segmentation is a crucial strategy for businesses to understand their customer base better and tailor their offerings accordingly. By grouping customers with similar characteristics, behaviors, and preferences, companies can:

- **Personalize Marketing Campaigns**: Targeted marketing campaigns can be developed for each customer segment, increasing the likelihood of engagement and conversion.

- **Improve Customer Experience**: By understanding the unique needs and preferences of each segment, businesses can enhance customer experience by providing tailored products, services, and support.

- **Optimize Resource Allocation**: Segmentation helps businesses allocate resources effectively by focusing on the most profitable or promising customer segments.

- **Identify Growth Opportunities**: Analyzing customer segments can reveal untapped market opportunities and guide product development or expansion strategies.

- **Mitigate Risks**: Understanding customer behavior and risk profiles can help businesses make informed decisions regarding credit limits, interest rates, and other credit-related policies, reducing potential financial risks.
""")

# Footer
st.write("---")
st.write("Developed by Krish Goyani 🙋‍♂️")

# LinkedIn
st.markdown("[LinkedIn](https://www.linkedin.com/in/krish-goyani-433969268/)")

# Twitter
st.markdown("[Twitter](https://twitter.com/KrishGoyanii)")

# GitHub
st.markdown("[GitHub](https://github.com/Krish-Goyani)")