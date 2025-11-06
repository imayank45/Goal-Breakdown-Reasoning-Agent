from langchain_core.runnables import RunnableSequence, RunnableLambda
from .sequential_chain import sequential_chain
from .parallel_chain import parallel_chain
from .merge_chain import merge_chain


# full resoning pipeline that carries state forward
reasoning_flow = RunnableSequence(
    # start from goal
    RunnableLambda(lambda x: {
        "goal": x["goal"],
        "breakdown": sequential_chain.invoke({"goal": x["goal"]})
    }),
    
    # generate summary and plan in parallel
    RunnableLambda(lambda x: {
        **x,
        **parallel_chain.invoke({"breakdown": x["breakdown"], "summary": x.get("summary", "")})
    }),
    
    # merge all into single reasoning text
    merge_chain,
    
    # final structured output
    RunnableLambda(lambda x: f"""
─────────────────────────────
🧠 GOAL-BREAKDOWN AGENT OUTPUT
─────────────────────────────

🎯 Goal:
{x['goal']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🪜 Breakdown:
{x['breakdown']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧩 Summary:
{x['summary']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 Plan:
{x['plan']}
"""

    ))