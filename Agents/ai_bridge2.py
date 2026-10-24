import requests
from pydantic import BaseModel,EmailStr,PositiveInt,ValidationError

# 1. DEFINE THE VALIDATION MODEL
# We expect the LLM to return a profile containing exactly these three fields.
# Pydantic will auto-cast types (e.g., converting string "95" to integer 95) or fail fast.
class UserInsight(BaseModel):
    user_name: str
    sentiment_score: int
    is_flagged_for_review: bool

print("--- MODEL INITIALIZED ---")
print("Pydantic Schema enforces: user_name (str), sentiment_score (int), is_flagged_for_review (bool)\n")

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
print(response.json())