# Contributing

This repository is shared by a four-person group. Keep `main` stable.

## Workflow
1. Pull the latest `main`.
2. Check GitHub Issues/Projects and agree who owns the task.
3. Create a focused branch, e.g. `feature/map-view`, `feature/linked-brushing`, `data/missingness`, or `docs/user-tasks`.
4. Make small, descriptive commits.
5. Push the branch and open a pull request into `main`.
6. Ask another member to review; address feedback and test before merging.

Do not push unfinished work directly to `main`.

## Conventions
- Never commit secrets, `.venv/`, or raw/large generated data.
- Keep the original CSV unchanged; document transformations.
- Put reusable data logic in `data/`, individual plots in `visualizations/`, and shared selection logic in `interactions/`.
- Update docs and tests when changing data processing or interaction behaviour.
- Agree on shared interfaces before multiple people work on linked views.
