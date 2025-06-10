from services.ai_helper import get_gemini_response, load_prompt

def get_peers(symbol, company_name):
    prompt = load_prompt("prompts/peer_prompt.txt", symbol=symbol, company_name=company_name)
    return get_gemini_response(prompt)

def get_price_prediction(symbol, recent_data):
    # Safely format recent data to avoid exceeding Gemini prompt limits
    recent_data_str = recent_data.tail(60).to_string(index=False)

    if len(recent_data_str) > 3000:
        recent_data_str = recent_data.tail(10).to_string(index=False)

    prompt = load_prompt("prompts/prediction_prompt.txt", symbol=symbol, data=recent_data_str)
    return get_gemini_response(prompt)

def get_recommendation(symbol, price_data):
    prompt = load_prompt("prompts/recommendation_prompt.txt", symbol=symbol, data=price_data.tail(60).to_string())
    return get_gemini_response(prompt)
