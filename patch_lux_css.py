import re

with open("css/style.css", "r", encoding="utf-8") as f:
    text = f.read()

# Enhance button
btn_css = """
.btn-primary {
    background-color: var(--primary-gold);
    color: var(--primary-dark);
    letter-spacing: 3px;
    padding: 18px 48px;
    font-size: 0.85rem;
    border: none;
    box-shadow: 0 4px 20px rgba(201,168,76,0.2);
}

.btn-secondary {
    background-color: transparent;
    color: var(--text-light);
    border: 1px solid rgba(245,240,232,0.4);
    letter-spacing: 3px;
    padding: 18px 48px;
    font-size: 0.85rem;
}
.btn-secondary:hover {
    border-color: var(--primary-gold);
    color: var(--primary-gold);
    background: rgba(201,168,76,0.05);
}
"""
text = re.sub(r'\.btn-primary \{.*?\color: var\(--primary-dark\);\n\}', btn_css, text, flags=re.DOTALL)

# Refine nav spacing
text = text.replace('gap: 40px;', 'gap: 50px;')
text = text.replace('font-size: 0.88rem;', 'font-size: 0.8rem; text-transform: uppercase; letter-spacing: 2px;')

# Enhance hero label
text = text.replace('letter-spacing: 5px;', 'letter-spacing: 8px;')

# Write back
with open("css/style.css", "w", encoding="utf-8") as f:
    f.write(text)
