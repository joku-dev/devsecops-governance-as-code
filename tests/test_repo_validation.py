from pathlib import Path
import json
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]


class RepoValidationTests(unittest.TestCase):
    def test_validator_passes(self):
        result = subprocess.run(
            ["python3", str(ROOT / "scripts" / "validate_governance_repo.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        self.assertIn("Validation passed", result.stdout)

    def test_opa_check_passes(self):
        result = subprocess.run(
            ["opa", "check", str(ROOT / "policies" / "opa")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)

    def test_branch_protection_policy_allows_example_input(self):
        result = subprocess.run(
            [
                "opa",
                "eval",
                "-f",
                "json",
                "-d",
                str(ROOT / "policies" / "opa"),
                "-i",
                str(ROOT / "policies" / "example-input.release-candidate.json"),
                "data.devsecops.branch_protection.deny",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["result"][0]["expressions"][0]["value"], [])


if __name__ == "__main__":
    unittest.main()
