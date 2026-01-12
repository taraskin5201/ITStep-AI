# # пошук потрібного документа
# # RAG -- (пошук - відповідь - генерація)
#
# # документ1 -- Суп корисний при застуді
# # документ2 -- Суп придумали в Китаї
# # документ3 -- Бігати більше 10 км шкідливо для здоров'я
#
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from pinecone import Pinecone, ServerlessSpec
# from langchain_pinecone import PineconeVectorStore
# from langchain_core.documents import Document
#
# import os
# import dotenv
# from uuid import uuid4
#
#
# # завантаження апі ключа
# dotenv.load_dotenv()
# gemini_api_key = os.getenv("GEMINI_API_KEY")
# pinecone_api_key = os.getenv("PINECONE_API_KEY")
#
# # модель для кодування текстів(embedding model)
# embeddings = GoogleGenerativeAIEmbeddings(
#     model="models/text-embedding-004",
#     google_api_key=gemini_api_key
# )
#
# # # кодування текстів
# # # отримані числа називають вектор
# # vec1 = embeddings.embed_query("Суп корисний при застуді")
# #
# # print(vec1)
# # print(len(vec1))
# #
# # vec2 = embeddings.embed_query("При застуді корисно їсти суп")
# # print(vec2)
# #
# # vec3 = embeddings.embed_query("Бігати більше 10 км шкідливо для здоров'я")
# # print(vec3)
#
# # створення весторної бази даних
# pc = Pinecone(api_key=pinecone_api_key)
# index_name = "soup"  # назва бази даних
#
# if not pc.has_index(index_name):
#     pc.create_index(
#         name=index_name,
#         dimension=768,      # кількість чисел при кодування
#         metric="cosine",    # формула для схожості
#         spec=ServerlessSpec(
#             cloud="aws",         # хмарний сервер(амазон)
#             region="us-east-1"   # регіон(Каліфорнія)
#         ),
#     )
#
# index = pc.Index(index_name)
# vector_store = PineconeVectorStore(
#     index=index,
#     embedding=embeddings
# )
#
# # створення документів
#
# # документ1 -- Суп корисний при застуді
# doc1 = Document(
#     page_content="Суп корисний при застуді",   # вміст дукумента
#     metadata={               # додаткова інформація
#         "type": "здоров'я",
#         "author": "Anton Halysh"
#     }
# )
#
#
# # документ2 -- Суп придумали в Китаї
# doc2 = Document(
#     page_content="Суп придумали в Китаї",   # вміст дукумента
#     metadata={               # додаткова інформація
#         "type": "історія",
#         "author": "Anton Halysh",
#         "date": "2025 01 07"
#     }
# )
#
# # документ3 -- Бігати більше 10 км шкідливо для здоров'я
# doc3 = Document(
#     page_content="Бігати більше 10 км шкідливо для здоров'я",   # вміст дукумента
#     metadata={               # додаткова інформація
#         "type": "здоров'я",
#         "author": "Unknown"
#     }
# )
#
# # список документів
# docs = [doc1, doc2, doc3]
#
# # створення унікальних id для документів
# ids = [str(uuid4()) for _ in range(len(docs))]
#
# # print(ids)
#
# # # вантаження документів у базу даних
# # vector_store.add_documents(
# #     documents=docs,
# #     ids=ids
# # )
#
# # отримати схожі документи
#
# user_input = "Де придумали суп?"
#
# result_docs = vector_store.similarity_search(
#     user_input,   # текст для порівняння схожості
#     k=2,          # кількість документів у відповіді
# )
#
# for doc in result_docs:
#     print(doc)
#
# print()


from langchain_google_genai import GoogleGenerativeAIEmbeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document

import json
import os
import dotenv
from uuid import uuid4

# Завдання 1
# Створіть векторну базу даних, де кожен документ – це вміст файлу з папки data/lesson_rag/files
#  добавте в метадані шлях до файлу
#  створіть для кожного документу ID
#  збережіть створені ID та назви відповідних файлів в окремий json файл
# Перевірте чи працює правильно пошук

# завантаження апі ключа
dotenv.load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")

# модель для кодування текстів(embedding model)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=gemini_api_key
)

pc = Pinecone(api_key=pinecone_api_key)
index_name = "practice1"  # назва бази даних

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=768,      # кількість чисел при кодування
        metric="cosine",    # формула для схожості
        spec=ServerlessSpec(
            cloud="aws",         # хмарний сервер(амазон)
            region="us-east-1"   # регіон(Каліфорнія)
        ),
    )

index = pc.Index(index_name)
vector_store = PineconeVectorStore(
    index=index,
    embedding=embeddings
)


# документ1 -- future of ai
with open('data/lesson_rag/files/future_of_ai.txt','r', encoding='utf-8') as f:
    text_1 = f.read()

doc1 = Document(
    page_content=text_1, #вміст документа
    metadata={'path': 'data/lesson_rag/files/future_of_ai.txt'
    }
)

# документ2 -- intro
with open('data/lesson_rag/files/intro.txt','r', encoding='utf-8') as f:
    text_2 = f.read()

doc2 = Document(
    page_content=text_2,
    metadata={
        "path":"data/lesson_rag/files/intro.txt"
    }
)

# документ3 -- machine_learning
with open('data/lesson_rag/files/machine_learning.txt','r', encoding='utf-8') as f:
    text_3 = f.read()

doc3 = Document(
    page_content=text_3,
    metadata={
        "path":'data/lesson_rag/files/machine_learning.txt'
    }
)

#doc4 -- neural_networks
with open('data/lesson_rag/files/neural_networks.txt','r', encoding='utf-8') as f:
    text_4 = f.read()

doc4 = Document(
    page_content=text_4,
    metadata={
        "path":'data/lesson_rag/files/neural_networks.txt'
    }
)


# documents list
docs = [doc1, doc2, doc3, doc4]

#creating unique documents id
ids = [str(uuid4()) for _ in  range(len(docs))]

id_map = {

}

for doc,id  in  zip(docs, ids):
    id_map[doc.metadata["path"]] = id

print(id_map)

with open ('ids.json', 'w') as f:
    json.dump(id_map, f, indent=2)

# #завантаження документів у базу Данних
vector_store.add_documents(
    documents=docs,
    ids=ids
)