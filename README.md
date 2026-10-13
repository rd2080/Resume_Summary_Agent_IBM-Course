# Resume Summary Agent — IBM Course

V1 implementation of a resume summary workflow built with Python and LangGraph.

See [resume_summary_agent/README.md](resume_summary_agent/README.md) for setup and usage.

The workflow extracts requirements from a job description, retrieves relevant structured profile facts, assembles a tailored summary from exact source fact wording, and rejects unsupported claims. OpenAI credentials are read from environment variables.

## Quick start

```sh
cd resume_summary_agent
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=your_api_key_here
python cli.py --jd examples/job_description.txt --profile examples/profile.json
pytest
```

Review and verify every example profile fact before using the sample in an application. Never add claims or metrics that are not supported by your records.
