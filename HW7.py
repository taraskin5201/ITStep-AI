# Завдання 1
# Напишіть додаток з чат ботом по допомозі з вивченням
# англійської мови.
#  Якщо користувач просить перекласти слово або
# фразу, то вивести переклад та приклад використання
# у речені
#  Якщо користувач просить перекласти речення, то
# вивести переклад та пояснення граматики, наприклад
# структура there is/are, пасивна форма дієслова, тощо


import streamlit as st
import os
import dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
)

# заголовок
st.title("Chat Bot - Твій помічник з вивчення англійської мови")

# завантаження апі ключа за допомогою streamlit
api_key = st.secrets.get("GEMINI_API_KEY")

# створити llm
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    api_key=api_key,
)

user_query = st.chat_input("Ваше повідомлення")

# якщо це початок то створити історію в session state
if user_query is None:
    # історія повідомлень
    st.session_state['history'] = [
        # перше повідомлення з основними інструкціями(промпт)
        SystemMessage(
            """
            Ти -- ввічливий та розумний чат бот, який допомагає користувачу вивчати англійську мову.
            Якщо користувач просить перекласти слово або фразу, то виведи переклад та приклад 
            використання у реченні.
            Якщо користувач просить перекласти речення, то виведи переклад та пояснення граматики, 
            наприклад структура there is/are, пасивна форма дієслова, тощо.
            """
        )
    ]

# якщо повідомлення введено, то дати відповідь від моделі
if user_query:
    # переволимо повідомлення в HumanMessage
    human_message = HumanMessage(user_query)

    # добавляємо до історії повідомлень
    st.session_state['history'].append(human_message)

    # запускаємо модель
    response = llm.invoke(st.session_state['history'])

    # response -- AIMessage
    # добавляємо до історії повідомлень
    st.session_state['history'].append(response)


# вивести історію повідомлень
for msg in st.session_state['history']:
    if isinstance(msg, HumanMessage):
        st.markdown(f"Ви: {msg.content}")
    elif isinstance(msg, AIMessage):
        st.markdown(f"AI: {msg.content}")