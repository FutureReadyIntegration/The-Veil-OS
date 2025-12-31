# ───────────────────────────────────────────────
# The Veil — Makefile
# Common operational commands
# ───────────────────────────────────────────────

ENV=veil-env
PYTHON=python

# Activate environment
activate:
    @echo "Activating environment..."
    @conda activate $(ENV)

# Run the dashboard
dashboard:
    $(PYTHON) src/veil/gui/dashboard.py

# Run individual organs
guardian:
    $(PYTHON) -m veil.organs.guardian

chronicle:
    $(PYTHON) -m veil.organs.chronicle

hospital:
    $(PYTHON) -m veil.organs.hospital

reconciler:
    $(PYTHON) -m veil.organs.reconciler

weaver:
    $(PYTHON) -m veil.organs.weaver

# Bootstrap runtime directories
bootstrap:
    $(PYTHON) scripts/bootstrap.py

# Run tests
test:
    pytest -q

# Format code
format:
    black src
    ruff check src --fix

# Clean caches
clean:
    find . -type d -name "__pycache__" -exec rm -rf {} +
