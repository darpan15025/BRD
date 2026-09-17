#!/usr/bin/env python3
"""Generate PDF from the LIT BRD Markdown file."""

import re
from pathlib import Path

from fpdf import FPDF

DOCS_DIR = Path(__file__).parent
MD_FILE = DOCS_DIR / "LIT-Live-Internet-TV-Business-Requirements-Document.md"
PDF_FILE = DOCS_DIR / "LIT-Live-Internet-TV-Business-Requirements-Document.pdf"

SKIP_SECTIONS = {"Table of Contents", "Document Approval"}


class BRDPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(120, 120, 120)
        self.cell(self.epw, 6, "Tata Play Fiber | LIT - Live Internet TV | BRD v1.2", align="C")
        self.ln(8)

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, f"Page {self.page_no()}", align="C")

    def section_title(self, title: str):
        if self.get_y() > 250:
            self.add_page()
        self.ln(2)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(30, 30, 30)
        self.multi_cell(self.epw, 6, sanitize(title))
        self.ln(1)

    def sub_title(self, title: str):
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(50, 50, 50)
        self.multi_cell(self.epw, 5, sanitize(title))
        self.ln(1)

    def body(self, text: str, bold: bool = False):
        self.set_font("Helvetica", "B" if bold else "", 8)
        self.set_text_color(30, 30, 30)
        self.multi_cell(self.epw, 4.5, sanitize(text))

    def bullet(self, text: str):
        self.body(f"  - {text}")


def sanitize(text: str) -> str:
    replacements = {
        "\u2014": "-", "\u2013": "-", "\u2018": "'", "\u2019": "'",
        "\u201c": '"', "\u201d": '"', "\u2192": "->", "\u2190": "<-",
        "\u2022": "-", "\u20b9": "Rs.", "\u00a0": " ",
        "\u2705": "[Yes]", "\u274c": "[No]", "\u26a0\ufe0f": "[!]", "\u2753": "[?]",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    text = re.sub(r"```[\s\S]*?```", "[diagram omitted]", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    return text.encode("latin-1", errors="replace").decode("latin-1")


def parse_table_row(line: str) -> str | None:
    if not line.strip().startswith("|"):
        return None
    if re.match(r"^\|[\s\-:|]+\|$", line.strip()):
        return None
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return " | ".join(cells)


def parse_markdown(md_text: str) -> list[tuple[str, list[str]]]:
    sections: list[tuple[str, list[str]]] = []
    current_title = None
    current_lines: list[str] = []
    in_code = False

    for line in md_text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue

        if line.startswith("## ") and not line.startswith("### "):
            if current_title:
                sections.append((current_title, current_lines))
            current_title = line[3:].strip()
            current_lines = []
            continue

        if not current_title or current_title.startswith("Tata Play Fiber"):
            continue

        if line.strip() == "---":
            continue

        if line.startswith("### "):
            current_lines.append(f"SUB:{line[4:].strip()}")
        elif line.startswith("#### "):
            current_lines.append(f"SUB:{line[5:].strip()}")
        elif line.startswith("- "):
            current_lines.append(f"BUL:{line[2:].strip()}")
        elif line.startswith("|"):
            row = parse_table_row(line)
            if row:
                current_lines.append(f"TBL:{row}")
        elif line.strip() and not line.startswith("#") and not line.strip().startswith("*End"):
            current_lines.append(f"TXT:{line.strip()}")

    if current_title:
        sections.append((current_title, current_lines))
    return sections


def build_pdf():
    pdf = BRDPDF(orientation="P", unit="mm", format="A4")
    pdf.set_margins(15, 15, 15)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 15)
    pdf.multi_cell(pdf.epw, 8, sanitize("Business Requirements Document (BRD)"))
    pdf.set_font("Helvetica", "B", 11)
    pdf.multi_cell(pdf.epw, 6, sanitize("Tata Play Fiber - LIT (Live Internet TV) - Manage LIT Module"))
    pdf.set_font("Helvetica", "", 9)
    pdf.multi_cell(pdf.epw, 5, sanitize("Version 1.2 | September 17, 2026 | Draft"))
    pdf.ln(2)

    sections = parse_markdown(MD_FILE.read_text(encoding="utf-8"))
    for title, lines in sections:
        if title in SKIP_SECTIONS:
            continue
        pdf.section_title(title)
        for item in lines:
            if item.startswith("SUB:"):
                pdf.sub_title(item[4:])
            elif item.startswith("BUL:"):
                pdf.bullet(item[4:])
            elif item.startswith("TBL:"):
                pdf.body(item[4:])
            elif item.startswith("TXT:"):
                pdf.body(item[4:])

    pdf.output(str(PDF_FILE))
    print(f"PDF generated: {PDF_FILE} ({PDF_FILE.stat().st_size} bytes)")


if __name__ == "__main__":
    build_pdf()
