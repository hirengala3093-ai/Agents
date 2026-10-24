# 2. CONSTRUCTING THE API CALL

import requests
from pydantic import BaseModel,EmailStr,PositiveInt,ValidationError

from ai_bridge2 import UserInsight


def analyze_user_data_via_api():
    # A dummy endpoint that simulates receiving a JSON payload from an LLM
    api_url = "https://jsonplaceholder.typicode.com/posts"

    # 2a. The Headers (Authentication Layer)
    # In a real scenario, "Bearer YOUR_API_KEY" goes here.
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer sk-mock-api-key-12345"
    }

    # 2b. The Payload (Intelligence Layer)
    # This represents exactly what we send to OpenAI or Anthropic.
    payload = {
        "model": "gpt-4-turbo",
        "messages": [
            {"role": "system", "content": "You analyze user sentiment."},
            {"role": "user", "content": "Analyze the sentiment for user 'Alice'."}
        ]
    }

    print("--- TRANSMITTING HTTP POST REQUEST ---")


# 2. CONSTRUCTING THE API CALL
def analyze_user_data_via_api():
    # A dummy endpoint that simulates receiving a JSON payload from an LLM
    api_url = "https://jsonplaceholder.typicode.com/posts"

    # 2a. The Headers (Authentication Layer)
    # In a real scenario, "Bearer YOUR_API_KEY" goes here.
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer sk-mock-api-key-12345"
    }

    # 2b. The Payload (Intelligence Layer)
    # This represents exactly what we send to OpenAI or Anthropic.
    payload = {
        "model": "gpt-4-turbo",
        "messages": [
            {"role": "system", "content": "You analyze user sentiment."},
            {"role": "user", "content": "Analyze the sentiment for user 'Alice'."}
        ]
    }

    print("--- TRANSMITTING HTTP POST REQUEST ---")

# 4. END-TO-END EXECUTION & VALIDATION
if __name__ == "__main__":
    # Step A: Get the raw data from the web
    raw_api_data = analyze_user_data_via_api()

    if raw_api_data:
        print("--- VALIDATING RAW LLM OUTPUT ---")
        print(f"Raw Data received: {raw_api_data}\n")

        try:
            # Step B: Pass the raw dictionary into our strict Pydantic model
            # This is where the magic happens (Auto-casting strings to ints/bools)
            validated_insight = UserInsight(**raw_api_data)

            print("--- VALIDATION SUCCESSFUL! ---")
            print(f"Secured Object: {validated_insight}")

            # Now your IDE knows exactly what data types these are!
            print(f"Cleaned Score (Now a true Integer): {validated_insight.sentiment_score + 10}")

        except ValidationError as e:
            # Step C: Fail Fast if the LLM completely hallucinated the structure
            print(f"[VALIDATION CRASH] The LLM failed to match our schema:\n{e.json()}")
