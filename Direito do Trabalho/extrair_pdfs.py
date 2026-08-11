import fitz
from pathlib import Path

base = Path(r"C:\Programação\hermes\PDF Revisão\Direito do Trabalho")
out = base

for pdf in sorted(base.rglob("*.pdf")):
    doc = fitz.open(pdf)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    md_name = pdf.stem + ".md"
    md_path = out / pdf.relative_to(base).parent / md_name
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(text, encoding="utf-8")
    print(f"OK: {md_path}")
