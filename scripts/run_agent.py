name: Run Claude Agent

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  run-agent:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip uninstall anthropic -y || true
          pip install anthropic

      - name: Run agent script
        env:
          ANTHROPIC_API_KEY: ${{ secrets.CLAUDE_API_KEY }}
        run: |
          if [ -z "$ANTHROPIC_API_KEY" ]; then
            echo "❌ CLAUDE_API_KEY secret is not set"
            exit 1
          fi
          python scripts/run_agent.py
