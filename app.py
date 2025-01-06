import streamlit as st
import pickle
import time

# Add an image at the top
st.image("Twitter.jpg", width=620)

st.title("Twitter Sentiment Analysis")

# Load the pre-trained model
model = pickle.load(open('twitter_sentiment.pkl', 'rb'))

# Get the tweet input from the user
tweet = st.text_input("Enter Your Tweet here")

# Button to trigger prediction
if st.button("Predict"):
    if tweet:
        start_time = time.time()  # Start time
        prediction = model.predict([tweet])  # Prediction
        end_time = time.time()  # End time
        execution_time = end_time - start_time  # Execution time

        # Display results and execution time
        st.write(f"Sentiment: {prediction[0]}")
        st.write(f"Execution Time: {execution_time:.4f} seconds")
    else:
        st.write("Please enter a tweet.")

# Adding your details at the bottom
st.markdown("""
            
# About Us
We, Zeeshan and Darab, have developed this project. We are currently in the 7th semester of Computer Science Engineering (CSE).

- **Our Recent Project is on**: Twitter Sentiment Analysis project using Random Forest.
- **Contact**: [zeeshanahmed0393@gmail.com](mailto:zeeshanahmed0393@gmail.com)
- **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/zeeshanahmed0393/)
""")
