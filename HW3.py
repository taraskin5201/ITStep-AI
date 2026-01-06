# Завдання 1
# Напишіть модель для генерації персонального плану
# тренувань з двох ланцюгів:
#  Перший ланцюг отримує мету тренування(схуднення,
# набір м’язів, тощо) та повертає список вправ
#  Другий ланцюг отримує список вправ, рівень
# підготовки
# користувача(низький,
# середній,
# професіонал) та кількість часу на тиждень(в годинах)
# і повертає план тренувань


import os
import dotenv
from typing import List
from pydantic import BaseModel, Field
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser


dotenv.load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

llm = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=api_key,
)


class ExerciseResponse(BaseModel):
    exercises: List[str] = Field(description="Список вправ відповідно до мети тренування")


parser1 = PydanticOutputParser(pydantic_object=ExerciseResponse)
instructions1 = parser1.get_format_instructions()

prompt1 = PromptTemplate.from_template(
    """
    Ти — фітнес-чатбот.
    Користувач назвав мету тренування.
    Твоя задача — підібрати список вправ.

    ### МЕТА ТРЕНУВАННЯ
    {goal}

    ### ФОРМАТ ВІДПОВІДІ
    {instructions}
    """,
    partial_variables={"instructions": instructions1}
)

chain_exercises = prompt1 | llm | parser1


class TrainingPlanResponse(BaseModel):
    plan: List[str] = Field(
        description="Тижневий план тренувань у форматі днів і навантаження"
    )


parser2 = PydanticOutputParser(pydantic_object=TrainingPlanResponse)
instructions2 = parser2.get_format_instructions()

prompt2 = PromptTemplate.from_template(
    """
    Ти — фітнес-чатбот.
    На основі вправ, рівня підготовки та доступного часу
    сформуй персональний план тренувань.

    ### ВПРАВИ
    {exercises}

    ### РІВЕНЬ ПІДГОТОВКИ
    {level}

    ### ГОДИН НА ТИЖДЕНЬ
    {hours}

    ### ФОРМАТ ВІДПОВІДІ
    {instructions}
    """,
    partial_variables={"instructions": instructions2}
)

chain_plan = prompt2 | llm | parser2


print("Вітаю! Я фітнес-чатбот.")
goal = input("👉 Яка ваша мета тренування? ")

exercise_response = chain_exercises.invoke({
    "goal": goal
})

print("\nЧудово! Ось вправи, які вам підійдуть:")
for ex in exercise_response.exercises:
    print(f"- {ex}")

level = input("\n👉 Який ваш рівень підготовки (низький / середній / професіонал)? ")
hours = input("👉 Скільки годин на тиждень ви готові тренуватися? ")

plan_response = chain_plan.invoke({
    "exercises": exercise_response.exercises,
    "level": level,
    "hours": hours
})

print("\nОсь ваш персональний план тренувань:")
for item in plan_response.plan:
    print(item)

print("\n💪 Успіхів у тренуваннях!")
