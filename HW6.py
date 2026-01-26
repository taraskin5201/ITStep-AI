# Завдання 1
#
# Добавте в створену базу даних файл
# data/lesson_rag/huge_file.txt про умови користування гуглом
# Оскільки файл надто великий, то його треба добавляти
# частинами. Для цього:
#  прочитайте вміст файлу
#  розділіть його на окремі блоки(між блоками два
# порожніх рядка, дивись файл)
#  отримайте перший рядок кожного блоку – це його
# назва
#  створіть документи для кожного блоку. В метаданих:
# o назва файлу
# o назва блоку
#  створіть ID та добавте все в існуючу базу даних
#  добавте ID у json файл
#  перевірте агента

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document

import os
import json
import dotenv
from uuid import uuid4


dotenv.load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")


embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=gemini_api_key
)


pc = Pinecone(api_key=pinecone_api_key)
index = pc.Index("practice1")

vector_store = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

with open('data/lesson_rag/huge_file.txt', 'r', encoding='utf-8') as f:
    huge_text = f.read()


blocks = huge_text.split('\n\n\n')


docs = []

for block in blocks:
    block = block.strip()
    if not block:
        continue

    lines = block.split('\n')
    block_title = lines[0]   # перший рядок — назва блоку

    doc = Document(
        page_content=block,
        metadata={
            "path": "data/lesson_rag/huge_file.txt",
            "block_title": block_title
        }
    )

    docs.append(doc)


ids = [str(uuid4()) for _ in range(len(docs))]


with open('ids.json', 'r') as f:
    id_map = json.load(f)

for doc, id_ in zip(docs, ids):
    key = f'{doc.metadata["path"]}::{doc.metadata["block_title"]}'
    id_map[key] = id_

with open('ids.json', 'w') as f:
    json.dump(id_map, f, indent=2)


vector_store.add_documents(
    documents=docs,
    ids=ids
)

query = "Які умови користування сервісами Google?"
results = vector_store.similarity_search(query, k=3)

for res in results:
    print("BLOCK:", res.metadata.get("block_title", "NO BLOCK TITLE"))
    print("FILE:", res.metadata.get("path"))
    print(res.page_content[:300])
    print("-" * 60)


# Повне очищення індексу Pinecone, без видалення самого індексу
# =========================

# from pinecone import Pinecone
# import os
# import dotenv
#
# dotenv.load_dotenv()
# pinecone_api_key = os.getenv("PINECONE_API_KEY")
#
# pc = Pinecone(api_key=pinecone_api_key)
# index = pc.Index("practice1")
#
# # повне очищення індексу
# index.delete(delete_all=True)
#
# print("Index practice1 is fully cleaned")
