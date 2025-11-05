from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from .prompts import goal_prompt

llm = ChatOpenAI(
    model_name='gpt-4o-mini',
    temperature=0.7
)

sequential_chain = RunnableSequence(
    goal_prompt | llm | StrOutputParser()
)