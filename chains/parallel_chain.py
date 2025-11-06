from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from .prompts import summary_prompt, plan_prompt

llm = ChatOpenAI(
    model_name='gpt-4o-mini',
    temperature=0.7
)

parallel_chain = RunnableParallel({
    "summary": summary_prompt | llm | StrOutputParser(),
    "plan": plan_prompt | llm | StrOutputParser()
}
)

