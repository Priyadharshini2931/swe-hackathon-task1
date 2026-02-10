name: Claude API Check

on:
  push:
    branches: [ "main" ]
  pull_request:

jobs:
  check-api-key:
    runs-on: ubuntu-latest

    env:
      CLAUDE_API_KEY: ${{ secrets.CLAUDE_API_KEY }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Verify Claude API key
        run: |
          if [ -z "$CLAUDE_API_KEY" ]; then
            echo "❌ Error: CLAUDE_API_KEY secret is not set in repository secrets."
            echo "👉 Please add your Anthropic API key as a repository secret named 'CLAUDE_API_KEY'."
            echo "👉 Go to: Settings > Secrets and variables > Actions > New repository secret"
            exit 1
          fi

          echo "✅ CLAUDE_API_KEY is set"
