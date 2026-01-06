# Завдання 1
# Напишіть чат модель яка підсумовує всю розмову в
# декілька речень. Вкажіть щоб модель зберігала якомога
# більше деталей.
# Використайте цю модель для простого чат бота який
# замість trim_massages використовує модель з підсумуванням.
# Підсумовуйте повідомлення, коли їх більше 4.
# Старі повідомлення треба видалити
# НЕ ВИДАЛЯТИ SystemMessage та не використовувати
# його для підсумування

import os
import dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
    BaseMessage
)


dotenv.load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

chat_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    api_key=api_key,
)

summary_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    api_key=api_key,
)


def summarize_messages(messages: list[BaseMessage]) -> AIMessage:
    """
    Підсумовує список HumanMessage та AIMessage.
    SystemMessage сюди НЕ передається.
    """

    summary_prompt = [
        SystemMessage(
            """
            Ти — модель для підсумування діалогу.
            Підсумуй розмову в декілька речень,
            зберігаючи якомога більше важливих деталей,
            фактів, імен та запитів користувача.
            """
        )
    ]

    summary_prompt.extend(messages)

    summary = summary_llm.invoke(summary_prompt)

    return AIMessage(
        content=f"📝 Підсумок попередньої розмови:\n{summary.content}"
    )


messages = [
    SystemMessage(
        """
        Ти — ввічливий чат бот, який імітує Людину павука.
        Давай короткі та влучні відповіді.
        """
    )
]

MAX_MESSAGES = 4

while True:
    user_query = input("Ви: ")

    if user_query == "":
        break

    messages.append(HumanMessage(user_query))

    non_system_messages = [
        m for m in messages if not isinstance(m, SystemMessage)
    ]

    if len(non_system_messages) > MAX_MESSAGES:
        summary = summarize_messages(non_system_messages[:-2])

        messages = [
            messages[0],
            summary,
            *non_system_messages[-2:]
        ]

    response = chat_llm.invoke(messages)
    messages.append(response)

    print(f"AI: {response.content}")

    print("\n#### ІСТОРІЯ ####")
    for msg in messages:
        print(repr(msg))
    print()
