# TXT-GPT


TXT-GPT is a natural language processing (NLP) project. It uses OpenAI's GPT models to create a conversational AI agent named 'Cortana', that can interactively answer questions based on the contents of a text file.

# Description

This project works by loading text files into an index and then querying this index to find responses to user questions. The AI agent uses OpenAI's GPT models for text generation and response selection.

# Setup & Installation

# Prerequisites
Python
OpenAI's Python package
The Python packages used in this project are:


bash
Copy code
pip install <package-name>
Installing
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/atekle10/TXT-GPT.git
Then, navigate to the TXT-GPT directory:

bash
Copy code
cd TXT-GPT

# Usage

Load text files using TextLoader and create an index with VectorstoreIndexCreator.
Define a function that will query the created index.
Define a tool that uses the query function.
Create a conversational prompt using ConversationalAgent.create_prompt().
Initialize a ConversationBufferMemory for storing the conversation history.
Set up a LLMChain with OpenAI's chat model and the created prompt.
Initialize the conversational agent with the LLMChain, the created tool, and the conversation memory.
Start the agent and interact with it by inputting text.
Remember to replace 'insert OpenAI key' with your actual OpenAI API key.

Authors

Abel Tekle - Initial work - GitHub
