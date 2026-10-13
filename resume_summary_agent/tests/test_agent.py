import agent


PROFILE = {
    "facts": [
        {"id": "a", "text": "Anaplan Model Builder with L1 certification.", "tags": ["Anaplan", "model builder"]},
        {"id": "b", "text": "Experience with SQL.", "tags": ["SQL"]},
    ]
}


def test_retrieval_selects_relevant_verified_facts():
    state = {
        "profile": PROFILE,
        "requirements": {"skills": ["Anaplan model building"], "responsibilities": [], "experience": [], "qualifications": []},
    }
    result = agent.retrieve_profile_facts(state)
    assert [fact["id"] for fact in result["relevant_facts"]] == ["a"]


def test_summary_uses_exact_profile_fact_text():
    state = {"profile": PROFILE, "relevant_facts": [PROFILE["facts"][0]]}
    result = agent.check_claims(agent.generate_summary(state))
    assert result["summary"] == PROFILE["facts"][0]["text"]
    assert result["unsupported_claims"] == []


def test_unsupported_claim_is_rejected_and_removed():
    state = {
        "profile": PROFILE,
        "summary": "Anaplan Model Builder with L1 certification.\nDelivered 40% faster planning cycles.",
    }
    result = agent.check_claims(state)
    assert result["unsupported_claims"] == ["Delivered 40% faster planning cycles."]
    assert result["summary"] == ""


def test_input_validation_rejects_duplicate_fact_ids():
    profile = {"facts": [
        {"id": "same", "text": "First fact."},
        {"id": "same", "text": "Second fact."},
    ]}
    try:
        agent.validate_inputs({"job_description": "A role", "profile": profile})
    except ValueError as exc:
        assert "Duplicate" in str(exc)
    else:
        raise AssertionError("duplicate IDs should fail validation")
