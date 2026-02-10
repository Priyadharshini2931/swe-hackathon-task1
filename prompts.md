# Prompts Used

## Initial Task Analysis
The task was to improve ISBN import logic by using local staged records from the `import_item` table instead of external API calls.
Identifiers (e.g., ISBNs) should be checked against `ia_id` in the format `{source}:{identifier}` where sources include `amazon` and `idb`.

## Technical Requirements Prompt
- A fixed constant tuple for source identifiers: `STAGED_SOURCES = ('amazon', 'idb')`.
- A method `find_staged_or_pending` in `ImportItem` returning a `ResultSet` of matching entries with status 'staged' or 'pending'.
- Standardize `ia_id` as `{source}:{identifier}`.

## Fix Implementation
Modified `openlibrary/core/imports.py` to add defined constants and methods.
Refactored `openlibrary/core/models.py`'s `Edition.from_isbn` to utilize the new centralized logic.
