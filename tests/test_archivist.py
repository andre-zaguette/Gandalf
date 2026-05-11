#!/usr/bin/env python3
"""Regression tests for WizardArchivist."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

_TEMPLATE = (
    Path(__file__).parent.parent
    / "packages/gandalf-the-grey/core/assets/templates/wizard-archivist.py"
)
_spec = importlib.util.spec_from_file_location("wizard_archivist", _TEMPLATE)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
WizardArchivist = _mod.WizardArchivist


class TestShouldIgnore(unittest.TestCase):
    def setUp(self):
        self.a = WizardArchivist(".")

    def test_ignores_git(self):
        self.assertTrue(self.a.should_ignore(Path(".git/config")))

    def test_ignores_node_modules(self):
        self.assertTrue(self.a.should_ignore(Path("node_modules/lodash/index.js")))

    def test_ignores_pycache(self):
        self.assertTrue(self.a.should_ignore(Path("src/__pycache__/foo.pyc")))

    def test_does_not_ignore_src(self):
        self.assertFalse(self.a.should_ignore(Path("src/main.py")))

    def test_does_not_ignore_docs(self):
        self.assertFalse(self.a.should_ignore(Path("docs/archive/PALANTIR.md")))


class TestAnalyzeFile(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.a = WizardArchivist(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def _write(self, name, content):
        p = self.root / name
        p.write_text(content)
        return Path(name)

    def test_python_class_and_def_extracted(self):
        rel = self._write("main.py", "class Foo:\n    pass\ndef bar(x):\n    return x\n")
        self.a.analyze_file(rel)
        sigs = self.a.map_data["summary"].get("main.py", [])
        self.assertTrue(any("class Foo" in s for s in sigs))
        self.assertTrue(any("def bar" in s for s in sigs))

    def test_python_imports_captured_module_not_name(self):
        """from pathlib import Path must capture 'pathlib', not 'Path'."""
        rel = self._write("svc.py", "import os\nfrom pathlib import Path\nimport json\n")
        self.a.analyze_file(rel)
        deps = self.a.map_data["dependencies"].get("svc.py", [])
        self.assertIn("os", deps)
        self.assertIn("pathlib", deps)
        self.assertIn("json", deps)
        self.assertNotIn("Path", deps)

    def test_file_with_no_signatures_not_in_summary(self):
        rel = self._write("constants.py", "X = 42\nY = 'hello'\n")
        self.a.analyze_file(rel)
        self.assertNotIn("constants.py", self.a.map_data["summary"])

    def test_js_export_function_extracted(self):
        rel = self._write("utils.js", "export function greet(name) {\n  return `Hi ${name}`;\n}\n")
        self.a.analyze_file(rel)
        sigs = self.a.map_data["summary"].get("utils.js", [])
        self.assertTrue(any("greet" in str(s) for s in sigs))

    def test_unreadable_path_does_not_raise(self):
        try:
            self.a.analyze_file(Path("nonexistent_file.py"))
        except Exception as e:
            self.fail(f"analyze_file raised unexpectedly: {e}")


class TestIdentifyGodNodes(unittest.TestCase):
    def setUp(self):
        self.a = WizardArchivist(".")

    def test_most_imported_is_first(self):
        self.a.map_data["dependencies"] = {
            "a.py": ["requests", "utils"],
            "b.py": ["requests", "utils"],
            "c.py": ["requests"],
            "d.py": ["flask"],
        }
        self.a.identify_god_nodes()
        nodes = self.a.map_data["god_nodes"]
        self.assertIn("requests", nodes)
        self.assertEqual(nodes[0], "requests")

    def test_at_most_five_returned(self):
        self.a.map_data["dependencies"] = {
            f"f{i}.py": [f"lib{j}" for j in range(i, i + 4)] for i in range(10)
        }
        self.a.identify_god_nodes()
        self.assertLessEqual(len(self.a.map_data["god_nodes"]), 5)

    def test_stdlib_excluded(self):
        """Regression: sys, os, re, pathlib, json must never appear as God Nodes."""
        self.a.map_data["dependencies"] = {
            "a.py": ["sys", "os", "re", "pathlib", "json"],
            "b.py": ["sys", "os", "re"],
            "c.py": ["mylib"],
        }
        self.a.identify_god_nodes()
        nodes = self.a.map_data["god_nodes"]
        for name in ("sys", "os", "re", "pathlib", "json", "Path"):
            self.assertNotIn(name, nodes, f"stdlib '{name}' must not be a God Node")


class TestGenerateReports(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.a = WizardArchivist(self._tmp.name)
        self.a.map_data = {
            "project_name": "TestRealm",
            "tree": {".": ["main.py"]},
            "dependencies": {"main.py": ["requests"]},
            "god_nodes": ["requests"],
            "summary": {"main.py": ["def run()"]},
        }

    def tearDown(self):
        self._tmp.cleanup()

    def test_palantir_created(self):
        self.a.generate_reports()
        self.assertTrue((self.root / "docs/archive/PALANTIR.md").exists())

    def test_map_json_created(self):
        self.a.generate_reports()
        self.assertTrue((self.root / "docs/archive/MAP.json").exists())

    def test_palantir_has_all_sections(self):
        self.a.generate_reports()
        content = (self.root / "docs/archive/PALANTIR.md").read_text()
        for section in ("Citadel Pillars", "Territory Map", "Ley Lines", "Rune Signatures"):
            self.assertIn(section, content)

    def test_map_json_valid_and_has_required_keys(self):
        self.a.generate_reports()
        data = json.loads((self.root / "docs/archive/MAP.json").read_text())
        for key in ("project_name", "tree", "dependencies", "god_nodes", "summary"):
            self.assertIn(key, data)
        self.assertEqual(data["project_name"], "TestRealm")


class TestScanIntegration(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        root = Path(self._tmp.name)
        (root / "src").mkdir()
        (root / "src/app.py").write_text(
            "import os\nfrom pathlib import Path\n\nclass App:\n    pass\n\ndef run():\n    pass\n"
        )
        (root / "src/utils.py").write_text("import os\n\ndef helper(): pass\n")
        (root / ".git").mkdir()
        (root / ".git/HEAD").write_text("ref: refs/heads/main\n")

    def tearDown(self):
        self._tmp.cleanup()

    def test_tree_populated(self):
        a = WizardArchivist(self._tmp.name)
        a.scan()
        self.assertTrue(any("src" in k for k in a.map_data["tree"]))

    def test_git_dir_skipped(self):
        a = WizardArchivist(self._tmp.name)
        a.scan()
        self.assertFalse(any(".git" in k for k in a.map_data["tree"]))

    def test_signatures_extracted(self):
        a = WizardArchivist(self._tmp.name)
        a.scan()
        all_sigs = str(a.map_data["summary"])
        self.assertIn("class App", all_sigs)
        self.assertIn("def run", all_sigs)

    def test_output_files_created(self):
        a = WizardArchivist(self._tmp.name)
        a.scan()
        root = Path(self._tmp.name)
        self.assertTrue((root / "docs/archive/PALANTIR.md").exists())
        self.assertTrue((root / "docs/archive/MAP.json").exists())

    def test_god_nodes_exclude_stdlib(self):
        a = WizardArchivist(self._tmp.name)
        a.scan()
        nodes = a.map_data["god_nodes"]
        for name in ("sys", "os", "re", "pathlib", "json", "Path"):
            self.assertNotIn(name, nodes, f"stdlib '{name}' must not be a God Node")


if __name__ == "__main__":
    unittest.main(verbosity=2)
