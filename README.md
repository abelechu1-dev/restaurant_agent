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

- **Python** — Application logic
- **Google ADK** — AI agent framework
- **Google Gemini** — Natural language processing and reasoning
- **Yelp Fusion API** — Restaurant search
- **Requests** — API communication
- **python-dotenv** — Environment variable management

## 4. Agent Architecture

The agent uses a goal-based, tool-driven architecture.

**Architecture:**

```text
User Request
     |
     v
Google Gemini
     |
     v
recommend_restaurants()
     |
     v
search_restaurants()
     |
     v
check_constraints()
     |
     v
check_hours()
     |
     v
check_budget()
     |
     v
rank_restaurants()
     |
     v
Results + Decision Logs
     |
     v
Gemini Explanation
```

Gemini interprets the user's preferences and calls `recommend_restaurants()`, which executes the restaurant evaluation functions in a predefined order.

### Agent States

1. **Initial State:** Receive the user's request and extract preferences.
2. **Search State:** Retrieve restaurant candidates from Yelp.
3. **Filtering State:** Evaluate cuisine, opening hours, and available budget information.
4. **Ranking State:** Rank matching restaurants using Yelp ratings.
5. **Goal State:** Return recommendations with explanations.

### Agent Actions

- `search_restaurants()` — Search Yelp for restaurants.
- `check_constraints()` — Filter restaurants by cuisine.
- `check_hours()` — Check published operating hours.
- `check_budget()` — Record available budget information.
- `rank_restaurants()` — Rank restaurants by Yelp rating.
- `recommend_restaurants()` — Execute all five functions in a predefined order and record decision logs.

### Agent Goal

Find the best available Turkish restaurant in Downtown Baltimore for two people on Thursday at 7:30 PM, considering a total budget of $65 and the requested seating preference.

The agent must clearly identify any criteria it cannot verify.

## 5. AI Concepts

### Searching for Solutions

The agent searches Yelp to retrieve candidate restaurants based on cuisine and location.

### Reasoning with Constraints

The agent evaluates restaurants using the following criteria:

- **Cuisine:** Turkish
- **Location:** Downtown Baltimore
- **Budget:** $65 for two people
- **Time:** Thursday at 7:30 PM
- **Seating:** Window with a garden or street view

Cuisine and opening hours are checked against Yelp data. Location is used in the Yelp search query. Budget information is recorded using Yelp price categories, but exact meal costs cannot be confirmed. Seating preferences also cannot be verified through the available API.

Constraints that cannot be verified are reported rather than assumed satisfied.

### Deterministic Planning

The agent uses a predefined sequence of actions:

1. Understand the user request using Gemini.
2. Search Yelp for restaurants.
3. Filter restaurants by cuisine.
4. Check published opening hours.
5. Evaluate available budget information.
6. Rank restaurants by Yelp rating.
7. Explain the recommendations.

The Python function `recommend_restaurants()` enforces steps 2–6 in a fixed order.

This demonstrates deterministic planning because the sequence of operations is predefined rather than independently selected by Gemini.

However, the complete agent is not fully deterministic because Gemini's interpretation and Yelp's restaurant data can vary.

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

"Find a Turkish restaurant in Downtown Baltimore, MD, for two people on Thursday at 7:30 PM with a total budget of $65 and a table near a window overlooking a garden or street."

Gemini extracts the cuisine, location, budget, day, and time before calling the recommendation function.

## 9. Current Results

During earlier testing:

- Yelp restaurant searches successfully retrieved restaurant candidates.
- Cuisine filtering identified Cazbar as a Turkish restaurant.
- Published opening-hours checking showed that Cazbar's regular Thursday hours include 7:30 PM.
- Yelp reported a 4.2 rating and a `$$` price category for Cazbar at the time of testing.
- The Python recommendation pipeline successfully executed the filtering and ranking steps.

### Example Decision-Making Logs

```text
Search: Found 10 restaurants
Cuisine: 1 match Turkish
Hours: 1 match the requested time
Budget: $65 requested; exact prices not verified
Ranking: Sorted by Yelp rating
```

These logs demonstrate how the agent processes restaurant candidates.

The complete workflow still needs final verification through Google ADK Web.

## 10. Limitations

- Yelp price categories do not confirm exact meal costs for two people.
- Window seating and reservation availability cannot be verified through the current API.
- Exact Downtown Baltimore boundaries are not independently validated; location matching depends on Yelp search results.
- Published opening hours do not guarantee table availability or account for every temporary schedule change.
- Restaurants without Yelp ratings may be excluded by the ranking function.
- Complete Google ADK workflow and decision-log testing remain pending.

The agent should recommend contacting the restaurant for information unavailable through its tools.

## 11. Demonstration

The demonstration video will show:

1. The project source code and architecture.
2. Starting the agent using Google ADK.
3. Entering a restaurant recommendation request.
4. Inspecting the recommendation function and decision-making logs.
5. Displaying the final ranked restaurant recommendation.
6. Explaining verified and unverified constraints.

## 12. Conclusion

This project demonstrates how an AI agent can combine natural language understanding, restaurant searching, constraint reasoning, and deterministic planning.

Google Gemini interprets user requests, while Python functions retrieve and evaluate restaurant information from Yelp in a predefined sequence. The agent ranks suitable restaurants and explains its recommendations while identifying requirements that cannot be verified using the available data.

The project illustrates how generative AI can work alongside traditional Python programming to build a structured, tool-driven recommendation system.
