import os
from openai import OpenAI
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent
import dotenv
import streamlit as st
api_key ="ENTER YOUR API KEY HERE"
os.environ["OPENAI_API_KEY"] = api_key

def main():

    st.set_page_config(page_title="Ask your CSV 📈")
    st.header("Ask your CSV 📈")
    user_csv = st.file_uploader("Upload your csv file", type="csv")

    if user_csv is not None:
        user_question = st.text_input('Please Ask Me A Question About Your CSV')

        llm = OpenAI(temperature=0.7)
        agent = create_csv_agent(llm, user_csv, verbose=True)

        if user_question is not None and user_question != "":
            response=agent.run(user_question)

            st.write(response)

if __name__ == "__main__":
    main()
