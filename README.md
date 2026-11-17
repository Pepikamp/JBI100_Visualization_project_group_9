# Visualization Project – Group 14

JBI100 Visualization course project: an interactive, coordinated-view exploration tool for the **Global Power Plant Database (WRI), version 1.3.0**.

## Goal and design
The group will define its target users, analytical goal, tasks, views, and linked interactions through data exploration. The intended application uses coordinated multiple views: selections in one view (such as brushing a scatterplot) should be reflected in other views (such as highlighting matching plants on a map).

## Dataset
Source: [WRI Global Power Plant Database](https://datasets.wri.org/datasets/global-power-plant-database)  
Release: 1.3.0  
Expected CSV: `global_power_plant_database.csv`

Download and extract the WRI release, then put the CSV at `data/raw/global_power_plant_database.csv`. Keep raw data unchanged. The dataset is not included in this repository. Check the source's license and attribution requirements before redistribution.

## Structure
- `data/raw/`: original downloaded CSV (ignored by Git)
- `data/processed/`: generated/cleaned data (ignored by Git)
- `data/data_dictionary.md`: attribute definitions
- `docs/`: project definition, data analysis, tasks, design, interactions, evaluation
- `notebooks/`: exploratory notebooks
- `src/visualization_project/`: Dash app, data utilities, views, interactions
- `tests/`: automated tests

## Setup
Create a virtual environment and install dependencies:

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Place the CSV at `data/raw/global_power_plant_database.csv`, then run:

```bash
python -m src.visualization_project.app
```

Open `http://127.0.0.1:8050/`. The initial app is a scaffold, not the finished visualization.

## Group 14
Four members; fill in names and GitHub usernames:

| Member | GitHub username | Responsibilities |
|---|---|---|
| 1 | TBD | TBD |
| 2 | TBD | TBD |
| 3 | TBD | TBD |
| 4 | TBD | TBD |

## Course documentation
Use the templates in `docs/` to document domain/users/goal, data attributes and quality, user tasks, visual encodings and rationale, linked interactions, and evaluation findings.

## License
The license for our own code has not yet been selected. The dataset and our code may have different licensing terms.
