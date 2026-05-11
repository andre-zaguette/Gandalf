#!/usr/bin/env python3
import sys

# Rubrica de Qualidade do Mago
RUBRIC = {
    "1. Map the Quest": "Objetivo claro e contexto validado?",
    "2. Proof Before Alloy": "TDD/Testes implementados e passando?",
    "3. Surgical Runes": "Mudança mínima e estilo respeitado?",
    "4. SOLID Principles": "Responsabilidades claras e sem acoplamento?",
    "5. The Red Book": "Lições aprendidas foram registradas se necessário?"
}

def self_audit():
    print("✨ The Mirror of Galadriel: Reflecting upon your work...")
    score = 0
    total = len(RUBRIC)
    
    for key, desc in RUBRIC.items():
        print(f"\n[ ] {key}: {desc}")
        val = input("Grade (1-5): ")
        try:
            score += int(val)
        except:
            pass
            
    final_score = (score / (total * 5)) * 100
    print(f"\n📊 Final Alignment: {final_score:.1f}%")
    
    if final_score < 80:
        print("⚠️ The Mirror shows shadows. Refactor before you commit.")
        sys.exit(1)
    else:
        print("✅ The work is pure. Pass, Wizard.")
        sys.exit(0)

if __name__ == "__main__":
    self_audit()
