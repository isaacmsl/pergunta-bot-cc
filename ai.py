import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

os.environ['OPENAI_API_KEY'] = 'YOUR_OPEN_AI_KEY'

def answer_query(query):
    # carrega indexador FAISS pré-processado com embeddings OpenAI
    faiss_index = FAISS.load_local("faiss_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    retriever = faiss_index.as_retriever()

    llm = ChatOpenAI(temperature = 0.0, model="gpt-3.5-turbo")

    qa_stuff = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", 
        retriever=retriever,
        verbose=False
    )

    return qa_stuff.run(query)