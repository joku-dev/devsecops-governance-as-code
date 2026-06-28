from pathlib import Path
import importlib.util
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "intake_github_actions_run.py"


sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("intake_github_actions_run", SCRIPT)
intake = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(intake)


class GitHubActionsRunIntakeTests(unittest.TestCase):
    def test_infers_tagged_baseline_ref(self):
        run = {
            "referenced_workflows": [
                {
                    "path": "joku-dev/devsecops-governance-as-code/.github/workflows/devsecops-baseline-l1-v1.1.3.yml@l1-baseline-v1.1.3",
                    "ref": "refs/tags/l1-baseline-v1.1.3",
                }
            ]
        }

        self.assertEqual(intake.infer_baseline_ref(run), "l1-baseline-v1.1.3")

    def test_evidence_flags_are_derived_from_governance_input(self):
        governance_input = {
            "traceability": {
                "requirements_linked": True,
                "testcases_linked": True,
                "reports_linked": True,
            },
            "static_analysis": {
                "performed": True,
            },
            "evidence": {
                "sbom": {"exists": True},
                "vulnerability_scan": {"exists": True},
            },
            "artifact": {
                "digest": {"exists": True},
            },
            "operations": {
                "deployed_versions_recorded": True,
                "security_events_recorded": True,
            },
        }

        flags = intake.evidence_flags(
            governance_input,
            {"governance-control-evaluation", "devsecops-governance-run-input"},
        )

        self.assertTrue(flags["sbom"])
        self.assertTrue(flags["vulnerability_scan"])
        self.assertTrue(flags["artifact_digest"])
        self.assertTrue(flags["governance_control_report"])
        self.assertTrue(flags["governance_run_input"])
        self.assertTrue(flags["static_analysis_summary"])
        self.assertTrue(flags["traceability_mapping"])
        self.assertTrue(flags["operations_evidence"])

    def test_find_job_status_matches_fragments(self):
        jobs = [
            {"name": "Prepare DevSecOps Evidence", "conclusion": "success"},
            {"name": "Central DevSecOps Baseline / Released DevSecOps L1 Baseline v1.1.3 / DevSecOps Baseline Gate", "conclusion": "success"},
        ]

        self.assertEqual(intake.find_job_status(jobs, "baseline", "gate"), "success")
