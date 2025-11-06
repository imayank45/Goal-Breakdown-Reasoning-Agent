from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

feedback_prompt = PromptTemplate(
    template=(
        "You are an assistant evaluating feedback.\n"
        "Customer review: {review}\n\n"
        "Based on this review, respond with constructive feedback or next steps "
        "related to the plan below.\n\nPlan:\n{plan}"
    ),
    input_variables=["review", "plan"]
)

feedback_chain = (
    feedback_prompt
    | ChatOpenAI(model="gpt-4o-mini")
    | StrOutputParser()
)
