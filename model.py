import os
import sys

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import openai
from langchain.memory import ConversationBufferMemory
from langchain import OpenAI, LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType, ZeroShotAgent, initialize_agent, Tool, AgentExecutor, ConversationalAgent




os.environ['OPENAI_API_KEY'] = "insert OpenAI key"



loader1 = TextLoader('info.txt', 'utf-8')
#loader2 = TextLoader('ll.txt', 'utf-8')
#loader3 = TextLoader('zz.txt','utf-8' )

index = VectorstoreIndexCreator().from_loaders([loader1])


# Define the function that will be run by the agent
def query_index(input):
    return index.query(input, llm=ChatOpenAI())

# Define the tool
tool = Tool(name="Index Query Tool", func=query_index, description="use to query info on product managers")

prefix = """You are an AI txt file reader named cortana, you can query txt files to answer any questions the user prompts you with:"""
suffix = """Begin! "


""{chat_history}
Question: {input}
{agent_scratchpad}"""

prompt = ConversationalAgent.create_prompt(
    [tool],
    prefix=prefix,
    suffix=suffix,
    input_variables=["input", "chat_history", "agent_scratchpad"],
)
memory = ConversationBufferMemory(memory_key="chat_history")   

llm_chain = LLMChain(llm=ChatOpenAI(temperature=0), prompt=prompt)
agent = ConversationalAgent(llm_chain=llm_chain, tools=[tool], verbose=True)

agent_chain = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=[tool],
    verbose=True,
    memory=memory,
)

while True:
    input_text = input("User: ")
    agent_output = agent_chain.run(input_text)
    print(f"Agent: {agent_output}")
    memory.save_context({"input": input_text}, {"output": agent_output})


