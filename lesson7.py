import streamlit as st


# st.title("ITStep")
#
# st.markdown("звичайний текст")
#
# st.markdown("**жирний текст**")
#
# user_query = st.chat_input("Введіть ваш запит:")
#
# # st.markdown(f"Ви ввели: {user_query}")
# #
# # if user_query == "Привіт":
# #     st.markdown("Привіт! Як я можу допомогти?")
#
#
# # if user_query == None:
# #     st.session_state["history"] = []
# #
# # st.session_state["history"].append(user_query)
# #
# # st.markdown(f"Ви ввели: {st.session_state['history']}")



# ЧАТ-БОТ

import os
import dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    trim_messages
)


st.title("ITStep ChatBot")

# завантаження апі ключа
dotenv.load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# створити llm
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    api_key=api_key,
)

# історія повідомлень
messages = [
    # перше повідомлення з основними інструкціями(промпт)
    SystemMessage(
        """
        Ти -- ввічливий чат бот, твоя зада давити короткі та
        чіткі відповіді на питання
        """
    ),
    HumanMessage("Привіт"),
    AIMessage("Привіт, щоб ти зотів дізнатись?"),
    HumanMessage("Порекомендуй цікавий фільм про космос")
]


# дати відповідь на очтаннє повідомлення
# враховуючи історію спілкування та основні інструкції

response = llm.invoke(messages)

print(type(response))
print(response)
print(repr(response))


простий чатбот

історія повідомлень
на початку лише інструкції
messages = [
    SystemMessage(
        """
        Ти -- ввічливий чат бот, який імітує Толкіна. Давай короткі відповіді
        на питання користувача
        """
    )
]

while True:
    user_query = input("Ви: ")

    # закіцнчуємо якщо натиснути Enter
    if user_query == '':
        break

    # переволимо повідомлення в HumanMessage
    human_message = HumanMessage(user_query)

    # добавляємо до історії повідомлень
    messages.append(human_message)

    # запускаємо модель
    response = llm.invoke(messages)

    # response -- AIMessage
    # добавляємо до історії повідомлень
    messages.append(response)

    # вивести відповідь
    print(f"AI: {response.content}")

    # вивести саму історії спілкування
    print()
    print("####ІСТОРІЯ####")

    for message in messages:
        print(repr(message))

    print()