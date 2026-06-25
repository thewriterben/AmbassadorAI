"""Regression tests for the DGD toolchain's pure logic. Run: pytest -q"""
import json
import os

TOOLS = os.path.join(os.path.dirname(__file__), "..", "tools")


# ---------------------------------------------------------------- compliance_lint
def test_lint_verdicts():
    import compliance_lint as CL
    assert CL.lint_text("Buy DGD now for 100x returns")["verdict"] == "fail"
    assert CL.lint_text("Read the white paper. Not financial advice.")["verdict"] == "pass"
    # plain verb 'buys' must not FAIL (educational), only warn
    assert CL.lint_text("Your money buys a little less each year")["verdict"] == "warn"
    # 'safe harbor' (legal term) is allowed; 'safe haven' (money claim) is not
    assert CL.lint_text("DGD is designed as a safe harbor digital commodity")["verdict"] != "fail"
    assert CL.lint_text("DGD is a safe haven for your money")["verdict"] == "fail"


def test_lint_matches_eval_cases():
    import compliance_lint as CL
    cases = json.load(open(os.path.join(TOOLS, "compliance_cases.json"), encoding="utf-8"))["cases"]
    for c in cases:
        assert CL.lint_text(c["text"])["verdict"] == c["expect"], c["id"]


# ---------------------------------------------------------------- dgd_publish
def test_publish_caption_disclosures_and_budget():
    import dgd_publish as P
    cap, warns = P.build_caption("x", "Money covers less each year.", P.SAFE_TAGS, True, True)
    assert "#Ad" in cap
    assert "Not financial advice" in cap
    assert "Made with AI" in cap
    assert len(cap) <= 280 or warns  # within X budget, or it warned


def test_publish_youtube_settings():
    import dgd_publish as P
    s = P.provider_settings("youtube", "My Title", P.SAFE_TAGS, False)
    assert s["title"] == "My Title" and s["type"] == "public" and isinstance(s["tags"], list)


# ---------------------------------------------------------------- dgd_performance
def test_perf_metrics():
    import dgd_performance as M
    r = {"impressions": 1000, "likes": 40, "comments": 5, "shares": 5, "saves": 0, "follows": 20}
    assert abs(M.eng_rate(r) - 0.05) < 1e-9
    assert abs(M.follow_yield(r) - 20.0) < 1e-9
    assert M.eng_rate({"impressions": 0}) == 0.0  # no divide-by-zero


def test_perf_rank_orders_by_engagement():
    import dgd_performance as M
    rows = [{"hook": "A", "impressions": 100, "likes": 10, "comments": 0, "shares": 0, "saves": 0, "follows": 1},
            {"hook": "B", "impressions": 100, "likes": 1, "comments": 0, "shares": 0, "saves": 0, "follows": 0}]
    assert M._rank(rows, "hook")[0]["key"] == "A"


# ---------------------------------------------------------------- dgd_ai (gate loop)
def test_ai_gate_retries_then_passes(monkeypatch):
    import dgd_ai
    state = {"n": 0}
    def fake(system, user):
        state["n"] += 1
        if state["n"] == 1:
            return ("Buy now for guaranteed 100x returns!", "mock")
        return ("Money is a system with fixed, transparent rules. Not financial advice.", "mock")
    monkeypatch.setattr(dgd_ai, "call_llm", fake)
    r = dgd_ai.generate("hooks", "inflation")
    assert r["verdict"] != "fail" and r["attempts"] == 2


def test_ai_gate_blocks_persistent_violation(monkeypatch):
    import dgd_ai
    monkeypatch.setattr(dgd_ai, "call_llm", lambda s, u: ("guaranteed profit, buy now", "mock"))
    assert dgd_ai.generate("hooks", "x")["verdict"] == "fail"


# ---------------------------------------------------------------- dgd_assets
def test_assets_scan_and_font_fallback():
    import dgd_assets as A
    assert A.compliance_scan("buy now")          # banned -> non-empty hits
    assert not A.compliance_scan("sound money explained")
    assert A._font(None, 20) is not None          # cross-platform fallback always returns a font
