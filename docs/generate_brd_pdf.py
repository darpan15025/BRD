#!/usr/bin/env python3
"""Generate PDF from the LIT BRD Markdown file."""

from pathlib import Path

from fpdf import FPDF

DOCS_DIR = Path(__file__).parent
MD_FILE = DOCS_DIR / "LIT-Live-Internet-TV-Business-Requirements-Document.md"
PDF_FILE = DOCS_DIR / "LIT-Live-Internet-TV-Business-Requirements-Document.pdf"


class BRDPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(100, 100, 100)
        self.cell(self.epw, 8, "Tata Play Fiber | LIT - Live Internet TV | BRD", align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def section_title(self, title: str):
        self.ln(4)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(30, 30, 30)
        self.multi_cell(self.epw, 8, title)
        self.ln(2)

    def sub_title(self, title: str):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(50, 50, 50)
        self.multi_cell(self.epw, 7, title)
        self.ln(1)

    def body_text(self, text: str):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(self.epw, 5, text)
        self.ln(1)

    def bullet(self, text: str):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(self.epw, 5, f"  - {text}")


def sanitize(text: str) -> str:
    replacements = {
        "\u2014": "-",
        "\u2013": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2192": "->",
        "\u2190": "<-",
        "\u2022": "-",
        "\u20b9": "Rs.",
        "\u00a0": " ",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    return text.encode("latin-1", errors="replace").decode("latin-1")


def build_pdf():
    pdf = BRDPDF(orientation="P", unit="mm", format="A4")
    pdf.set_margins(20, 20, 20)
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(20, 20, 20)
    pdf.multi_cell(pdf.epw, 9, sanitize("Business Requirements Document (BRD)"))
    pdf.set_font("Helvetica", "B", 12)
    pdf.multi_cell(pdf.epw, 7, sanitize("Tata Play Fiber Mobile Application (MAPP)"))
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(pdf.epw, 6, sanitize("Feature: LIT - Live Internet TV | Manage LIT Module"))
    pdf.ln(4)

    meta = [
        "Document Version: 1.1",
        "Date: September 17, 2026",
        "Status: Draft",
        "Design Reference: FigJam - Login Revamp (Manage LIT section)",
        "Design URL: https://www.figma.com/board/psByt5QSY6vvmuAOmExFz7/Login-Revamp?node-id=0-1",
    ]
    for line in meta:
        pdf.body_text(sanitize(line))

    sections = [
        (
            "1. Executive Summary",
            [
                "Tata Play Fiber (TPF) is introducing LIT (Live Internet TV) as an add-on service within the Tata Play Fiber Mobile Application (MAPP).",
                "This BRD defines business, functional, integration, and UI requirements for the Manage LIT module, enabling existing Fiber + LIT subscribers to change or cancel their LIT plan.",
                "Manage LIT is accessed from the Home screen Quick Actions via the Manage live TV tile (marked New).",
                "The solution coordinates MAPP (frontend), HOBS (order orchestration), and the LIT platform (subscription lifecycle, pricing, proration).",
            ],
        ),
        (
            "2. Scope - Manage LIT Module",
            [
                "In Scope: LIT plan change (upgrade, downgrade, swap), LIT cancellation, channel/language selection, plan summary and payment, cancellation confirmation and success states.",
                "Out of Scope for this module: LIT first-time purchase, recharge + LIT add-on, fiber plan change, purchase nudges (covered in separate journeys).",
            ],
        ),
        (
            "3. Manage LIT User Flows (from Design)",
            [
                "Flow A - Change Plan: Home -> Manage live TV -> Action selector -> Manage Plan overview -> Language selection -> Channel browse -> Plan details -> Summary -> Payment.",
                "Flow B - Cancel Plan: Home -> Manage live TV -> Action selector -> Cancel confirmation modal -> Success confirmation.",
            ],
        ),
        (
            "4. Screen Inventory",
            [
                "SCR-01 Home Screen with Manage live TV quick action (New badge).",
                "SCR-02 Action Selector bottom sheet: Cancel plan / Change plan options.",
                "SCR-03 Manage Plan Overview: current plan (price, 130 TV channels, add-ons), Your Channels, genre categories, Change Plan CTA.",
                "SCR-04 Language Selection: multi-select language grid (English, Hindi, Marathi, Telugu, Tamil, Kannada, Malayalam, Bengali, etc.).",
                "SCR-05 Your Channels: searchable channel list with language filter chips and genre categories.",
                "SCR-06 Plan Details: recommended plan card with channel count, price, genre tags, Confirm and Proceed CTA.",
                "SCR-07 Summary (collapsed/expanded): LIT pack details, edit (pencil) and remove (trash) actions, Proceed to pay CTA.",
                "SCR-08 Cancel Confirmation: sad face icon, warning copy, Yes Cancel My Plan / I Don't Want to Cancel.",
                "SCR-09 Cancel Success: green checkmark, Plan cancelled successfully message.",
            ],
        ),
        (
            "5. Functional Requirements - Manage LIT",
            [
                "FR-M1: MAPP shall display Manage live TV quick action on Home for Fiber + LIT subscribers.",
                "FR-M2: Tapping Manage live TV shall present action selector with Change plan and Cancel plan options.",
                "FR-M3: Change plan shall invoke HOBS manage/getRedirectionUrl and redirect to LIT for plan modification.",
                "FR-M4: MAPP shall receive LIT callback and place Add/Remove order (actions I and O as applicable).",
                "FR-M5: LIT upgrade shall display prorated price and total price before payment.",
                "FR-M6: LIT downgrade shall process instantly; FDO is not applicable.",
                "FR-M7: Cancel plan shall show confirmation with content access loss warning before submission.",
                "FR-M8: On confirm cancel, MAPP shall submit Add/Remove order with action O; entitlement suspended immediately.",
                "FR-M9: Cancel success screen shall confirm plan cancellation to the user.",
                "FR-M10: Manage Plan shall show current LIT pack details, channels, genres, and My Channels link.",
                "FR-M11: Channel search shall support filtering by language and genre within selected pack.",
                "FR-M12: Combined Fiber + LIT plan change in single transaction is NOT supported.",
            ],
        ),
        (
            "6. Business Rules",
            [
                "BR-M01: LIT validity aligns with Fiber plan validity for bundled customers.",
                "BR-M02: FDO is not applicable for LIT plan changes.",
                "BR-M03: LIT downgrade is processed instantly.",
                "BR-M04: LIT cancellation suspends entitlement immediately upon fulfillment.",
                "BR-M05: Suspended accounts cannot access MAPP or Manage LIT.",
                "BR-M06: Recharge-for-others allows Continue only; no Manage or Remove for LIT.",
                "BR-M07: Prorated pricing applies for LIT upgrade scenarios.",
            ],
        ),
        (
            "7. API Requirements",
            [
                "GET /lit/manage/getRedirectionUrl - Obtain LIT URL for manage/change plan journey.",
                "GET /lit/getSubscriberEntitlement/{subscriberId} - Fetch LIT entitlements.",
                "GET /lit/packtochannel/{packName} - Channel list for LIT pack.",
                "POST submitOrder - LIT Add/Remove orders (I/O) after LIT callback.",
                "GET getSubscriberDetails - Return LIT Subscriber ID (modified).",
                "NEW MAPP API - Receive LIT platform callback post-redirection.",
                "Base URL (UAT): https://apiuathobs.tataplayfiber.co.in",
            ],
        ),
        (
            "8. UI/UX Requirements (from FigJam Design)",
            [
                "Dark theme with deep purple headers and magenta/pink primary CTAs.",
                "Bottom sheet pattern for action selection and cancellation confirmation.",
                "Sticky footer with price summary and Proceed to pay / Change Plan CTAs.",
                "Language selection uses selectable card grid with live channel count and price calculation.",
                "Channel browse supports search, language filter chips (removable), and genre category accordion.",
                "Summary screen supports expand/collapse for pack details with edit and remove icons.",
                "Cancellation flow uses emotional design (sad face) with explicit content loss warning.",
                "Success state uses green checkmark with dimmed background overlay.",
            ],
        ),
        (
            "9. Acceptance Criteria",
            [
                "UAT Scenario 3: LIT Change Plan Only via Manage LIT journey passes end-to-end.",
                "UAT Scenario 6/10: LIT Drop/Cancellation with immediate suspension passes.",
                "UAT Scenarios 7-9: LIT Upgrade/Downgrade/Swap with correct pricing passes.",
                "UI matches FigJam Manage LIT section (Change Plan + Cancel Plan flows).",
                "All HOBS wrapper APIs return expected responses in integration testing.",
            ],
        ),
        (
            "10. Open Questions",
            [
                "Q1: Autopay - will LIT price be included in automandate file for standalone changes?",
                "Q2: Online sales journey LIT integration - pending DigiSales discussion.",
                "Q3: DigiSales Payment Link journey - pending discussion.",
                "Q4: 2-step verification (Portal) impact on Manage LIT - pending discussion.",
            ],
        ),
    ]

    for title, bullets in sections:
        pdf.section_title(sanitize(title))
        for item in bullets:
            pdf.bullet(sanitize(item))

    pdf.output(str(PDF_FILE))
    print(f"PDF generated: {PDF_FILE}")


if __name__ == "__main__":
    build_pdf()
