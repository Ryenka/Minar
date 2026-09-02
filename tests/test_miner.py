from src.miner import has_agentic_workflow


def test_has_agentic_workflow_positive():
    files = ["daily-report.md", "daily-report.lock.yml", "ci.yml"]
    assert has_agentic_workflow(files) is True


def test_has_agentic_workflow_only_md():
    files = ["daily-report.md", "ci.yml"]
    assert has_agentic_workflow(files) is False


def test_has_agentic_workflow_only_lock():
    files = ["daily-report.lock.yml", "ci.yml"]
    assert has_agentic_workflow(files) is False


def test_has_agentic_workflow_mismatched_names():
    files = ["daily-report.md", "other-task.lock.yml"]
    assert has_agentic_workflow(files) is False


def test_has_agentic_workflow_multiple_files():
    files = [
        "deploy.yml",
        "agent_a.md",
        "agent_b.md",
        "agent_b.lock.yml",
    ]
    assert has_agentic_workflow(files) is True