# Завдання 1
# Напишіть чат бота, з інструментом по рекомендації
# ресторанів.
# Для цього скористайтесь
# GoogleSerperAPIWrapper(type="places")
# Інструмент повинен отримувати запит для пошуку та
# повертати таку інформацію про ресторани:
#  назва
#  посилання на сайт(якщо є)
#  рейтинг


import os
import dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import GoogleSerperAPIWrapper
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import (
    HumanMessage,
    SystemMessage
)

dotenv.load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=gemini_api_key,
)


places_searcher = GoogleSerperAPIWrapper(
    serper_api_key=serper_api_key,
    type="places"
)

def recommend_restaurants(query: str) -> str:
    """
    Рекомендує ресторани на основі запиту користувача

    :param query: запит (наприклад "італійські ресторани у Львові")
    :return: список ресторанів з назвою, сайтом та рейтингом
    """
    results = places_searcher.results(query)

    restaurants = results.get("places", [])

    if not restaurants:
        return "Не вдалося знайти ресторани за цим запитом."

    answer = "**Рекомендовані ресторани:**\n\n"

    for r in restaurants[:5]:  # обмежимо до 5 результатів
        name = r.get("title", "Невідома назва")
        rating = r.get("rating", "Немає рейтингу")
        website = r.get("website", "Сайт відсутній")

        answer += (
            f"**Назва:** {name}\n"
            f"**Рейтинг:** {rating}\n"
            f"**Сайт:** {website}\n\n"
        )

    return answer


agent = create_react_agent(
    model=llm,
    tools=[recommend_restaurants]
)


messages = [
    SystemMessage(
        """
        Ти ввічливий чат-бот.
        Твоя задача — рекомендувати ресторани на основі запиту користувача.

        У тебе є інструмент:
        • recommend_restaurants — використовуй його для пошуку ресторанів
        """
    )
]


while True:
    user_query = input("Ви: ")

    if user_query == "":
        break

    messages.append(HumanMessage(user_query))

    input_data = {
        "messages": messages
    }

    response = agent.invoke(input_data)
    messages = response["messages"]

    answer = messages[-1]
    print(answer.content)

    print("\nІсторія повідомлень:")
    for msg in messages:
        print(repr(msg))
