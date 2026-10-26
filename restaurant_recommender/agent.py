
from google.adk.agents import Agent
from .tools import recommend_restaurants

root_agent = Agent(
    model="gemini-3.8-flash",
    name="restaurant_agent",
    description="Finds and recommends restaurants using Yelp.",

    instruction="""
    You are an intelligent restaurant recommendation agent.

    1. Understand the user's cuisine, location, budget, day, and time.
    2. Call recommend_restaurants to find and evaluate restaurants.
    3. Display the returned logs under "Decision-Making Process".
    4. Show the ranked restaurants with ratings and Yelp price categories.
    5. Explain why the restaurants were recommended.

    Monday=0, Tuesday=1, Wednesday=2, Thursday=3,
    Friday=4, Saturday=5, Sunday=6.

    Use 24-hour time (7:30 PM = 1930).

    Never invent restaurant prices or availability.
    If information cannot be verified, say so.
    """,

    tools=[recommend_restaurants]
)
