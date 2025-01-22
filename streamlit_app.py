
       import streamlit as st
import pandas as pd

# Function to get bot response
def get_bot_response(user_query, data):
    normalized_query = user_query.strip().lower()
    response = data[data['User Query'] == normalized_query]['Bot Response']
    
    if not response.empty:
        return response.values[0]
    else:
        return "I'm sorry, I don't have an answer for that."

# Streamlit app
def main():
    st.title("Gym Chatbot")

    # File uploader
    uploaded_file = st.file_uploader("Upload your dataset", type=["csv"])
    
    if uploaded_file is not None:
        # Load the dataset
        data = pd.read_csv(uploaded_file)
        
        # Clean the data (optional)
        data['User Query'] = data['User Query'].str.strip().str.lower()
        data['Bot Response'] = data['Bot Response'].str.strip()
        
        # User input
        user_input = st.text_input("Enter your query:")
        
        if user_input:
            bot_response = get_bot_response(user_input, data)
            st.write("Bot Response:", bot_response)
    else:
        st.write("Please upload a CSV file.")

if __name__ == "__main__":
    main()


