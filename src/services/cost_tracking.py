import tiktoken

def count_tokens(text: str, model: str = "gpt-4o-mini") -> int:
    """Counts the number of tokens in a given text for a specific model."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")  # Fallback encoding
    return len(encoding.encode(text))

def analyze_query_cost(input: str, output: str, provider: str = "gpt-4o-mini") -> dict:
    """
    Calculates the cost of a single RAG query based on the active model provider.
    Prices are defined per 1,000,000 tokens.
    """
    input_tokens = count_tokens(input, model=provider)
    output_tokens = count_tokens(output, model=provider)
    
    # Define your pricing matrix
    pricing_matrix = {
        "gpt-4o-mini": {"in": 0.150, "out": 0.600},
        "claude-3-haiku": {"in": 0.250, "out": 1.250},
        
        # When you switch to your local Unsloth model on AWS, 
        # the token cost is technically zero (you pay for server uptime instead)
        "local_llama_3": {"in": 0.0, "out": 0.0} 
    }
    
    rates = pricing_matrix.get(provider, {"in": 0.0, "out": 0.0})
    
    # Calculate costs (Tokens / 1,000,000 * Rate)
    input_cost = (input_tokens / 1_000_000) * rates["in"]
    output_cost = (output_tokens / 1_000_000) * rates["out"]
    total_cost = input_cost + output_cost
    
    return {
        "provider": provider,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_cost_usd": total_cost,
        "formatted_cost": f"${total_cost:.6f}"
    }

# Example Usage:
# result = analyze_query_cost(1200, 300, "gpt-4o-mini")
# print(result["formatted_cost"]) # Outputs: $0.000360