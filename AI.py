import google.generativeai as genai
import streamlit as st

# Configure API Key
API_KEY = "AIzaSyAiAip-3_8v368OEvGdFzBeeW12M-X60Ik" # Replace with your actual key
genai.configure(api_key=API_KEY)

# Initialize the Model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

st.title("🩺 OsmoDoc - Testing Model -MOHIT ")
user_input = st.text_input("Ask Medibot a medical question:")

# Define a function to check if the query is medical-related
def is_medical_query(query):
    keywords = ["medicine", "symptoms", "disease", "doctor", "health", "treatment",
                "pain", "fever", "injury", "infection", "surgery", "cure", "diagnosis","Suffering"]
    
    return any(word in query.lower() for word in keywords)

if st.button("Ask"):
    if user_input:
        if is_medical_query(user_input):  # ✅ Check if it's a medical query
            response = chat.send_message(user_input, stream=True)
            response.resolve()
            st.write("🤖 Medibot:", response.text)
        else:
            st.write("🤖 Medibot: Sorry sir, I can't answer anything else. I am a Medibot.")
