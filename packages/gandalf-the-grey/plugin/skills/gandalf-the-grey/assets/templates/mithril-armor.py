#!/usr/bin/env python3
import os
import re

# Mithril Armor: Simple Secret & Safety Scanner
SHADOW_PATTERNS = [
    r'(?i)api_key.*=.*[\'"][a-zA-Z0-9]{20,}[\'"]',
    r'(?i)password.*=.*[\'"][a-zA-Z0-9]{8,}[\'"]',
    r'(?i)secret.*=.*[\'"][a-zA-Z0-9]{20,}[\'"]',
    r'eval\(',
    r'exec\('
]

def scan_for_shadows(directory="."):
    print("🛡️ Mithril Armor: Scanning for Shadows (Secrets & Vulnerabilities)...")
    found_issues = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".py", ".js", ".ts", ".env", ".yml", ".yaml")):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', errors='ignore') as f:
                        content = f.read()
                        for pattern in SHADOW_PATTERNS:
                            if re.search(pattern, content):
                                print(f"🔥 SHADOW DETECTED in {path}: Match found for pattern {pattern}")
                                found_issues += 1
                except:
                    pass
    
    if found_issues > 0:
        print(f"\n❌ {found_issues} shadows found. Your armor is breached. Fix them!")
        return False
    
    print("✨ No shadows found. Your quest is shielded.")
    return True

if __name__ == "__main__":
    import sys
    if not scan_for_shadows():
        sys.exit(1)
