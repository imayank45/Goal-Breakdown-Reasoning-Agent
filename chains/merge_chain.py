from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

def merge_chain(x):
    merged = (
        f"--- Goal Breakdown ---\n{x['breakdown']}\n\n"
        f"--- Summary ---\n{x['summary']}\n\n"
        f"--- Plan ---\n{x['plan']}\n"
    )
    
    return {**x, "merged": merged}

merge_chain = RunnableLambda(merge_chain)