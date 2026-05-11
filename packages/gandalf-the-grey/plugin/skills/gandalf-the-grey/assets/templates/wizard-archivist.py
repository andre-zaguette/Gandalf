#!/usr/bin/env python3
import os
import sys
import json
import re
from pathlib import Path

_STDLIB_MODULES = getattr(sys, "stdlib_module_names", frozenset({
    "abc", "ast", "asyncio", "builtins", "collections", "contextlib",
    "copy", "dataclasses", "datetime", "decimal", "email", "enum",
    "functools", "gc", "glob", "hashlib", "http", "importlib", "inspect",
    "io", "itertools", "json", "logging", "math", "multiprocessing",
    "operator", "os", "pathlib", "pickle", "platform", "pprint",
    "queue", "re", "shutil", "signal", "socket", "sqlite3", "ssl",
    "stat", "string", "subprocess", "sys", "tempfile", "threading",
    "time", "traceback", "typing", "unittest", "urllib", "uuid",
    "warnings", "weakref", "xml", "zipfile", "zlib",
}))

class WizardArchivist:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir).resolve()
        self.archive_dir = self.root_dir / "docs" / "archive"
        self.ignore_dirs = {".git", "node_modules", "__pycache__", "venv", ".venv", "dist", "build", ".gemini"}
        self.map_data = {
            "project_name": self.root_dir.name,
            "tree": {},
            "dependencies": {},
            "god_nodes": [],
            "summary": {}
        }

    def should_ignore(self, path):
        return any(part in self.ignore_dirs for part in path.parts)

    def scan(self):
        print(f"🧙 Mapping the Realm: {self.root_dir}")
        for root, dirs, files in os.walk(self.root_dir):
            rel_root = Path(root).relative_to(self.root_dir)
            if self.should_ignore(rel_root):
                continue

            self.map_data["tree"][str(rel_root)] = files
            
            for file in files:
                if file.endswith((".py", ".js", ".ts", ".tsx", ".go", ".java")):
                    self.analyze_file(rel_root / file)

        self.identify_god_nodes()
        self.generate_reports()

    def analyze_file(self, rel_path):
        full_path = self.root_dir / rel_path
        try:
            content = full_path.read_text(errors="ignore")
            # Import detection: capture module name only (not the imported symbol)
            raw = re.findall(
                r'^from\s+([\w.\-/@]+)\s+import|^import\s+([\w.\-/@]+)',
                content, re.M
            )
            imports = [a or b for a, b in raw if a or b]
            if imports:
                self.map_data["dependencies"][str(rel_path)] = list(set(imports))
            
            # Signature extraction (Classes and Functions)
            signatures = []
            # Python
            signatures.extend(re.findall(r'^\s*(class\s+\w+.*:)', content, re.M))
            signatures.extend(re.findall(r'^\s*(def\s+\w+\(.*\).*):', content, re.M))
            # JS/TS
            signatures.extend(re.findall(r'^\s*(export\s+)?(class\s+\w+.*)\s*\{', content, re.M))
            signatures.extend(re.findall(r'^\s*(export\s+)?(function\s+\w+\(.*\).*)[\s\{]', content, re.M))
            signatures.extend(re.findall(r'^\s*(const|let|var)\s+(\w+)\s*=\s*\(.*\)\s*=>', content, re.M))

            if signatures:
                self.map_data["summary"][str(rel_path)] = [str(s) for s in signatures[:15]]
        except Exception as e:
            print(f"⚠️ Could not read {rel_path}: {e}")

    def identify_god_nodes(self):
        # Files that are imported most frequently or have many lines
        import_counts = {}
        for deps in self.map_data["dependencies"].values():
            for d in deps:
                import_counts[d] = import_counts.get(d, 0) + 1
        
        # Sort and take top 5, excluding stdlib modules
        sorted_nodes = sorted(
            [(k, v) for k, v in import_counts.items() if k not in _STDLIB_MODULES],
            key=lambda x: x[1], reverse=True,
        )
        self.map_data["god_nodes"] = [node[0] for node in sorted_nodes[:5]]

    def generate_reports(self):
        self.archive_dir.mkdir(parents=True, exist_ok=True)
        
        # PALANTIR.md (Human/Agent readable)
        palantir_path = self.archive_dir / "PALANTIR.md"
        with open(palantir_path, "w") as f:
            f.write(f"# The Palantír Map: {self.map_data['project_name']}\n\n")
            f.write("## 🏰 Citadel Pillars (God Nodes)\n")
            f.write("These files are central to the realm's architecture:\n")
            for node in self.map_data["god_nodes"]:
                f.write(f"- `{node}`\n")
            
            f.write("\n## 🗺️ Territory Map\n")
            for path, files in sorted(self.map_data["tree"].items()):
                if path == ".":
                    f.write(f"- **Root**: {', '.join(files)}\n")
                else:
                    indent = "  " * path.count(os.sep)
                    f.write(f"{indent}- **{path}/**: {', '.join(files[:10])}{'...' if len(files) > 10 else ''}\n")

            f.write("\n## ⛓️ Ley Lines (Dependencies)\n")
            for file, deps in list(self.map_data["dependencies"].items())[:20]:
                f.write(f"- `{file}` depends on: {', '.join(deps[:5])}{'...' if len(deps) > 5 else ''}\n")

            f.write("\n## 📜 Rune Signatures (APIs)\n")
            for file, sigs in list(self.map_data["summary"].items())[:30]:
                f.write(f"### `{file}`\n")
                for sig in sigs:
                    f.write(f"- `{sig}`\n")
                f.write("\n")

        # MAP.json (Structured)
        with open(self.archive_dir / "MAP.json", "w") as f:
            json.dump(self.map_data, f, indent=2)

        print(f"✅ Archive complete. Consult the Palantír at {palantir_path}")

if __name__ == "__main__":
    import sys
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    archivist = WizardArchivist(root)
    archivist.scan()
