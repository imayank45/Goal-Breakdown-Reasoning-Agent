from .openai_model import get_openai_model

def create_model(provider='openai', **kwargs):
    """Factory function to create and return a model instance based on the provider."""
    if provider == 'openai':
        return get_openai_model(**kwargs)
    else:
        raise ValueError(f"Unsupported model provider: {provider}")