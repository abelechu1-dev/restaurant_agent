
# Restaurant Recommendation AI Agent

## Overview
An intelligent restaurant recommendation agent built using Python, Google ADK, Gemini, and the Yelp Fusion API.

The agent understands user preferences, searches restaurants, evaluates constraints, and recommends suitable options.

## Technologies
- Python
- Google ADK
- Google Gemini
- Yelp Fusion API
- Requests and python-dotenv

## Agent Architecture
The agent uses a goal-based, tool-driven architecture.

User Request → Gemini → Yelp Search → Constraint Checking → Ranking → Recommendation

Gemini understands the request and selects tools. Python functions perform searching, filtering, and ranking.

## States, Actions, and Goals

**States:**
1. Initial — Receive and understand user preferences.
2. Search — Retrieve restaurants from Yelp.
3. Filter — Evaluate cuisine, location, hours, and budget.
4. Rank — Order matching restaurants.
5. Goal — Return recommendations with explanations.

**Actions:**
- `search_restaurants()` — Search Yelp.
- `check_constraints()` — Filter by cuisine.
- `check_hours()` — Check operating hours.
- `check_budget()` — Evaluate budget information.
- `rank_restaurants()` — Rank by rating.

**Goal:** Find a Turkish restaurant in Downtown Baltimore for two people, Thursday at 7:30 PM, under $65, with the requested seating preference.

## AI Concepts

**Searching for Solutions:** Yelp retrieves restaurant candidates.

**Reasoning with Constraints:** Python evaluates restaurant information against user requirements.

**Deterministic Planning:** A predefined pipeline can enforce the sequence of search, filtering, hours checking, budget evaluation, and ranking.

**NLP:** Gemini extracts user preferences from natural language.

## Installation

```bash
pip install google-adk requests python-dotenv
```

Create `restaurant_recommender/.env`:

```env
GOOGLE_API_KEY=your_key
YELP_API_KEY=your_key
```

Run the agent from the project root:

```bash
adk web
```

## Example Request

Find a Turkish restaurant in Downtown Baltimore for two people on Thursday at 7:30 PM with a $65 budget.

## Current Results

- Yelp restaurant search works.
- Turkish cuisine filtering works.
- Thursday opening-hours checking works.
- Cazbar was identified as a matching candidate.
- Gemini generates restaurant recommendations.

## Limitations

Yelp price categories do not confirm a $65 total meal cost. Window seating and reservation availability cannot be verified through the current tools.

Budget filtering, full execution logging, and deterministic workflow verification are still being completed.
