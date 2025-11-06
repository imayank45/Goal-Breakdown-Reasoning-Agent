from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Prompt to show plan + summary before asking review
review_prompt = PromptTemplate(
    template=(
        "Below is a summary and plan for a goal.\n\n"
        "Summary:\n{summary}\n\n"
        "Plan:\n{plan}\n\n"
        "Please enter your review as a customer (e.g., 'I like it', 'Needs improvement'):"
    ),
    input_variables=["plan", "summary"]
)

# Chain that asks customer for manual input
def review_chain(inputs):
    print("\n--- CUSTOMER REVIEW REQUIRED ---")
    print("Summary:\n", inputs["summary"])
    print("\nPlan:\n", inputs["plan"])
    review_input = input("\nEnter your review: ")
    return review_input
