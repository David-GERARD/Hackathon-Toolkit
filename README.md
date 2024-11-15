
# Hackathon-Toolkit

Hackathon-Toolkit is a streamlined project structure designed to help developers collaborate efficiently on hackathon projects. This repository enforces good coding practices, encourages modular development, and ensures reproducibility with a built-in environment and CI/CD pipeline.

---

## Setup Guide

### Fetch and Connect All Remote Branches
To clone the repository and set up the branches:
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Fetch all remote branches:
   ```bash
   git fetch --all
   ```
3. Set up tracking for `main` and `dev` branches:
   ```bash
   git checkout main
   git pull origin main
   git checkout -b dev origin/dev
   ```

Now you have both `main` and `dev` branches locally.

---

### Creating and Activating the Conda Environment
The project uses a Conda environment defined in `env/environment.yml` to ensure consistent dependencies for all collaborators. Setting it up is crucial for reproducibility and seamless workflow integration.

1. Create the Conda environment:
   ```bash
   conda env create -f env/environment.yml
   ```
2. Activate the environment:
   ```bash
   conda activate hackathon
   ```
3. Verify the environment setup:
   ```bash
   python --version
   ```

This ensures that all team members work in the same environment, avoiding "it works on my machine" problems.

---

## Development Workflow

### Use `dev` Branch for Development
- Always work on the `dev` branch for development.
- Push your changes to `dev` and create pull requests for merging into the `main` branch.
- The `main` branch is reserved for stable, production-ready code.

```bash
git checkout dev
# Make your changes
git add .
git commit -m "Your commit message"
git push origin dev
```

### Pull Requests
- Ensure all changes are reviewed and tested before merging into `main`.
- Create a pull request targeting the `main` branch from the `dev` branch.

---

### Modular Development
- Develop individual components as separate Python files within the `src/` directory.
- Integrate and call these modules in `src/main.py`, which serves as the primary pipeline for execution.

Example file structure:
```
src/
├── module1.py
├── module2.py
├── main.py
```

**Tip:** Keep functions reusable and well-documented to encourage collaboration.

---

## Continuous Integration and Code Quality

This repository uses a GitHub Actions workflow to maintain code quality and reproducibility:
1. **Code Quality**: Runs `pylint` to enforce coding standards.
2. **Reproducibility**: Ensures `src/main.py` and `src/streamlit_GUI.py` run without errors.

When you push changes or create a pull request, the workflow will automatically:
- Check for linting issues.
- Run `src/main.py` and `src/streamlit_GUI.py` in a CI environment.

Fix any issues reported in the workflow before merging your changes.

---

## Happy Hacking! 🚀
```
