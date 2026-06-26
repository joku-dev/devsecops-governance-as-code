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

    def test_traceability_csv_includes_authority_documents(self):
        result = subprocess.run(
            ["python3", str(ROOT / "scripts" / "generate_traceability_csv.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        csv_path = ROOT / "generated" / "xlsx" / "traceability_matrix.csv"
        content = csv_path.read_text(encoding="utf-8")
        self.assertIn("authority_documents", content.splitlines()[0])
        self.assertIn("DEVSECOPS-POL-001", content)

    def test_document_control_matrix_is_generated(self):
        result = subprocess.run(
            ["python3", str(ROOT / "scripts" / "generate_document_control_matrix.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        csv_path = ROOT / "generated" / "xlsx" / "document_control_matrix.csv"
        md_path = ROOT / "generated" / "reports" / "document-control-matrix.md"
        self.assertTrue(csv_path.exists())
        self.assertTrue(md_path.exists())
        self.assertIn("document_id", csv_path.read_text(encoding="utf-8").splitlines()[0])
        self.assertIn("DEVSECOPS-DIR-001", md_path.read_text(encoding="utf-8"))

    def test_open_gap_report_is_generated(self):
        result = subprocess.run(
            ["python3", str(ROOT / "scripts" / "generate_open_gap_report.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        csv_path = ROOT / "generated" / "xlsx" / "open_gap_report.csv"
        md_path = ROOT / "generated" / "reports" / "open-gap-report.md"
        self.assertTrue(csv_path.exists())
        self.assertTrue(md_path.exists())
        self.assertIn("gap_id", csv_path.read_text(encoding="utf-8").splitlines()[0])
        self.assertIn("GAP-DOC-DEVSECOPS-POL-001", md_path.read_text(encoding="utf-8"))

    def test_governance_documents_are_rendered(self):
        result = subprocess.run(
            ["python3", str(ROOT / "scripts" / "render_governance_documents.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        policy_md = ROOT / "generated" / "documents" / "devsecops-pol-001.rendered.md"
        policy_html = ROOT / "generated" / "documents" / "devsecops-pol-001.html"
        directive_md = ROOT / "generated" / "documents" / "devsecops-dir-001.rendered.md"
        directive_html = ROOT / "generated" / "documents" / "devsecops-dir-001.html"
        self.assertTrue(policy_md.exists())
        self.assertTrue(policy_html.exists())
        self.assertTrue(directive_md.exists())
        self.assertTrue(directive_html.exists())
        self.assertIn("Document ID: `DEVSECOPS-POL-001`", policy_md.read_text(encoding="utf-8"))
        self.assertIn("<html", policy_html.read_text(encoding="utf-8"))

    def test_status_viewer_is_generated(self):
        subprocess.run(
            ["python3", str(ROOT / "scripts" / "generate_traceability_csv.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        subprocess.run(
            ["python3", str(ROOT / "scripts" / "generate_document_control_matrix.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        subprocess.run(
            ["python3", str(ROOT / "scripts" / "generate_open_gap_report.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        subprocess.run(
            ["python3", str(ROOT / "scripts" / "render_governance_documents.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        result = subprocess.run(
            ["python3", str(ROOT / "scripts" / "generate_status_viewer.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        viewer = ROOT / "generated" / "viewer" / "status-viewer.html"
        self.assertTrue(viewer.exists())
        content = viewer.read_text(encoding="utf-8")
        self.assertIn("Governance Status Viewer", content)
        self.assertIn("Open Gap Report", content)

    def test_demo_run_succeeds(self):
        result = subprocess.run(
            ["python3", str(ROOT / "scripts" / "run_demo.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        overview = ROOT / "generated" / "demo" / "demo-run.md"
        green = ROOT / "generated" / "demo" / "green-summary.json"
        red = ROOT / "generated" / "demo" / "red-summary.json"
        self.assertTrue(overview.exists())
        self.assertTrue(green.exists())
        self.assertTrue(red.exists())
        self.assertIn("Governance Demo Run", overview.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
