
import os
import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))


# 1. Search Yelp
def search_restaurants(cuisine, location):
    """Search Yelp for restaurants."""

    api_key = os.getenv("YELP_API_KEY")

    if not api_key:
        return {"error": "Yelp API key not found"}

    url = "https://api.yelp.com/v3/businesses/search"
    headers = {"Authorization": "Bearer " + api_key}
    params = {"term": cuisine, "location": location, "limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=15)

        if response.status_code != 200:
            return {"error": response.text}

        return {"restaurants": response.json()["businesses"]}

    except requests.RequestException as error:
        return {"error": str(error)}


# 2. Filter by cuisine
def check_constraints(restaurants, cuisine):
    """Filter restaurants by cuisine."""

    matches = []

    for restaurant in restaurants:
        for category in restaurant.get("categories", []):
            if category["title"].lower() == cuisine.lower():
                matches.append(restaurant)
                break

    return {"restaurants": matches}


# 3. Check opening hours
def check_hours(restaurants, day, time):
    """Check published restaurant opening hours."""

    matches = []

    for restaurant in restaurants:
        for schedule in restaurant.get("business_hours", []):
            for period in schedule.get("open", []):
                if period["day"] == day:
                    start = int(period["start"])
                    end = int(period["end"])

                    if start <= time < end:
                        matches.append(restaurant)
                        break

    return {"restaurants": matches}


# 4. Check budget
def check_budget(restaurants, budget):
    """Record Yelp price information and budget."""

    for restaurant in restaurants:
        restaurant["yelp_price"] = restaurant.get("price", "Unknown")
        restaurant["budget_limit"] = budget
        restaurant["budget_status"] = "Not verified"

    return {"restaurants": restaurants}


# 5. Rank restaurants
def rank_restaurants(restaurants):
    """Rank restaurants by Yelp rating."""

    rated = []

    for restaurant in restaurants:
        if restaurant.get("rating") is not None:# I used not None here to make sure that there is no bias when selecting restaurant, in class we talked about replaing a missing value as true or false could raise a bias.
            rated.append(restaurant)

    ranked = sorted(
        rated,
        key=lambda r: r["rating"],
        reverse=True
    )

    return {"restaurants": ranked}

# 6. Main recommendation function
def recommend_restaurants(cuisine, location, budget, day, time):
    """Search, filter, rank, and record decisions."""

    logs = []

    result = search_restaurants(cuisine, location)

    if "error" in result:
        return {"error": result["error"], "logs": logs}

    restaurants = result["restaurants"]
    logs.append(f"Search: Found {len(restaurants)} restaurants")

    restaurants = check_constraints(restaurants, cuisine)["restaurants"]
    logs.append(f"Cuisine: {len(restaurants)} match {cuisine}")

    restaurants = check_hours(restaurants, day, time)["restaurants"]
    logs.append(f"Hours: {len(restaurants)} match the requested time")

    restaurants = check_budget(restaurants, budget)["restaurants"]
    logs.append(f"Budget: ${budget} requested; exact prices not verified")

    restaurants = rank_restaurants(restaurants)["restaurants"]
    logs.append("Ranking: Sorted by Yelp rating")

    return {"restaurants": restaurants, "logs": logs}
