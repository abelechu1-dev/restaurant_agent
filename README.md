
# Restaurant Recommendation AI Agent

## 1. Project Overview

This project is an intelligent restaurant recommendation agent developed using Python, Google ADK, Google Gemini, and the Yelp Fusion API.

The agent understands natural language requests, searches for restaurants, evaluates user constraints, and recommends suitable restaurants.

The project demonstrates three AI concepts:
- Searching for Solutions
- Reasoning with Constraints
- Deterministic Planning

## 2. Problem Statement

The agent is designed to handle requests such as:

"Find a Turkish restaurant in Downtown Baltimore, MD for two people to have dinner under $65 on Thursday night at 7:30 PM with a table for two near a window overlooking a garden or street."

The agent evaluates restaurant information and explains which requirements are satisfied and which cannot be verified.

## 3. Technologies Used

- Python — Application logic
- Google ADK — AI agent framework
- Google Gemini — Natural language processing and reasoning
- Yelp Fusion API — Restaurant search
- Requests — API communication
- python-dotenv — Environment variable management

## 4. Agent Architecture

The agent uses a goal-based, tool-driven architecture.

User Request → Gemini → Restaurant Search → Constraint Checking → Ranking → Recommendation

Gemini interprets the user's preferences and invokes Python tools to retrieve and evaluate restaurant information.

### Agent States

1. **Initial State:** Receive the user's request and extract preferences.
2. **Search State:** Retrieve restaurant candidates from Yelp.
3. **Filtering State:** Evaluate cuisine, location, opening hours, and budget.
4. **Ranking State:** Rank suitable restaurants using Yelp ratings.
5. **Goal State:** Return recommendations with explanations.

### Agent Actions

- `search_restaurants()` — Search Yelp for restaurants.
- `check_constraints()` — Filter restaurants by cuisine.
- `check_hours()` — Check published operating hours.
- `check_budget()` — Evaluate available budget information.
- `rank_restaurants()` — Rank restaurants by Yelp rating.

The agent may also use `recommend_restaurants()` to execute these actions in a predefined order.

### Agent Goal

Find the best available Turkish restaurant in Downtown Baltimore for two people on Thursday at 7:30 PM, with a total budget of $65 and the requested seating preference.

The agent must clearly identify any criteria it cannot verify.

## 5. AI Concepts

### Searching for Solutions

The agent searches Yelp to retrieve candidate restaurants based on cuisine and location.

### Reasoning with Constraints

The agent evaluates restaurants using:
- Cuisine: Turkish
- Location: Downtown Baltimore
- Budget: $65 for two people
- Time: Thursday at 7:30 PM
- Seating: Window with a garden or street view

Constraints that cannot be verified are reported rather than assumed satisfied.

### Deterministic Planning

The planned sequence is:

1. Understand the user request.
2. Search for restaurants.
3. Filter by cuisine.
4. Check opening hours.
5. Evaluate budget.
6. Rank candidates.
7. Explain recommendations.

A Python orchestration function can enforce this sequence. Full workflow testing is still pending.

## 6. Project Structure

```text
restaurant_agent/
|
|-- restaurant_recommender/
|   |-- __init__.py
|   |-- agent.py
|   |-- tools.py
|   |-- .env
|   |-- .gitignore
|
|-- README.md
```

## 7. Installation

Install the required libraries:

```bash
pip install google-adk requests python-dotenv
```

Create `restaurant_recommender/.env` and add:

```env
GOOGLE_API_KEY=your_google_api_key
YELP_API_KEY=your_yelp_api_key
```

Run the application from the project root:

```bash
adk web
```

Open the local address shown in the terminal and select `restaurant_recommender`.

## 8. Example Request

Find a Turkish restaurant in Downtown Baltimore for two people on Thursday at 7:30 PM with a total budget of $65.

## 9. Current Results

During testing:
- Yelp restaurant search successfully retrieved restaurant candidates.
- Cuisine filtering identified Cazbar as a Turkish restaurant.
- Published opening-hours checking confirmed Cazbar's regular Thursday hours include 7:30 PM.
- Gemini generated restaurant recommendations.

## 10. Limitations

- Yelp price categories do not confirm exact meal costs.
- Window seating and reservation availability cannot be verified through the current API.
- Exact Downtown Baltimore boundaries are not yet validated this is higly dependent on the data received from YELP.
- Complete deterministic workflow and decision-log testing are pending.

The agent should recommend contacting the restaurant for information unavailable through its tools.

## 11. Demonstration

The demonstration video will show:
1. The project source code and architecture.
2. Starting the agent using Google ADK.
3. Entering a restaurant recommendation request.
4. Inspecting tool execution and filtering.
5. Displaying the final restaurant recommendation.

## 12. Conclusion

This project demonstrates a restaurant recommendation AI agent combining Gemini's natural language understanding with Yelp restaurant search and Python-based constraint evaluation.

The agent provides recommendations using available evidence while clearly communicating unverified requirements.
