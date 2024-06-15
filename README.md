# Multi-LLM-chatbot

![image](https://github.com/GayaaniD/Multi-LLM-chatbot/assets/125920863/16bc1206-4b37-488f-9e72-1cf0d2f77eae)

## Project Overview
This project demonstrates how to create a chatbot that can interact with users through a text interface. Users can pose questions, and the chatbot will respond using the capabilities of either the OpenAI LLM or the Ollama-based open-source LLM (Llama2 in this example).

## Key Components
- Langchain: An open-source framework that simplifies LLM integration and streamlines chatbot development.

  - Langchain Core: Provides foundational components for building LLM pipelines.
  - Langchain OpenAI: Facilitates access and interaction with OpenAI’s LLM API.
  - Langchain Community: Offers integrations with various third-party tools and open-source LLMs.

- Streamlit: A Python library for building user interfaces for data apps.

- Ollama: An open-source runtime environment for running LLMs locally on your machine.

- OpenAI API: Provides access to a commercially available LLM with high performance.

- Llama2: A powerful open-source LLM available through Ollama.

## Project Flow
1. Chatbot with OpenAI LLM:

    - Define a prompt template that establishes the conversation flow between the system and the user.
    - Utilize ChatOpenAI from langchain_openai to interact with the OpenAI LLM API.
    - Employ StrOutputParser from langchain_core to handle the LLM response as a string.
    - Build a Langchain pipeline by chaining the prompt template, ChatOpenAI instance, and output parser.
    - Integrate Streamlit to create a user interface where users can input questions. Upon receiving user input, trigger the Langchain pipeline to generate a response using the OpenAI LLM.

2. Chatbot with Ollama LLM:

    - Download the desired open-source LLM (Llama2 in this example) using Ollama’s command-line interface.
    - Use Ollama from langchain_community to interact with the locally running LLM.
    - Create a separate Langchain pipeline using the prompt template, Ollama instance with the Llama2 model, and output parser.
    - Integrate Streamlit to create a user interface where users can input questions. Upon receiving user input, trigger the Langchain pipeline to generate a response using the OpenAI LLM.

Within the Streamlit app, allow users to select between the OpenAI and Ollama-based chatbot options.

## How to Run the Project
1. Clone the GitHub repository.
2. Rename the `.env.example` file to `.env` and add your API keys.
3. Install the project dependencies by running the `requirements.txt` file. You can do this by opening your terminal and typing:
    ```
    pip install -r requirements.txt
    ```
4. After the dependencies are installed, you can run the project by using:
   ```
   streamlit run multillm_bot.py
   ```
   
## Outcome
![image](https://github.com/GayaaniD/Multi-LLM-chatbot/assets/125920863/26c96249-e404-4151-83b2-f65bb024489d)

## Benefits & Consideration
- Flexibility: The ability to switch between paid and open-source LLMs offers cost-effectiveness and access to cutting-edge models.
- Cost: Utilizing OpenAI’s LLM API incurs costs based on the token size of each request. For frequent chatbot interactions, these costs can accumulate.
- Performance: OpenAI provides high-performance LLMs, while Ollama offers a free, open-source alternative with potentially higher latency.
- Monitoring: Langchain facilitates tracking LLM interactions through its Langsmith dashboard. Project will be created with the specific name <LANGCHAIN_PROJECT > inside langsmith as we mentioned in the .env file.
