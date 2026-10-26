import os
import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

def search_restaurants(cuisine: str, location: str) -> dict:
    """Search Yelp for restaurants by cuisine and location."""

    url = "https://api.yelp.com/v3/businesses/search"

    api_key = os.getenv("YELP_API_KEY")

    if not api_key:
        return {"error": "Yelp API key not found"}

    headers = {
        "Authorization": "Bearer " + api_key
    }

    params = {
        "term": cuisine,
        "location": location,
        "limit": 10
    }

    try:
        response = requests.get(
            url, headers=headers, params=params, timeout=15
        )

        if response.status_code != 200:
            return {"error": response.text}

        restaurants = response.json()["businesses"]

        return {"restaurants": restaurants}

    except requests.RequestException as error:
        return {"error": str(error)}


def check_constraints(restaurants: list, cuisine: str) -> dict:
    """Filter restaurants by cuisine."""

    matches = []

    for restaurant in restaurants:
        for category in restaurant["categories"]:
            if category["title"].lower() == cuisine.lower():
                matches.append(restaurant)
                break

    return {"restaurants": matches}


def check_budget(restaurants: list, budget: int) -> dict:
    """Check restaurant prices against the user's budget."""

    results = []

    for restaurant in restaurants:
        price = restaurant.get("price", "Unknown")

        restaurant["budget_status"] = "Not verified"
        restaurant["budget_limit"] = budget

        results.append(restaurant)

    return {"restaurants": results}


def check_hours(restaurants: list, day: int, time: int) -> dict:
    """Find restaurants open at a given day and time."""

    matches = []

    for restaurant in restaurants:
        hours = restaurant.get("business_hours", [])

        for schedule in hours:
            for period in schedule.get("open", []):
                if period["day"] == day:
                    start = int(period["start"])
                    end = int(period["end"])

                    if start <= time < end:
                        matches.append(restaurant)
                        break

    return {"restaurants": matches}


def rank_restaurants(restaurants: list) -> dict:
    """Rank restaurants by rating."""

    ranked = sorted(
        restaurants,
        key=lambda r: r.get("rating", 0),
        reverse=True
    )

    return {"restaurants": ranked}