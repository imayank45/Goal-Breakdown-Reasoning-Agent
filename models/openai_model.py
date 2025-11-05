from langchain_openai import ChatOpenAI

def get_openai_model(model_name='gpt-4o-mini', temperature=0.7):
    """Returns an instance of ChatOpenAI with specified parameters."""
    return ChatOpenAI(model_name=model_name, temperature=temperature)