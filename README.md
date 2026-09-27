# MetaSquad Engine ⚽🧠

> **An algorithmic eFootball squad optimizer that predicts peak performance, maps optimal progression points, and solves for the best tactical starting XI.**

Most companion apps act as simple database lookups for maximum Overall Rating (OVR). MetaSquad Engine treats team building as a combinatorial optimization problem. It calculates the mathematically optimal way to allocate progression points for a player's specific tactical role, identifies missing "meta" skills, and evaluates thousands of permutations to output the perfect 11-man formation.

## 🚀 Core Features

- **Role-Based Progression Optimizer:** Uses integer linear programming (via SciPy) to allocate training points, maximizing hidden stat weights for specific roles (e.g., heavily weighting Defensive Awareness for a _Build Up CB_) instead of chasing raw OVR.
- **Combinatorial Formation Solver:** Evaluates player pools against positional constraints and playstyle synergies (e.g., pairing a _Goal Poacher_ with a _Creative Playmaker_) to calculate the ultimate starting XI.
- **Skill Token Recommendation Matrix:** Flags missing meta skills (like _Blocker_ or _Aerial Superiority_) required to optimize a base card for its selected role.
- **Automated Roster Ingestion:** Multimodal OCR pipeline to parse user screenshots of their "My Team" page directly into the optimization engine.

## 🛠️ Tech Stack

- **Core Engine:** Python, NumPy, SciPy (Combinatorics & Optimization)
- **Backend API:** FastAPI, Uvicorn, Pydantic
- **Package Management:** [uv](https://github.com/astral-sh/uv) (for lightning-fast dependency resolution)
- **Data Acquisition:** BeautifulSoup4 (Static player database parsing)

## ⚡ Getting Started

This project uses `uv` for modern dependency and virtual environment management.

### 1. Clone the repository

```bash
git clone [https://github.com/yourusername/metasquad-engine.git](https://github.com/yourusername/metasquad-engine.git)
cd metasquad-engine
```
