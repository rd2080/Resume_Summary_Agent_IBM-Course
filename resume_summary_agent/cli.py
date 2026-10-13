"""Command line interface for the Resume Summary Agent."""
import argparse
import json
from pathlib import Path

from agent import run


def main() -> None:
    parser = argparse.ArgumentParser(description="Create an evidence-grounded resume summary")
    parser.add_argument("--jd", required=True, type=Path, help="Text file containing the job description")
    parser.add_argument("--profile", required=True, type=Path, help="JSON candidate profile")
    args = parser.parse_args()
    result = run(args.jd.read_text(encoding="utf-8"), json.loads(args.profile.read_text(encoding="utf-8")))
    print(json.dumps({
        "requirements": result["requirements"],
        "relevant_facts": result["relevant_facts"],
        "summary": result["summary"],
        "unsupported_claims": result["unsupported_claims"],
    }, indent=2, ensure_ascii=False))
    if result["unsupported_claims"]:
        raise SystemExit("Summary rejected: unsupported claims detected")


if __name__ == "__main__":
    main()
