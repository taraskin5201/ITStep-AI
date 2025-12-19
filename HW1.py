import os
import dotenv
from langchain_google_genai import GoogleGenerativeAI

dotenv.load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


with open("data/lesson9/return_policy.txt", "r", encoding="utf-8") as f:
    return_policy = f.read()

llm = GoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    api_key=api_key,
    top_k=10,
    top_p=0.8,
    temperature=0.7
)

history = []

print("Чат-бот з питань повернення товару")
print("Для завершення натисніть Enter на порожньому рядку\n")

while True:
    user_input = input("Ви: ").strip()

    if user_input == "":
        print("Діалог завершено.")
        break

    history.append(f"Human: {user_input}")

    prompt = f"""
        Instruction:
        Ти — чат-бот служби підтримки магазину.
        Відповідай ТІЛЬКИ на основі наведеної політики повернення товару.
        Якщо інформації недостатньо — скажи, що цього немає в політиці.
        
        Політика повернення:
        {return_policy}
        
        Історія діалогу:
        """ + "\n".join(history) + "\nAI:"

    response = llm.invoke(prompt)

    print(f"AI: {response}\n")

    history.append(f"AI: {response}")
