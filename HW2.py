# Завдання 1
# Напишіть промпт для створення плану навчального
# курсу з певної теми для цільової айдиторії(початківці,
# професіонали, діти, тощо).
# Вхідні параметри: тема, опис цільової аудиторії
# Реалізуйте двома способами:
#  Zero-shot
#  Few-shot


import os
import dotenv

from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate

dotenv.load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

llm = GoogleGenerativeAI(
    model="gemma-3-1b-it",
    api_key=api_key,
    temperature=0.3
)

zero_shot_prompt = PromptTemplate.from_template("""
Ти — чат-бот, який допомагає створювати навчальні курси.
Спілкуйся ввічливо та зрозуміло.

Твоя задача — створити план навчального курсу на основі
введених даних користувача.

### ВХІДНІ ДАНІ
ТЕМА: {topic}
АУДИТОРІЯ: {audience}

### ІНСТРУКЦІЇ
1. Створи план курсу з модулів
2. Додай короткий опис до кожного модуля
3. Пояснюй відповідь так, ніби це відповідь у чаті

### ВІДПОВІДЬ БОТА
""")

zero_shot_chain = zero_shot_prompt | llm


few_shot_prompt = PromptTemplate.from_template("""
Ти — чат-бот, який допомагає створювати навчальні курси.
Спілкуйся ввічливо та зрозуміло.

### ПРИКЛАД ДІАЛОГУ

КОРИСТУВАЧ:
Хочу курс з Python для початківців

БОТ:
Ось приклад плану курсу:
1. Вступ до програмування
   - Що таке Python та де він використовується
2. Основи синтаксису
   - Змінні, типи даних
3. Умовні оператори та цикли
   - if, for, while
4. Функції
   - Створення та використання функцій

### ПОТОЧНИЙ ЗАПИТ

ТЕМА: {topic}
АУДИТОРІЯ: {audience}

### ІНСТРУКЦІЇ
1. Створи план курсу
2. Дотримуйся стилю наведеного прикладу
3. Відповідай як у чаті з користувачем

### ВІДПОВІДЬ БОТА
""")

few_shot_chain = few_shot_prompt | llm


print("🤖 Навчальний чат-бот")
print("Введіть 'exit' для виходу\n")

mode = input("Оберіть режим (1 - Zero-shot, 2 - Few-shot): ")

while True:
    topic = input("\nВведіть тему курсу: ")
    if topic.lower() == "exit":
        break

    audience = input("Опишіть цільову аудиторію: ")
    if audience.lower() == "exit":
        break

    if mode == "1":
        response = zero_shot_chain.invoke(
            {
                "topic": topic,
                "audience": audience
            }
        )
    else:
        response = few_shot_chain.invoke(
            {
                "topic": topic,
                "audience": audience
            }
        )

    print("\n АІ:")
    print(response)

print("\n👋 До побачення!")
