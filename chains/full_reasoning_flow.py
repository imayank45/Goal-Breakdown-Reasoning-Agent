from langchain_core.runnables import RunnableSequence, RunnableLambda
from .sequential_chain import sequential_chain


# full resoning pipeline that carries state forward
reasoning_flow = RunnableSequence(
    # start from goal
    RunnableLambda(lambda x: {
        "goal": x["goal"],
        "breakdown": sequential_chain.invoke({"goal": x["goal"]})
    }),
    
    # final structured output
    RunnableLambda(lambda x: (
        f"Goal: {x['goal']}\n\n"
        f"--- Breakdown ---\n"
        f"{x['breakdown']}"
    ))
)
