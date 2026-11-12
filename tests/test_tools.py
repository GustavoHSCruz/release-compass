"""Regression tests for lookup resolution and portable, non-overwriting installs."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
LOOKUP = ROOT / ".agents/skills/release-compass/scripts/lookup.py"


def run_lookup(*args, script=LOOKUP):
    return subprocess.run([sys.executable, str(script), *args], capture_output=True, text=True)


class LookupTests(unittest.TestCase):
    def test_exact_alias_overrides_full_text_matches(self):
        result = run_lookup("RC", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([t["id"] for t in json.loads(result.stdout)["terms"]], ["release-candidate"])

    def test_case_and_punctuation_normalization(self):
        result = run_lookup("bLuE green", "--format", "json")
        self.assertEqual(json.loads(result.stdout)["terms"][0]["id"], "blue-green")

    def test_comparison_keeps_distinct_dimensions(self):
        result = run_lookup("--compare", "Canary", "Nightly", "Unstable", "--format", "json")
        data = json.loads(result.stdout)
        self.assertEqual(result.returncode, 0)
        self.assertEqual([t["id"] for t in data["terms"]], ["canary", "nightly", "unstable"])
        self.assertTrue(all(t["sources"] for t in data["terms"]))

    def test_missing_comparison_is_not_silently_successful(self):
        result = run_lookup("--compare", "Canary", "unknown-channel-xyz", "--format", "json")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stdout)["missing"], ["unknown-channel-xyz"])

    def test_filter_and_empty_result(self):
        result = run_lookup("--category", "support", "--format", "json")
        self.assertTrue(all(t["category"] == "support" for t in json.loads(result.stdout)["terms"]))
        result = run_lookup("canary", "--category", "support", "--format", "json")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stdout)["count"], 0)

    def test_invalid_queries_fail(self):
        for args in [[], ["---"], ["--compare", "!!!"], ["canary", "--list"]]:
            with self.subTest(args=args):
                self.assertEqual(run_lookup(*args).returncode, 2)

    def test_unsourced_convention_is_explicit(self):
        result = run_lookup("prototype", "--format", "json")
        term = json.loads(result.stdout)["terms"][0]
        self.assertEqual(term["sources"], [])
        self.assertEqual(term["evidence"], "editorial-convention")


class InstallerTests(unittest.TestCase):
    def test_complete_copy_runs_without_the_checkout(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            installer_repo = base / "source"
            shutil.copytree(ROOT, installer_repo, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            for agent, folder in [("claude", ".claude"), ("codex", ".agents"), ("gemini", ".gemini"), ("grok", ".grok")]:
                result = subprocess.run([sys.executable, str(installer_repo / "scripts/install_skill.py"),
                                         "--agent", agent, "--project", str(base / agent)], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                skill = base / agent / folder / "skills/release-compass"
                self.assertTrue((skill / "references/workflows.md").exists())
                self.assertTrue((skill / "assets/release-policy.md").exists())
            shutil.rmtree(installer_repo)
            for agent, folder in [("claude", ".claude"), ("codex", ".agents"), ("gemini", ".gemini"), ("grok", ".grok")]:
                result = run_lookup("LTS", "--format", "json", script=base / agent / folder / "skills/release-compass/scripts/lookup.py")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(json.loads(result.stdout)["terms"][0]["id"], "lts")

    def test_dry_run_does_not_write_and_existing_files_are_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            project = Path(temp) / "project"
            command = [sys.executable, str(ROOT / "scripts/install_skill.py"), "--agent", "claude", "--project", str(project)]
            result = subprocess.run(command + ["--dry-run"], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(project.exists())
            target = project / ".claude/skills/release-compass"
            target.mkdir(parents=True)
            sentinel = target / "mine.txt"
            sentinel.write_text("keep me")
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(sentinel.read_text(), "keep me")
            self.assertFalse((target / "SKILL.md").exists())

    def test_symlinked_destination_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            project = base / "project"
            outside = base / "outside"
            project.mkdir()
            outside.mkdir()
            try:
                (project / ".claude").symlink_to(outside, target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("Symlink creation is not available")
            result = subprocess.run([sys.executable, str(ROOT / "scripts/install_skill.py"),
                                     "--agent", "claude", "--project", str(project)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(list(outside.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
