from google.adk.agents import Agent
from .tools import (
    search_restaurants,
    check_constraints,
    check_budget,
    check_hours,
    rank_restaurants
)

root_agent = Agent(
    model="gemini-3.8-flash",
    name="restaurant_agent",
    description="Finds and recommends restaurants using Yelp.",
    instruction="""
    You are an intelligent restaurant recommendation agent.

    Follow these steps:

    1. Understand the user's preferences:
       cuisine, location, budget, date, time, and seating.

    2. Call search_restaurants to search Yelp.

    3. Call check_constraints to filter by cuisine.

    4. Call check_hours to check opening hours.

    5. Call check_budget to evaluate budget information.

    6. Call rank_restaurants to rank matching restaurants.

    7. Explain why each restaurant was selected or rejected.

    Never invent restaurant details, prices, or availability.
    Yelp price tiers are not exact meal costs.
    Window seating must be verified separately.
    """,
    tools=[
        search_restaurants,check_constraints,check_budget,check_hours,rank_restaurants],
)