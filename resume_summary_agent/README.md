# Resume Summary Agent V1

A small Python CLI workflow that extracts job requirements, retrieves relevant candidate evidence, drafts a targeted summary, and rejects unsupported claims. It follows the notebook's LangGraph `TypedDict` shared-state and sequential `StateGraph` prompt-chaining pattern. The JD extractor calls OpenAI; retrieval and summary assembly are deterministic. Summary sentences are copied verbatim from profile facts so the claim checker can enforce evidence grounding.

## Setup

Use Python 3.10 or newer. From this directory:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set `OPENAI_API_KEY` in your shell (or export it after copying `.env`; the CLI does not automatically load `.env`). Optionally set `OPENAI_MODEL`.

## Run

```sh
python cli.py --jd examples/job_description.txt --profile examples/profile.json
```

The output is JSON containing extracted requirements, selected source facts, the summary, and any unsupported claims. Edit the profile JSON to add only facts you can verify from your resume or experience repository. The included profile reflects the currently established Anaplan profile details; review each sentence before using it in an application.

## Tests

```sh
pytest
```

The tests cover retrieval, verbatim summary assembly, duplicate source identifiers, and rejection of a fabricated quantified claim. Tests do not make API calls.

## V1 limits

- JD requirements depend on the model's extraction quality.
- Fact retrieval uses simple phrase-token overlap and tags; it is not semantic search.
- To preserve verifiability, summary generation selects and joins source sentences rather than paraphrasing them.
- No frontend, database, resume parsing, routing, or cover-letter generation is included.
