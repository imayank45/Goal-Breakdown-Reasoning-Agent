from langchain.prompts import PromptTemplate

goal_prompt = PromptTemplate(
    template="Breakdown the following goal into clear subgoals with reasoning:\n:{goal}"
)
