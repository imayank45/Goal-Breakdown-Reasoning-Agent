from langchain.prompts import PromptTemplate

# initial goal breakdown prompt
goal_prompt = PromptTemplate(
    template=(
        "You are a reasoning assistant.\n"
        "Break the following goal into smaller, logically ordered sub-goals with reasoning:\n\n"
        "Goal: {goal}\n\n"
        "Return a structured, numbered list of sub-goals."
    ),
    input_variables=["goal"]
)

# summary prompt depends on goal prompt
summary_prompt = PromptTemplate(
    template=(
        "Summarize the essence of the following breakdown into one concise paragraph: \n\n"
        "Breakdown:\n{breakdown}"
    ),
    input_variables=["breakdown"]
)

# plannning prompt that uses both summary and breakdown
plan_prompt = PromptTemplate(
    template=(
        "Using  the breakdown and summary below, design a clear step-by-step plan.\n"
        "Include reasoning for each step.\n\n"
        "Breakdown:\n{breakdown}\n\n"
        "Summary:\n{summary}"
    ),
    input_variables=["breakdown", "summary"]
)