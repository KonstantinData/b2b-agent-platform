# AI Research Pipeline (GitHub Actions)

**Purpose**: Fully automated research → competitor discovery → buyer identification → HubSpot integration.  
**Start**: via GitHub Actions UI or Issue Form.

## Quick Start
1. Set repository **Secrets**: `OPENAI_API_KEY`, `HUBSPOT_API_KEY` (or OAuth trio), optional `DEEPL_API_KEY`, `OPENCORPORATES_API_KEY`, `SERPAPI_API_KEY`.
2. Go to **Actions → Run research** and provide inputs.
3. Outputs appear as **Artifacts** (CSV/JSON/PDF) and in `data/outputs/`.

## Structure
- `agents/`: three agent modules + mapping maintenance.
- `integrations/`: HubSpot upsert and PDF builder.
- `data/`: mapping + master list + outputs.
- `.github/workflows/`: two workflows (UI + Issue form).
- `.github/ISSUE_TEMPLATE/`: issue form to trigger runs.
