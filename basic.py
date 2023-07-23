import os
import sys



from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import openai
from langchain.chat_models import ChatOpenAI


os.environ['OPENAI_API_KEY'] = "insert OpenAI key"



loader1 = TextLoader('info.txt', 'utf-8')

index = VectorstoreIndexCreator().from_loaders([loader1])

query="what kind of product managers are there manager"

print(index.query(query, llm=ChatOpenAI()))
