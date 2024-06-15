from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
load_dotenv()

# Langchain tracking and API key environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt template defining conversation flow
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries"),
    ("user", "Question: {question}")
])

# Streamlit app title
st.title('Langchain Chatbot Demo')

# User input field
input_text = st.text_input("Search the topic you want")

def get_response(llm_choice):
    # Define output parser
    output_parser = StrOutputParser()

    # Choose LLM based on input
    if llm_choice == "OpenAI":
        # Access OpenAI LLM through Langchain OpenAI
        llm = ChatOpenAI(model="gpt-3.5-turbo")
    else:
        # Access Ollama-based LLM (Llama2 in this example)
        llm = Ollama(model="llama2")

    # Build Langchain pipeline
    chain = prompt | llm | output_parser

    # Generate response if user input exists
    if input_text:
        return chain.invoke({'question': input_text})
    else:
        return None

# Select LLM option (can be extended for more choices)
llm_options = ["OpenAI", "Ollama (Llama2)"]
selected_llm = st.selectbox("Choose LLM", llm_options)

# Generate response based on selection
response = get_response(selected_llm)

# Display response if available
if response:
    st.write(f"**Response from {selected_llm}:**")
    st.write(response)