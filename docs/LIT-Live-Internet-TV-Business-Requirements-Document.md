# Business Requirements Document (BRD)

## Tata Play Fiber Mobile Application (MAPP)
### Feature: LIT — Live Internet TV (Manage LIT Module)

---

| Field | Value |
|-------|-------|
| **Document Version** | 1.2 |
| **Date** | September 17, 2026 |
| **Status** | Draft |
| **Product** | Tata Play Fiber (TPF) Mobile App |
| **Feature Name** | LIT (Live Internet TV) — Manage LIT Module |
| **Design Reference** | [Login Revamp – FigJam (Manage LIT Section)](https://www.figma.com/board/psByt5QSY6vvmuAOmExFz7/Login-Revamp?node-id=0-1) |
| **Design Scope** | Manage LIT flows only (Change Plan + Cancel Plan) |
| **Source Inputs** | MAPP Scenario Matrix (LIT Integration), FigJam Design (Manage LIT section, node 168:3578) |
| **Prepared For** | Product, Engineering (MAPP/HOBS/LIT), QA, UAT, Design |

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Background & Problem Statement](#2-background--problem-statement)
3. [Business Objectives & Success Metrics](#3-business-objectives--success-metrics)
4. [Scope](#4-scope)
5. [Stakeholders & RACI](#5-stakeholders--raci)
6. [Definitions & Acronyms](#6-definitions--acronyms)
7. [User Personas & Segments](#7-user-personas--segments)
8. [High-Level Solution Overview](#8-high-level-solution-overview)
9. [Functional Requirements](#9-functional-requirements)
10. [Manage LIT — Detailed User Journeys](#10-manage-lit--detailed-user-journeys)
11. [Screen-Level Specifications (Manage LIT)](#11-screen-level-specifications-manage-lit)
12. [Business Rules & Constraints](#12-business-rules--constraints)
13. [Pricing, Billing & Validity Logic](#13-pricing-billing--validity-logic)
14. [API & Integration Requirements](#14-api--integration-requirements)
15. [Data Fields & System Mapping](#15-data-fields--system-mapping)
16. [Error Handling & Edge Cases](#16-error-handling--edge-cases)
17. [Non-Functional Requirements](#17-non-functional-requirements)
18. [Assumptions & Dependencies](#18-assumptions--dependencies)
19. [Open Questions & Pending Decisions](#19-open-questions--pending-decisions)
20. [Out of Scope](#20-out-of-scope)
21. [Acceptance Criteria & Test Scenarios](#21-acceptance-criteria--test-scenarios)
22. [Appendix A — Full Scenario Matrix](#appendix-a--full-scenario-matrix)
23. [Appendix B — API Catalog](#appendix-b--api-catalog)
24. [Appendix C — UI Copy & Messaging Reference](#appendix-c--ui-copy--messaging-reference)

---

## 1. Executive Summary

Tata Play Fiber (TPF) is launching **LIT (Live Internet TV)** — a value-added subscription service that delivers live television channels and bundled OTT content over the internet to existing fiber broadband customers. LIT is positioned as an add-on to the core fiber plan, with subscription validity aligned to the customer's fiber plan lifecycle.

The **Manage LIT module** documented in this BRD enables existing **Fiber + LIT subscribers** to independently manage their Live Internet TV subscription within the Tata Play Fiber Mobile Application (MAPP). This includes viewing their current LIT plan details, changing their channel pack (upgrade, downgrade, or swap), browsing included channels by language and genre, reviewing pricing with proration, and cancelling their LIT subscription — all without contacting customer support.

This document serves as the single source of truth for product, design, engineering, and QA teams. It combines:

- **Business rules** from the MAPP LIT Integration Scenario Matrix (22 scenarios)
- **UI/UX specifications** from the FigJam design board (Manage LIT section — Change Plan and Cancel Plan flows)
- **Technical integration requirements** across MAPP, HOBS, and the LIT platform

The Manage LIT experience is accessed from the MAPP Home screen via a new **"Manage live TV"** quick action tile, which presents subscribers with a choice to either change their existing LIT plan or cancel it entirely.

---

## 2. Background & Problem Statement

### 2.1 Current State

Today, Tata Play Fiber customers subscribe to internet-only plans through MAPP. Live TV and OTT content are not natively manageable within the fiber app. When LIT is introduced as an add-on, subscribers who purchase it need a self-service mechanism to:

- Understand what channels and content are included in their current LIT pack
- Modify their LIT plan (add/remove languages, change channel tiers, upgrade or downgrade)
- Cancel LIT without cancelling their core fiber connection
- See transparent pricing including network fees, prorated charges, and total payable amount

### 2.2 Problem Statement

Without a dedicated Manage LIT journey in MAPP, LIT plan changes and cancellations would require:

- Contact center intervention (increasing operational cost)
- Redirection to external portals (poor customer experience)
- Manual order processing in HOBS (error-prone, slow fulfillment)

### 2.3 Proposed Solution

Integrate a **Manage LIT module** within MAPP that:

1. Surfaces LIT management from the Home screen Quick Actions
2. Presents a guided, multi-step plan change flow (language selection → channel browse → plan review → summary → payment)
3. Provides a clear, empathetic cancellation flow with explicit content-loss warnings
4. Orchestrates orders through HOBS using established Add/Remove order patterns
5. Maintains billing alignment between Fiber and LIT subscriptions

---

## 3. Business Objectives & Success Metrics

| # | Objective | Description | Success Metric | Target |
|---|-----------|-------------|----------------|--------|
| O1 | Self-service LIT management | Enable subscribers to change or cancel LIT without agent assistance | % of LIT changes completed via MAPP (vs. contact center) | ≥ 80% within 3 months of launch |
| O2 | Billing alignment | Ensure LIT validity and renewal dates stay synchronized with fiber plan | Misaligned renewal incidents | Zero tolerance |
| O3 | Reduce support load | Decrease LIT-related inbound calls and tickets | LIT support ticket volume | 30% reduction vs. baseline |
| O4 | Increase LIT engagement | Make LIT discoverable and manageable to improve retention | LIT churn rate after first 90 days | ≤ 15% monthly |
| O5 | Transparent pricing | Display itemized pricing (NCF, content cost, proration, discounts) before payment | Payment dispute rate on LIT orders | < 2% of transactions |
| O6 | Profile consistency | Keep subscriber identity synchronized across Fiber and LIT systems | Profile sync failure rate | < 0.5% |
| O7 | Fast fulfillment | Complete LIT plan changes and cancellations in real time | Order fulfillment time (P95) | < 10 seconds post-payment |

---

## 4. Scope

### 4.1 In Scope — Manage LIT Module (Primary Focus)

| Area | Description |
|------|-------------|
| **Entry Point** | "Manage live TV" quick action on MAPP Home screen with "New" badge |
| **Action Selection** | Bottom sheet offering "Change plan" and "Cancel plan" options |
| **Change Plan Flow** | Full journey: Manage Plan overview → Language selection → Channel browse → Plan review → Summary → Payment |
| **Cancel Plan Flow** | Confirmation bottom sheet → Success state with entitlement suspension |
| **Plan Display** | Current LIT pack details: channel count, price, duration, genres, OTT apps, add-ons |
| **Channel Discovery** | Search, language filters, genre categories, channel logo grid |
| **Pricing Display** | Monthly price, NCF breakdown, prorated amount, total payable, duration multiplier |
| **Order Placement** | HOBS Add/Remove orders (action `I` for add/change, action `O` for remove/cancel) |
| **LIT Redirection** | HOBS `manage/getRedirectionUrl` API for LIT platform handoff |
| **Callback Handling** | MAPP receives LIT selection data and triggers order submission |

### 4.2 In Scope — Supporting Backend Scenarios

| Area | Description |
|------|-------------|
| LIT first-time purchase (standalone, recharge + LIT, change plan + LIT) | Documented in scenario matrix; separate design flows |
| Fiber plan change with existing LIT | LIT remains active; validity re-aligned |
| Combined Fiber + LIT renewal pricing | `getEndUserDetails` returns bundled price |
| LIT subscriber ID in profile | `getSubscriberDetails` modification |
| RMN/email sync to LIT | Profile update propagation |
| Manage Services hub | Service promotion for non-subscribers |
| Paused/resumed fiber with LIT continuation | Prorated pricing scenario |

### 4.3 Out of Scope

See [Section 20 — Out of Scope](#20-out-of-scope).

---

## 5. Stakeholders & RACI

| Role | Name / Team | Responsibility | R | A | C | I |
|------|-------------|----------------|---|---|---|---|
| Product Owner | TPF Product | Feature prioritization, acceptance sign-off | | ✓ | | ✓ |
| MAPP Frontend | Mobile App Team | UI implementation, navigation, state management | ✓ | | ✓ | |
| MAPP Backend | Mobile API Team | Callback API, HOBS integration, order submission | ✓ | | ✓ | |
| HOBS Team | Backend Platform | Wrapper APIs, order fulfillment, entitlement sync | ✓ | ✓ | | ✓ |
| LIT Platform | LIT Team | Redirection URLs, pricing/proration, callback payload | ✓ | ✓ | | ✓ |
| Design | UX/UI Team | FigJam/Figma specs, design QA | ✓ | | ✓ | |
| QA | Quality Assurance | Test plan, UAT coordination, regression | ✓ | | | ✓ |
| DigiSales | Sales Platform | Online sales, payment link journeys (TBD) | | | ✓ | ✓ |
| Billing | Finance/Billing | Automandate, invoicing, NCF rules | | | ✓ | ✓ |
| UAT Business | Business Users | Scenario validation, sign-off | | | ✓ | ✓ |

*R = Responsible, A = Accountable, C = Consulted, I = Informed*

---

## 6. Definitions & Acronyms

| Term | Definition |
|------|------------|
| **MAPP** | Tata Play Fiber Mobile Application — the customer-facing iOS and Android app |
| **LIT** | Live Internet TV — an add-on OTT/live TV subscription service bundled with fiber |
| **HOBS** | Home Order & Billing System — central order orchestration and billing platform |
| **TPF** | Tata Play Fiber — the core fiber broadband service |
| **RMN** | Registered Mobile Number — primary contact number on the subscriber account |
| **NCF** | Network Capacity Fee — regulatory/network charge component of TV pricing (e.g., Rs 153) |
| **FDO** | Fiber Date of Operation — rules governing when a fiber plan change takes effect; **not applicable to LIT** |
| **Add/Remove Order** | HOBS order type where action `I` = Insert (add/activate) and `O` = Remove (deactivate/cancel) |
| **Change Package Order** | HOBS order for modifying the core fiber broadband plan |
| **Prorated Price** | Partial charge or credit calculated based on remaining days in the current billing cycle |
| **Modify Plan** | HOBS/LIT backend process to change an active LIT subscription to a different pack |
| **Entitlement** | The set of channels, OTT apps, and features a subscriber is authorized to access |
| **Redirection URL** | A secure, time-bound URL generated by HOBS that redirects the customer to the LIT platform |
| **Callback** | Data payload returned from LIT platform to MAPP after the customer completes selection on LIT |
| **Autopay / Automandate** | Recurring payment mandate registered for automatic fiber renewal |
| **BAU** | Business As Usual — existing flow remains unchanged |
| **Quick Action** | A tappable tile on the MAPP Home screen providing shortcut access to a feature |
| **Bottom Sheet** | A modal panel that slides up from the bottom of the screen for secondary actions |

---

## 7. User Personas & Segments

### 7.1 Primary Persona: Active LIT Subscriber (Manage LIT Target User)

| Attribute | Detail |
|-----------|--------|
| **Name** | Rajesh — The Connected Family Man |
| **Segment** | S2: Fiber + LIT |
| **Profile** | 35-year-old, suburban household, 200 Mbps fiber plan with LIT add-on |
| **Goal** | Customize TV channels to match family's language preferences (Hindi + English); occasionally upgrade for sports events |
| **Pain Points** | Cannot see which channels are included; unsure of pricing when changing plans; fears cancelling LIT will affect fiber |
| **Manage LIT Need** | View current pack, browse channels, change languages, see price before paying, cancel LIT independently |

### 7.2 Secondary Persona: Price-Conscious Downgrader

| Attribute | Detail |
|-----------|--------|
| **Name** | Priya — The Budget Optimizer |
| **Segment** | S2: Fiber + LIT |
| **Profile** | Wants to reduce monthly spend by downgrading LIT pack |
| **Goal** | Switch to a smaller channel pack with fewer languages |
| **Manage LIT Need** | Downgrade flow with instant effect (no FDO), clear new price display |

### 7.3 Customer Segments & Manage LIT Eligibility

| Segment | Description | Manage LIT Access |
|---------|-------------|-------------------|
| **S1: Fiber Only** | Active fiber, no LIT | ❌ Not eligible — sees purchase/promotion instead |
| **S2: Fiber + LIT** | Active fiber with active LIT | ✅ Full access — Change plan + Cancel plan |
| **S3: Fiber Autopay** | Fiber on autopay mandate + LIT | ✅ Full access — autopay impact TBD for LIT changes |
| **S4: Paused Fiber (Resumed)** | Fiber was paused, now resumed, LIT active | ✅ Access with prorated pricing |
| **S5: Suspended** | Account suspended, app login blocked | ❌ Not eligible — no app access |
| **S6: Recharge for Others** | Third party recharging another account | ⚠️ Limited — Continue only; no Manage/Remove |

---

## 8. High-Level Solution Overview

### 8.1 System Architecture

```
┌──────────────────────────────────────────────────────────────────────────┐
│                        TATA PLAY FIBER (MAPP)                            │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────┐  ┌─────────────┐ │
│  │ Home Screen │→ │ Manage LIT   │→ │ Plan Change │→ │  Summary &  │ │
│  │ Quick Action│  │ Action Sheet │  │   Screens   │  │   Payment   │ │
│  └─────────────┘  └──────────────┘  └─────────────┘  └──────┬──────┘ │
└───────────────────────────────────────────────────────────────┼────────┘
                                                                │
                    ┌───────────────────────────────────────────┤
                    │                                           │
                    ▼                                           ▼
         ┌─────────────────┐                       ┌─────────────────┐
         │      HOBS       │                       │  LIT Platform   │
         │  (Orchestration)│◄─────────────────────►│  (Subscription) │
         │                 │   Wrapper APIs        │                 │
         │ • getRedirection│                       │ • Plan catalog  │
         │ • submitOrder   │                       │ • Pricing/NCF   │
         │ • Entitlements  │                       │ • Proration     │
         │ • Profile sync  │                       │ • Callback      │
         └─────────────────┘                       └─────────────────┘
```

### 8.2 Manage LIT Integration Pattern

**Change Plan Flow:**
1. Customer taps "Manage live TV" on Home → MAPP shows action selector
2. Customer selects "Change plan" → MAPP calls `GET /lit/manage/getRedirectionUrl`
3. HOBS returns secure redirection URL → MAPP opens LIT platform (in-app webview or native)
4. Customer selects languages, browses channels, reviews plan on LIT/MAPP screens
5. LIT returns selection via callback → MAPP receives pack details, pricing, proration
6. Customer reviews Summary screen → taps "Proceed to pay"
7. MAPP calls `submitOrder` with Add/Remove actions (`I` for new pack, `O` for old pack)
8. HOBS fulfills order → LIT Modify Plan processed → entitlement updated
9. MAPP shows confirmation → updated plan reflected on Manage Plan overview

**Cancel Plan Flow:**
1. Customer taps "Manage live TV" → selects "Cancel plan"
2. MAPP shows cancellation confirmation bottom sheet with content-loss warning
3. Customer taps "Yes, Cancel My Plan"
4. MAPP calls `submitOrder` with Add/Remove action `O`
5. HOBS unsubscribes LIT → suspends entitlement immediately
6. MAPP shows success screen → LIT no longer visible as active service

---

## 9. Functional Requirements

### 9.1 Manage LIT — Core Requirements

| ID | Requirement | Description | Priority |
|----|-------------|-------------|----------|
| FR-M1 | Quick action visibility | MAPP shall display "Manage live TV" quick action tile on the Home screen for subscribers with an active Fiber + LIT subscription. The tile shall include a "New" badge to drive discovery. | Must Have |
| FR-M2 | Action selector | Upon tapping Manage live TV, MAPP shall present a bottom sheet with heading "What would you like to do?" and two options: "Change plan" and "Cancel plan". | Must Have |
| FR-M3 | Manage plan overview | The Manage Plan screen shall display the subscriber's current LIT pack including: monthly price, total TV channel count, add-on count (e.g., Extra box), active language selections with channel logos, and a "My Channels" deep-link. | Must Have |
| FR-M4 | Genre category display | Manage Plan shall show collapsible genre categories (Movies, Sports, News, Kids, Spiritual, TV Shows) with channel counts per category. Tapping a category shall expand to show included channels. | Must Have |
| FR-M5 | Language selection | Change plan flow shall present a multi-select language grid (English, Hindi, Marathi, Telugu, Tamil, Kannada, Malayalam, Bengali, and others). Selection shall dynamically update the channel count and price in the sticky footer. | Must Have |
| FR-M6 | Channel browse & search | Subscribers shall be able to search channels within the selected pack using a search bar ("Search channels in this pack"). Active language filters shall appear as removable chips. | Must Have |
| FR-M7 | Plan recommendation | After language/channel selection, MAPP shall display a plan recommendation card: "Here's a plan based on your selection" with channel count, monthly price, genre tags, and sample channel logos. | Must Have |
| FR-M8 | Summary & pricing | The Summary screen shall show the selected LIT pack with: label badge, channel count (e.g., 538 TV Channels), total price (e.g., ₹2382), duration breakdown (e.g., ₹397 × 6 Months), edit (pencil) and remove (trash) icons. | Must Have |
| FR-M9 | Expandable summary | Tapping the chevron-up icon on the sticky footer shall expand the summary card to show detailed specs: screen/device count, language details, OTT/genre tags, and full pricing breakdown. | Must Have |
| FR-M10 | Payment initiation | "Proceed to pay" CTA shall initiate the standard MAPP payment flow with the calculated total (including prorated charges for upgrades). | Must Have |
| FR-M11 | LIT redirection | For plan changes requiring LIT platform interaction, MAPP shall call HOBS `manage/getRedirectionUrl` and handle the secure handoff with a loading indicator. | Must Have |
| FR-M12 | Order placement | Post-selection, MAPP shall submit Add/Remove order via `submitOrder`: action `I` for new/updated LIT pack, action `O` for removed/cancelled pack. Both actions may be submitted in a single order for swap/change scenarios. | Must Have |
| FR-M13 | Proration display | For LIT upgrades, the Summary screen shall display both prorated price (for remaining cycle) and total price before payment confirmation. | Must Have |
| FR-M14 | Instant downgrade | LIT downgrades shall be processed instantly upon order fulfillment. No FDO or future-dated change is permitted. | Must Have |
| FR-M15 | Cancel confirmation | Cancel plan shall display a bottom sheet with sad face icon, heading "We're sad to see you go!", and explicit warning: "Your plan will be cancelled and you will no longer have access to your content." | Must Have |
| FR-M16 | Cancel actions | Cancel bottom sheet shall offer two buttons: primary "Yes, Cancel My Plan" (triggers order) and secondary "I Don't Want to Cancel" (dismisses sheet). | Must Have |
| FR-M17 | Cancel fulfillment | On confirmed cancellation, MAPP shall submit Add/Remove order with action `O`. HOBS shall unsubscribe LIT and suspend entitlement immediately. | Must Have |
| FR-M18 | Cancel success | After successful cancellation, MAPP shall display a success overlay with green checkmark and message "Plan cancelled successfully!" over a dimmed home screen. | Must Have |
| FR-M19 | Edit from summary | Tapping the pencil (edit) icon on the Summary screen shall navigate the customer back to plan/language selection to modify their choice. | Should Have |
| FR-M20 | Remove from summary | Tapping the trash (remove) icon on the Summary screen shall trigger the Cancel Plan confirmation flow. | Should Have |
| FR-M21 | Discovery prompt | Manage Plan overview shall show "Discover a best fit" prompt with utility icon to encourage plan exploration. | Should Have |
| FR-M22 | No combined transaction | Combined Fiber plan change + LIT plan change in a single transaction shall NOT be supported. MAPP shall enforce separate journeys. | Must Have |

### 9.2 Supporting Functional Requirements (Backend Scenarios)

| ID | Requirement | Description | Priority |
|----|-------------|-------------|----------|
| FR-1.1 | LIT purchase display | MAPP shall display LIT as an available add-on during recharge, plan change, and standalone purchase journeys for Fiber-only customers. | Must Have |
| FR-1.2 | Expiry date handoff | For standalone LIT purchase, MAPP shall send the current fiber plan expiry date to LIT for validity alignment. | Must Have |
| FR-2.1 | Fiber-only plan change | During fiber-only plan change, LIT products shall NOT be modifiable. Existing LIT remains active with validity re-aligned to new fiber plan. | Must Have |
| FR-4.1 | Combined renewal price | For same-plan renewal, `getEndUserDetails` shall return combined Fiber + LIT renewal price. | Must Have |
| FR-7.1 | Package details API | HOBS wrapper API shall provide LIT package and channel details for MAPP display. | Must Have |
| FR-7.2 | LIT subscriber ID | `getSubscriberDetails` shall return LIT Subscriber ID. | Must Have |
| FR-7.3 | Profile sync | On RMN/email update, HOBS shall propagate changes to LIT via Update Subscriber Profile API. | Must Have |
| FR-9.1 | Recharge for others | If target subscriber has LIT, recharger shall see Continue only — no Manage or Remove. | Must Have |

---

## 10. Manage LIT — Detailed User Journeys

### 10.1 Journey A: Change LIT Plan (Happy Path)

**Actor:** Rajesh (Fiber + LIT subscriber)  
**Precondition:** Active fiber plan (200 Mbps), active LIT pack (130 channels, ₹399/month), app logged in  
**Goal:** Add Tamil language channels to existing Hindi + English pack  

| Step | Screen | User Action | System Behavior | API / Backend |
|------|--------|-------------|-----------------|---------------|
| 1 | Home (SCR-M01) | Taps "Manage live TV" quick action (with "New" badge) | Navigate to action selector; fetch current LIT entitlement | `GET /lit/getSubscriberEntitlement/{id}` |
| 2 | Action Selector (SCR-M02) | Taps "Change plan" | Navigate to Manage Plan overview; load current pack details | `GET /lit/packtochannel/{packName}` |
| 3 | Manage Plan (SCR-M03) | Reviews current plan: 130 channels, ₹399/month, Hindi + English logos | Display plan card, genre categories, "Discover a best fit" | Entitlement data rendered |
| 4 | Manage Plan (SCR-M03) | Taps "Change Plan" CTA in sticky footer | Navigate to Language Selection screen | — |
| 5 | Language Selection (SCR-M04) | Selects Tamil in addition to Hindi and English | Footer updates: "534 Channels \| ₹429/month (Includes Rs 153 network fee)" | LIT pricing API (real-time calc) |
| 6 | Language Selection (SCR-M04) | Taps "Proceed" | Navigate to Your Channels browse screen | — |
| 7 | Your Channels (SCR-M05) | Searches "Star Sports", filters by Sports genre | Display matching channels; show count per genre | Channel search/filter (local + API) |
| 8 | Plan Details (SCR-M06) | Reviews recommended plan: "534 TV Channels at ₹376/month" | Show plan card with genre tags, channel icons, promo banner | LIT plan recommendation |
| 9 | Plan Details (SCR-M06) | Taps "Confirm & Proceed" | Navigate to Summary screen (collapsed view) | — |
| 10 | Summary (SCR-M07) | Reviews: 534 TV Channels, ₹2544 total, ₹424 × 6 Months | Display pack card with edit/remove icons; sticky footer shows ₹2544 + "Proceed to pay" | Pricing breakdown from LIT |
| 11 | Summary (SCR-M07) | Taps chevron-up to expand | Show specs: device count, languages, OTT tags, NCF breakdown | — |
| 12 | Summary (SCR-M07) | Taps "Proceed to pay" | Initiate MAPP payment flow | Payment gateway |
| 13 | Payment | Completes payment | MAPP submits order: Add/Remove (O for old pack, I for new pack) | `POST submitOrder` |
| 14 | Confirmation | — | HOBS fulfills → LIT Modify Plan → entitlement updated | HOBS → LIT backend |
| 15 | Manage Plan (SCR-M03) | Sees updated plan with Tamil channels | Display success state; updated channel count and logos | Refresh entitlement |

**Postcondition:** LIT pack updated to 534 channels including Tamil. Fiber plan unchanged. New validity aligned.

---

### 10.2 Journey B: Cancel LIT Plan (Happy Path)

**Actor:** Priya (Fiber + LIT subscriber)  
**Precondition:** Active fiber + LIT, wants to cancel LIT to save money  
**Goal:** Cancel LIT subscription while keeping fiber active  

| Step | Screen | User Action | System Behavior | API / Backend |
|------|--------|-------------|-----------------|---------------|
| 1 | Home (SCR-M01) | Taps "Manage live TV" | Show action selector | Fetch entitlement |
| 2 | Action Selector (SCR-M02) | Taps "Cancel plan" | Show cancellation bottom sheet over dimmed home screen | — |
| 3 | Cancel Confirmation (SCR-M10) | Reads warning about content access loss | Display sad face icon, warning copy, two CTAs | — |
| 4 | Cancel Confirmation (SCR-M10) | Taps "Yes, Cancel My Plan" | Submit cancellation order | `POST submitOrder` (action O) |
| 5 | Backend | — | HOBS unsubscribes LIT → suspends entitlement immediately | HOBS → LIT unsubscribe |
| 6 | Cancel Success (SCR-M11) | Sees "Plan cancelled successfully!" with green checkmark | Show success overlay; dimmed home background | — |
| 7 | Home (SCR-M01) | Returns to home | "Manage live TV" tile removed or changed to "Explore LIT" promotion | UI state refresh |

**Postcondition:** LIT subscription cancelled. Fiber plan remains active. LIT entitlement suspended immediately.

---

### 10.3 Journey C: LIT Upgrade with Proration

**Actor:** Rajesh  
**Precondition:** Mid-cycle on 6-month LIT pack, wants to upgrade to premium pack  
**Goal:** Upgrade LIT pack and pay only the prorated difference  

| Step | User Action | System Behavior |
|------|-------------|-----------------|
| 1 | Initiates Change plan from Manage LIT | Load current pack with remaining validity info |
| 2 | Selects premium pack with more channels | LIT returns prorated price (e.g., ₹180 for remaining 4 months) + total new pack price |
| 3 | Reviews Summary with proration line item | Display: "Prorated upgrade charge: ₹180" + "New plan total: ₹2,982" |
| 4 | Proceeds to pay | Charge prorated + any applicable taxes |
| 5 | Order fulfilled | HOBS processes LIT Modify Plan; new entitlement active immediately |

---

### 10.4 Journey D: Cancel Abandonment

**Actor:** Rajesh  
**Precondition:** Initiated cancel flow but changed mind  

| Step | User Action | System Behavior |
|------|-------------|-----------------|
| 1 | Taps "Cancel plan" from action selector | Show cancellation bottom sheet |
| 2 | Taps "I Don't Want to Cancel" | Dismiss bottom sheet; return to home screen |
| 3 | — | No order submitted; LIT remains active; no state change |

---

## 11. Screen-Level Specifications (Manage LIT)

### SCR-M01: Home Screen — Quick Action Entry

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Primary entry point for Manage LIT; surfaces the feature alongside other Quick Actions |
| **Access Condition** | Subscriber has active Fiber + LIT subscription |
| **Layout** | Standard MAPP Home with CURRENT PLAN card (speed, recharge date), Quick Actions grid (2 rows × 4 columns), bottom navigation (Home, Plans, Support, Profile) |
| **Key Elements** | Greeting ("Good Morning {Name}!"), CURRENT PLAN card (200 MBPS, Unlimited Data, Next Recharge Date, Recharge + My Offers buttons), Quick Actions section, "Manage live TV" tile with TV/router icon and **"New" badge** |
| **Tile Label** | "Manage live TV" |
| **Badge** | "New" — pink/magenta pill badge on top-right of tile |
| **Tap Action** | Navigate to Action Selector (SCR-M02) |
| **Data Required** | Subscriber ID, LIT entitlement status (active/inactive), current fiber plan summary |
| **Error State** | If entitlement fetch fails, show toast: "Unable to load your TV plan. Please try again." |

---

### SCR-M02: Action Selector (Bottom Sheet)

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Let the subscriber choose between changing or cancelling their LIT plan |
| **Layout** | Bottom sheet overlay (≈200px height) on dimmed Home screen; drag indicator at top |
| **Heading** | "What would you like to do?" |
| **Subtext** | "Manage your Live TV plan in just a few taps" |
| **Options** | Two full-width buttons stacked vertically: **"Change plan"** (primary/outline) and **"Cancel plan"** (secondary/outline) |
| **Dismiss** | Tap outside sheet, swipe down, or back gesture → return to Home |
| **Change plan action** | Navigate to Manage Plan Overview (SCR-M03) |
| **Cancel plan action** | Show Cancel Confirmation bottom sheet (SCR-M10) |

---

### SCR-M03: Manage Plan Overview

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Display the subscriber's current LIT plan with channel details and option to change |
| **Header** | Back arrow + screen title (e.g., "Manage Plan" or "Your Plan") |
| **Your Plan Card** | Section header: "Your Plan" with "My Channels" link (top-right) |
| **Plan Metrics** | Left column: channel count (e.g., "130") with label "TV Channels"; channel logo row (up to 3 logos + "+N" overflow). Right column: add-on count (e.g., "1") with label "Extra box"; add-on icon row |
| **Discovery Prompt** | Light bulb icon + "Discover a best fit" text below plan card |
| **Filter Chips** | Horizontal scrollable chips for quick filtering (e.g., language-based) |
| **Genre Categories** | Collapsible accordion rows: Movies (25 Channels), Sports (15 Channels), News (12 Channels), Kids (15 Channels), Spiritual (11 Channels) — each with chevron-right and channel count |
| **Expanded Genre** | Shows horizontal channel chip cards (medium size) with channel logo, name, and HD/SD badge |
| **Sticky Footer CTA** | Full-width magenta button: **"Change Plan"** |
| **Data Source** | `GET /lit/getSubscriberEntitlement/{id}`, `GET /lit/packtochannel/{packName}` |

---

### SCR-M04: Language Selection

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Allow subscriber to select one or more languages to customize their channel pack |
| **Header** | Back arrow + title |
| **Instruction** | "Select one or more languages & get all channels of selected languages" |
| **Language Grid** | 3-column grid of selectable cards: English, Hindi, Marathi, Telugu, Tamil, Kannada, Malayalam, Bengali, Gujarati, Punjabi, Odia, etc. Each card shows language name and icon/flag |
| **Selection State** | Selected languages show highlighted border/background; deselected show default state |
| **Sticky Footer** | Left: dynamic channel count + price (e.g., "531 Channels \| ₹399/month (Includes Rs 153 network fee)"). Right: **"Proceed"** button |
| **Real-time Update** | Channel count and price recalculate on each language toggle |
| **Validation** | At least one language must be selected to proceed |
| **Proceed Action** | Navigate to Your Channels (SCR-M05) or Plan Details (SCR-M06) |

---

### SCR-M05: Your Channels (Browse & Search)

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Let subscriber explore and search channels within their selected pack |
| **Header** | Pack name (e.g., "538 TV Channels") with validity info |
| **Search Bar** | Placeholder: "Search channels in this pack" with search/filter icon on right |
| **Filter Chips** | Active language filters as removable chips (e.g., "English ×", "Hindi ×") |
| **Genre List** | Vertical list with channel counts: TV Shows (161), Sports (25), Movies (48), News (45), Spiritual (11), Kids (15) |
| **Expand Behavior** | Tap genre row → expand to show channel list within that genre |
| **Channel Display** | Channel logo, name, language tag, HD/SD indicator |
| **Bottom Sheet (Channel Detail)** | Tapping a genre may open a bottom sheet with full channel list, search, and pricing footer |
| **Footer** | Price display + "Proceed" / "Confirm & Proceed" CTA |

---

### SCR-M06: Plan Details (Review)

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Present the recommended LIT plan based on customer's language/channel selection |
| **Heading** | "Here's a plan based on your selection" |
| **Plan Card** | Large card: "{N} TV Channels at ₹{price}/month" (e.g., "538 TV Channels at ₹346/month") |
| **Subtext** | "Includes {N} complementary channels" or similar value statement |
| **Genre Tags** | Horizontal tag row: Sports, News, TV Shows, Movies, Kids, etc. |
| **Channel Grid** | Sample channel logos (6–12 icons) representing included channels |
| **Promo Banner** | Sparkle icon + promotional text (e.g., savings or bundle offer) |
| **Sticky Footer** | Price (with discount if applicable) + **"Confirm & Proceed"** CTA |
| **CTA Action** | Navigate to Summary (SCR-M07) |

---

### SCR-M07 / SCR-M08: Summary (Collapsed & Expanded)

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Final review of selected LIT plan with pricing before payment |
| **Header** | Back arrow + "Summary" |
| **Pack Card (Collapsed)** | Label badge (pack name), channel count ("538 TV Channels"), total price ("₹2382"), duration ("₹397 × 6 Months"), edit (pencil) icon top-right, remove (trash) icon top-right, chevron-right to expand |
| **Pack Card (Expanded)** | All collapsed content plus: specs list with monitor icon (device/screen count) and globe icon (language details), OTT/genre tag row, divider lines between sections |
| **Sticky Footer** | Left section: total price ("₹2382") with chevron-up toggle. Right section: **"Proceed to pay"** button (magenta) |
| **Edit Action** | Pencil icon → navigate back to language/plan selection |
| **Remove Action** | Trash icon → trigger Cancel Plan flow (SCR-M10) |
| **Expand/Collapse** | Chevron-up on footer toggles pack card between collapsed and expanded states |
| **Pricing Breakdown (Expanded)** | Base content price, NCF (network fee), discount (if any), taxes, prorated amount (for upgrades), grand total |

---

### SCR-M09: Payment

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Standard MAPP payment flow for LIT plan change charge |
| **Content** | Reuses existing MAPP payment screen with LIT-specific line items |
| **Line Items** | LIT plan name, duration, base price, NCF, proration, taxes, total |
| **Payment Methods** | All standard MAPP payment options (UPI, cards, net banking, wallet) |
| **On Success** | Submit order → show confirmation → navigate to updated Manage Plan or Home |
| **On Failure** | Show error with retry option; do not submit order |

---

### SCR-M10: Cancel Confirmation (Bottom Sheet)

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Confirm subscriber's intent to cancel LIT with clear consequences |
| **Layout** | Bottom sheet (≈368px height) on dimmed Home screen; close (×) button at top |
| **Icon** | Sad face emoji/icon (centered) |
| **Heading** | "We're sad to see you go!" |
| **Warning Text** | "Your plan will be cancelled and you will no longer have access to your content. Are you sure you want to cancel?" |
| **Primary CTA** | **"Yes, Cancel My Plan"** — magenta filled button; triggers order submission |
| **Secondary CTA** | **"I Don't Want to Cancel"** — outline/text button; dismisses sheet |
| **Close (×)** | Same as secondary CTA — dismiss without action |
| **On Confirm** | Submit Add/Remove order (action `O`) → show success (SCR-M11) |

---

### SCR-M11: Cancel Success

| Attribute | Detail |
|-----------|--------|
| **Purpose** | Confirm successful LIT cancellation to the subscriber |
| **Layout** | Centered overlay on dimmed Home screen |
| **Icon** | Green checkmark (in confirm/success circle) |
| **Message** | "Plan cancelled successfully!" |
| **Duration** | Auto-dismiss after 3 seconds OR tap to dismiss |
| **Post-dismiss** | Home screen refreshes; "Manage live TV" tile removed or replaced with LIT promotion |

---

## 12. Business Rules & Constraints

| Rule ID | Rule | Rationale | Enforcement |
|---------|------|-----------|-------------|
| BR-01 | LIT validity shall align with fiber plan validity for bundled customers | Prevents billing discrepancies and customer confusion | HOBS validity sync on fiber renewal/change |
| BR-02 | FDO is NOT applicable for LIT plan changes | LIT changes are instant, not future-dated | MAPP shall not show FDO date picker for LIT |
| BR-03 | LIT downgrade is processed instantly | Customer expects immediate effect when reducing pack | HOBS instant fulfillment; no scheduled downgrade |
| BR-04 | Combined Fiber + LIT plan change in single transaction is prohibited | Technical limitation; separate order types | MAPP blocks LIT redirection during fiber-only plan change |
| BR-05 | Combined Fiber upgrade/downgrade + LIT upgrade/downgrade is prohibited | Prevents complex proration and order conflicts | MAPP enforces separate journeys |
| BR-06 | LIT entitlement suspension is immediate upon cancellation | Customer should not access content after cancelling | HOBS unsubscribes and suspends on fulfillment |
| BR-07 | Suspended accounts cannot access MAPP | Security and billing integrity | App login blocked; no Manage LIT access |
| BR-08 | During fiber-only plan change, LIT products cannot be modified | Avoids conflicting orders | LIT options hidden/disabled in fiber change UI |
| BR-09 | Recharge-for-others: LIT allows Continue only | Third party should not manage another's LIT | Manage and Remove actions hidden |
| BR-10 | Prorated pricing applies for LIT upgrade and paused/resumed fiber | Fair billing for mid-cycle changes | LIT platform calculates; MAPP displays |
| BR-11 | At least one language must be selected for plan change | Empty pack is invalid | Frontend validation before Proceed |
| BR-12 | Cancel requires explicit confirmation | Prevents accidental cancellation | Two-step: select Cancel → confirm Yes |

---

## 13. Pricing, Billing & Validity Logic

### 13.1 Price Components

| Component | Description | Example |
|-----------|-------------|---------|
| **Content Price** | Charge for TV channels and OTT apps in the selected pack | ₹346/month |
| **NCF (Network Capacity Fee)** | Regulatory network charge included in total | ₹153/month |
| **Total Monthly** | Content + NCF | ₹399/month (₹246 content + ₹153 NCF) |
| **Duration Multiplier** | Pack duration (1, 3, 6, 12 months) | ₹397 × 6 Months = ₹2,382 |
| **Prorated Charge** | Partial charge for upgrade mid-cycle | ₹180 for remaining 4 of 6 months |
| **Discount** | Promotional or bundle discount (if applicable) | 10% off → shown with strikethrough original price |

### 13.2 Proration Rules

| Scenario | Proration Behavior |
|----------|-------------------|
| LIT Upgrade (mid-cycle) | Customer pays difference between old and new pack for remaining days |
| LIT Downgrade (mid-cycle) | Instant switch; credit/refund policy per business decision (typically no refund for downgrade) |
| LIT Swap (same price tier) | No proration; instant pack swap |
| Paused & Resumed Fiber | LIT prorated based on fiber expiry date + total renewal amount |

### 13.3 Validity Alignment

- LIT subscription end date = Fiber plan end date (for bundled customers)
- On fiber plan change: LIT validity is re-aligned to new fiber plan end date (LIT pack itself unchanged)
- On fiber renewal: LIT renews alongside fiber (combined price from `getEndUserDetails`)
- On LIT cancellation: LIT entitlement ends immediately; fiber validity unaffected

---

## 14. API & Integration Requirements

### 14.1 HOBS LIT APIs

| API | Method | Endpoint | Request | Response | Used In |
|-----|--------|----------|---------|----------|---------|
| Manage Redirection | GET/POST | `/lit/manage/getRedirectionUrl` | `{ subscriberId, fiberExpiryDate }` | `{ redirectionUrl, sessionToken, expiry }` | Change plan (LIT handoff) |
| Subscribe Redirection | GET/POST | `/lit/subscribe/getRedirectionUrl` | `{ subscriberId, fiberExpiryDate }` | `{ redirectionUrl }` | First-time purchase (out of Manage LIT scope) |
| Subscriber Entitlement | GET | `/lit/getSubscriberEntitlement/{subscriberId}` | Path param: subscriberId | `{ litSubscriberId, packName, channelCount, price, validity, languages[], addons[] }` | Manage Plan overview |
| Pack to Channel | GET | `/lit/packtochannel/{packName}` | Path param: packName | `{ channels[{ name, logo, language, genre, hd }], genres[{ name, count }] }` | Channel browse |
| Subscriber Entitlements | GET | `/SubscriberServices/subscriberEntitlements` | `{ subscriberId }` | Combined fiber + LIT entitlements | Profile, Manage Services |
| Update Profile | POST | `/lit/lit/updateSubscriberProfile` | `{ litSubscriberId, rmn, email }` | `{ status, message }` | Profile update sync |

**Base URL (UAT):** `https://apiuathobs.tataplayfiber.co.in`

### 14.2 MAPP APIs

| API | Method | Direction | Purpose |
|-----|--------|-----------|---------|
| LIT Callback | POST | LIT → MAPP | Receive plan selection, pricing, and proration data after LIT redirection |
| Submit Order | POST | MAPP → HOBS | Place Add/Remove orders for LIT changes and cancellations |
| Get End User Details | GET | MAPP → HOBS | Fetch combined Fiber + LIT renewal pricing |
| Get Subscriber Details | GET | MAPP → HOBS | Fetch subscriber profile including LIT Subscriber ID |

### 14.3 API Sequence — Manage LIT Change Plan

```
Customer          MAPP              HOBS              LIT Platform
   │                │                  │                    │
   │──Tap Manage───►│                  │                    │
   │                │──GET entitlement─►│                    │
   │                │◄──pack details────│                    │
   │◄─Show Plan────│                  │                    │
   │                │                  │                    │
   │──Change Plan──►│                  │                    │
   │                │──GET redirect URL►│                    │
   │                │◄──URL + token─────│                    │
   │                │──Redirect────────────────────────────►│
   │◄─────────────────────────Plan selection UI─────────────│
   │──Confirm──────────────────────────────────────────────►│
   │                │◄─────────Callback (pack, price)──────│
   │◄─Show Summary─│                  │                    │
   │──Pay──────────►│                  │                    │
   │                │──POST submitOrder►│                    │
   │                │                  │──Modify Plan───────►│
   │                │                  │◄──Entitlement upd──│
   │                │◄──Order confirm───│                    │
   │◄─Success──────│                  │                    │
```

### 14.4 API Sequence — Manage LIT Cancel Plan

```
Customer          MAPP              HOBS              LIT Platform
   │                │                  │                    │
   │──Cancel Plan──►│                  │                    │
   │◄─Confirm Sheet│                  │                    │
   │──Yes Cancel───►│                  │                    │
   │                │──POST submitOrder─►│                    │
   │                │   (action: O)    │──Unsubscribe───────►│
   │                │                  │──Suspend entitlement►│
   │                │◄──Order confirm───│                    │
   │◄─Success──────│                  │                    │
```

---

## 15. Data Fields & System Mapping

### 15.1 LIT Entitlement Object (from HOBS)

| Field | Type | Description | Display Location |
|-------|------|-------------|------------------|
| `litSubscriberId` | String | Unique LIT platform subscriber identifier | Backend/profile (not shown to customer) |
| `packName` | String | Current LIT pack name (e.g., "LIT Premium 6M") | Summary label badge |
| `channelCount` | Integer | Total channels in pack (e.g., 538) | Plan card, footer |
| `monthlyPrice` | Decimal | Monthly charge including NCF (e.g., 399.00) | Plan card, footer |
| `totalPrice` | Decimal | Total for duration (e.g., 2382.00) | Summary, payment |
| `durationMonths` | Integer | Pack validity period (e.g., 6) | Duration breakdown |
| `monthlyBreakdown` | Decimal | Per-month cost (e.g., 397.00) | "₹397 × 6 Months" |
| `ncfAmount` | Decimal | Network capacity fee (e.g., 153.00) | Footer disclaimer |
| `languages` | Array | Active languages [{ code, name, icon }] | Language grid, filter chips |
| `genres` | Array | Genre categories [{ name, count }] | Genre accordion |
| `addons` | Array | Active add-ons [{ name, count }] (e.g., Extra box) | Plan card right column |
| `validityEndDate` | Date | LIT subscription end date | Manage Plan (implicit) |
| `status` | Enum | ACTIVE, SUSPENDED, CANCELLED | Determines Manage LIT visibility |

### 15.2 LIT Callback Payload (LIT → MAPP)

| Field | Type | Description |
|-------|------|-------------|
| `sessionToken` | String | Session identifier from redirection |
| `selectedPackName` | String | New pack selected by customer |
| `channelCount` | Integer | Channels in new pack |
| `monthlyPrice` | Decimal | New monthly price |
| `totalPrice` | Decimal | Total charge for duration |
| `proratedAmount` | Decimal | Prorated charge (upgrades only; 0 for downgrade/swap) |
| `durationMonths` | Integer | Selected duration |
| `languages` | Array | Selected language codes |
| `action` | Enum | CHANGE, UPGRADE, DOWNGRADE, SWAP |

### 15.3 Submit Order Payload (MAPP → HOBS)

| Field | Type | Description |
|-------|------|-------------|
| `subscriberId` | String | Fiber subscriber ID |
| `litSubscriberId` | String | LIT subscriber ID |
| `orders[]` | Array | Array of order items |
| `orders[].productType` | String | "LIT" |
| `orders[].action` | Enum | "I" (add/insert) or "O" (remove) |
| `orders[].packName` | String | LIT pack name |
| `orders[].price` | Decimal | Charge amount |
| `orders[].proratedAmount` | Decimal | Proration (if applicable) |

---

## 16. Error Handling & Edge Cases

| # | Scenario | Expected Behavior | User Message |
|---|----------|-------------------|--------------|
| E1 | HOBS entitlement API timeout | Show retry button on Manage Plan screen | "Unable to load your TV plan. Please try again." |
| E2 | LIT redirection URL failure | Block navigation; show error with retry | "Something went wrong. Please try again later." |
| E3 | LIT callback timeout (customer abandoned LIT webview) | Return to Manage Plan; no order placed | "Plan change was not completed." |
| E4 | Payment failure after plan selection | Do not submit order; return to Summary with retry | "Payment failed. Please try again." |
| E5 | Order submission failure (HOBS error) | Show error; do not charge customer | "We couldn't process your request. Please contact support." |
| E6 | Customer taps back during payment | Return to Summary; preserve selection | — |
| E7 | No languages selected on Language screen | Disable Proceed button | "Please select at least one language" |
| E8 | Suspended account attempts access | Block app login entirely | "Your account is suspended. Please contact support." |
| E9 | Fiber + LIT customer on fiber-only plan change | Hide/disable LIT options in fiber change flow | "Your TV plan will remain unchanged" (informational) |
| E10 | Network loss during order submission | Queue retry or show offline message | "No internet connection. Please check and try again." |
| E11 | Customer double-taps "Proceed to pay" | Debounce button; prevent duplicate orders | — |
| E12 | Prorated amount is ₹0 (same-price swap) | Show ₹0 proration line; charge only if price differs | "No additional charge for this change" |

---

## 17. Non-Functional Requirements

| ID | Category | Requirement | Measurement |
|----|----------|-------------|-------------|
| NFR-01 | Performance | LIT entitlement data shall load within 2 seconds on Manage Plan screen | P95 latency ≤ 2000ms |
| NFR-02 | Performance | Redirection URL shall be obtained within 3 seconds | P95 latency ≤ 3000ms |
| NFR-03 | Performance | Order submission shall complete within 5 seconds post-payment | P95 latency ≤ 5000ms |
| NFR-04 | Performance | Language selection price update shall reflect within 500ms of toggle | Client-side perceived instant |
| NFR-05 | Availability | LIT integration APIs shall maintain 99.5% uptime | Monthly uptime report |
| NFR-06 | Security | All MAPP ↔ HOBS ↔ LIT communication over TLS 1.2+ | Security audit |
| NFR-07 | Security | LIT callback shall be authenticated via session token validation | Penetration test |
| NFR-08 | Security | PII (RMN, email) shall not be logged in client-side analytics | Code review |
| NFR-09 | Audit | All LIT orders logged with subscriber ID, action, amount, timestamp, order ID | HOBS audit trail |
| NFR-10 | Compatibility | Feature supported on iOS 14+ and Android 8+ per TPF release matrix | Device testing |
| NFR-11 | Accessibility | All CTAs shall have minimum 44×44pt touch target; text contrast ratio ≥ 4.5:1 | WCAG 2.1 AA |
| NFR-12 | Localization | All user-facing strings in English; Hindi support per product roadmap | i18n review |

---

## 18. Assumptions & Dependencies

### 18.1 Assumptions

1. LIT platform is operational and provides stable redirection and callback mechanisms at launch
2. HOBS wrapper APIs will be deployed to UAT at least 2 weeks before MAPP frontend integration begins
3. Fiber plan expiry date is the authoritative source for LIT validity alignment
4. Proration logic is owned and calculated by the LIT platform; MAPP is a display layer
5. FigJam design (Manage LIT section) is approved and final for development
6. Payment gateway supports LIT-specific line items without modification
7. Channel logos and language icons are provided by LIT/Content team in required formats

### 18.2 Dependencies

| Dependency | Owner | Required By | Impact if Delayed |
|------------|-------|-------------|-------------------|
| HOBS LIT wrapper APIs (all 6 endpoints) | HOBS Team | Sprint 1 | Blocks all LIT journeys |
| LIT callback payload specification | LIT Team | Sprint 1 | Blocks order placement post-redirection |
| MAPP callback API endpoint | MAPP Backend | Sprint 2 | Blocks LIT → MAPP data handoff |
| FigJam design sign-off | Design Team | Sprint 1 | Blocks frontend development |
| Channel logo assets | Content Team | Sprint 2 | Blocks channel browse UI |
| Payment flow LIT line item support | Payment Team | Sprint 3 | Blocks end-to-end payment testing |
| DigiSales integration (if in scope) | DigiSales Team | TBD | Blocks online sales journey |
| Autopay automandate file update | Billing Team | TBD | Blocks autopay + LIT scenario |

---

## 19. Open Questions & Pending Decisions

| # | Question | Context | Owner | Status | Impact |
|---|----------|---------|-------|--------|--------|
| Q1 | How will LIT be integrated into the online sales journey? | DigiSales platform may need LIT pack selection during new fiber sale | Prasad / DigiSales | Discussion pending | Medium |
| Q2 | Will DigiSales Payment Link journey support LIT add-on? | Payment links sent via SMS/email for remote payment | Prasad / DigiSales | Discussion pending | Medium |
| Q3 | What is the impact of 2-step verification (Portal) on LIT journeys? | Portal-based verification may add a step before payment | Prasad / DigiSales | Discussion pending | Low |
| Q4 | Will LIT price be automatically included in the automandate file for autopay customers who purchase LIT standalone? | Affects recurring billing for autopay + LIT customers | Billing / Product | Open | High |
| Q5 | If LIT drop without order is allowed, should drop be available across all fiber journeys? | Affects whether Remove icon appears only in Manage LIT or everywhere | Product | Open | Medium |
| Q6 | What is the refund policy for LIT downgrade mid-cycle? | Customer downgrades but has paid for higher tier | Product / Billing | Open | Medium |
| Q7 | Should Manage live TV tile persist after cancellation (as "Explore LIT" promotion)? | Affects Home screen state post-cancel | Product / Design | Open | Low |

---

## 20. Out of Scope

- Combined Fiber + LIT plan change in a single transaction
- Combined Fiber upgrade/downgrade + LIT upgrade/downgrade in a single transaction
- LIT access for suspended (paused, not resumed) customers
- FDO-based future-dated LIT plan changes
- Modifications to one RMN, ownership change, and relocation journeys (BAU)
- LIT Manage and Remove actions in recharge-for-others journey
- LIT first-time purchase UI (documented in scenario matrix; separate design flows)
- LIT nudge/promotion overlay screens (separate design section)
- Web portal access for Manage LIT (mobile app only for this release)
- Multi-screen/stream concurrency management (shown in design but not in Manage LIT scope)

---

## 21. Acceptance Criteria & Test Scenarios

### 21.1 Manage LIT — Functional Test Scenarios

| TC ID | Scenario | Steps | Expected Result | Scenario Ref |
|-------|----------|-------|-----------------|--------------|
| TC-M01 | View current LIT plan | Login → Home → Manage live TV | Manage Plan shows correct channel count, price, languages, genres | #3, #14 |
| TC-M02 | Change plan — add language | Change plan → Select Tamil → Proceed → Confirm → Pay | LIT pack updated with Tamil channels; fiber unchanged | #3 |
| TC-M03 | Change plan — upgrade with proration | Change plan → Select premium pack → Review proration → Pay | Prorated amount charged; new pack active immediately | #7 |
| TC-M04 | Change plan — downgrade | Change plan → Select smaller pack → Confirm | Instant downgrade; no FDO; new price reflected | #9 |
| TC-M05 | Change plan — swap | Change plan → Select same-price different pack → Confirm | Pack swapped; no fiber update; no proration | #8 |
| TC-M06 | Cancel plan — confirm | Cancel plan → Yes, Cancel My Plan | LIT cancelled; entitlement suspended immediately; success shown | #6, #10 |
| TC-M07 | Cancel plan — abandon | Cancel plan → I Don't Want to Cancel | Sheet dismissed; LIT remains active | — |
| TC-M08 | Search channels | Change plan → Your Channels → Search "Star" | Matching channels displayed | — |
| TC-M09 | Filter by language chip | Your Channels → Remove "Hindi" chip | Channel list updates; count recalculated | — |
| TC-M10 | Expand genre category | Manage Plan → Tap "Sports" | Sports channels displayed with logos | — |
| TC-M11 | Edit from summary | Summary → Tap pencil icon | Navigate back to plan selection; previous selection preserved | — |
| TC-M12 | Remove from summary | Summary → Tap trash icon | Cancel confirmation shown | #6 |
| TC-M13 | Combined fiber+LIT change blocked | Fiber plan change screen | LIT options not visible/disabled | #4, #11 |
| TC-M14 | Suspended account blocked | Login as suspended user | App login denied; no Manage LIT access | #13 |
| TC-M15 | Recharge for others — limited | Recharge for LIT subscriber | Continue only; no Manage/Remove | #19 |

### 21.2 General Acceptance Criteria

| Criteria | Validation Method | Pass Condition |
|----------|-------------------|----------------|
| All 15 Manage LIT test scenarios pass | QA regression | 100% pass rate |
| All 22 scenario matrix scenarios pass UAT | Business UAT | Signed UAT report |
| UI matches FigJam Manage LIT design | Design QA walkthrough | Zero critical design deviations |
| API integration tests pass | Automated + manual API testing | All endpoints return expected responses |
| Performance benchmarks met | Load testing | P95 within NFR thresholds |
| Accessibility audit passed | WCAG review | AA compliance for Manage LIT screens |

---

## Appendix A — Full Scenario Matrix

| S.No | Scenario | Customer State | Journey / Use Case | Key System Behavior | Manage LIT Relevance |
|------|----------|----------------|--------------------|---------------------|----------------------|
| 1 | LIT Add-on Purchase — Standalone | Fiber, No LIT | Standalone purchase | Expiry date sent; Add/Remove order (I) | ❌ Purchase flow |
| 1a | Recharge + LIT Add-on | Fiber, No LIT | Recharge with LIT | Charge current + next TPF + LIT | ❌ Purchase flow |
| 1b | Immediate Change Plan + LIT | Fiber, No LIT | Plan change with LIT | Change Package order; no FDO | ❌ Purchase flow |
| 2 | Fiber Change Plan Only | Fiber + LIT | Fiber plan change | LIT unmodifiable; validity aligned | ⚠️ Related — LIT unchanged |
| 3 | LIT Change Plan Only | Fiber + LIT | Manage LIT | Redirect to LIT; callback; Add/Remove (I & O) | ✅ **Primary flow** |
| 4 | Fiber + LIT Change Plan | Fiber + LIT | Combined change | **NOT SUPPORTED** | ✅ Must be blocked |
| 5 | Recharge / Advance Renewal | Fiber + LIT | Same-plan renewal | Combined price from getEndUserDetails | ⚠️ Related — renewal |
| 6 | LIT Drop / Cancellation | Fiber + LIT | Remove LIT | Add/Remove (O); immediate suspension | ✅ **Cancel flow** |
| 7 | Fiber Continue + LIT Upgrade | Fiber + LIT | LIT upgrade | Prorated + total price; Modify Plan | ✅ Change plan — upgrade |
| 8 | Fiber Continue + LIT Swap | Fiber + LIT | LIT swap | Same as upgrade; no fiber update | ✅ Change plan — swap |
| 9 | Fiber Continue + LIT Downgrade | Fiber + LIT | LIT downgrade | Instant; no FDO; Add/Remove order | ✅ Change plan — downgrade |
| 10 | Fiber Continue + LIT Cancellation | Fiber + LIT | LIT cancel | Add/Remove (O); unsubscribe + suspend | ✅ **Cancel flow** |
| 11 | Fiber + LIT Combined Upgrade/Downgrade | Fiber + LIT | Combined change | **NOT ALLOWED** | ✅ Must be blocked |
| 12 | Paused & Resumed + LIT Continue | Fiber + LIT (paused) | LIT continuation | Prorated + total; Add/Remove order | ⚠️ Related — proration |
| 13 | Paused, Not Resumed / Suspended | Suspended | Any LIT journey | **NOT ALLOWED** — no app login | ✅ Must be blocked |
| 14 | LIT Package & Channel Details | All | Display | HOBS wrapper API | ✅ Manage Plan data |
| 15 | LIT Subscriber Details | All | Profile | getSubscriberDetails returns LIT ID | ⚠️ Backend |
| 16 | RMN / Email Update | All | Profile update | HOBS → LIT Update Profile | ⚠️ Backend |
| 17 | Autopay + LIT Standalone | Fiber Autopay | LIT purchase | Automandate inclusion — **TBD** | ❓ Open question |
| 18 | Manage Services Page | All | Service hub | Promotion if no services | ⚠️ Related — discovery |
| 19 | Recharge for Others | Third-party recharge | LIT active | Continue only; no Manage/Remove | ✅ Must be restricted |
| 20 | One RMN | All | BAU | No change | — |
| 21 | Ownership Change | All | BAU | No change | — |
| 22 | Relocation Journey | All | BAU | No change | — |

---

## Appendix B — API Catalog

### B.1 HOBS LIT APIs (UAT)

```
Base: https://apiuathobs.tataplayfiber.co.in

GET  /lit/subscribe/getRedirectionUrl     — New LIT subscription redirection
GET  /lit/manage/getRedirectionUrl        — Manage/change plan redirection
GET  /lit/getSubscriberEntitlement/{id}   — LIT entitlement for subscriber
GET  /lit/packtochannel/{packName}        — Channels in a LIT pack
POST /lit/lit/updateSubscriberProfile     — Sync RMN/email to LIT
```

### B.2 Additional Entitlement API

```
GET https://apiuathobs.tataplay.com/SubscriberServices/subscriberEntitlements
```

### B.3 Existing MAPP/HOBS APIs (Modified)

```
POST submitOrder           — LIT add-on orders (I/O), Change Package
GET  getEndUserDetails     — Combined Fiber + LIT renewal pricing
GET  getSubscriberDetails  — Include LIT Subscriber ID
```

### B.4 New MAPP API

```
POST [TBD]/lit/callback    — Receive LIT platform response post-redirection
```

---

## Appendix C — UI Copy & Messaging Reference

| Context | Copy | Screen |
|---------|------|--------|
| Quick Action Label | Manage live TV | SCR-M01 |
| Quick Action Badge | New | SCR-M01 |
| Home Greeting | Good Morning {Customer Name}! | SCR-M01 |
| Current Plan Label | CURRENT PLAN | SCR-M01 |
| Action Selector Heading | What would you like to do? | SCR-M02 |
| Action Selector Subtext | Manage your Live TV plan in just a few taps | SCR-M02 |
| Change Plan Option | Change plan | SCR-M02 |
| Cancel Plan Option | Cancel plan | SCR-M02 |
| Manage Plan Header | Your Plan | SCR-M03 |
| My Channels Link | My Channels | SCR-M03 |
| TV Channels Label | TV Channels | SCR-M03 |
| Extra Box Label | Extra box | SCR-M03 |
| Discovery Prompt | Discover a best fit | SCR-M03 |
| Change Plan CTA | Change Plan | SCR-M03 |
| Language Instruction | Select one or more languages & get all channels of selected languages | SCR-M04 |
| Channel Footer | {N} Channels \| ₹{price}/month (Includes Rs {ncf} network fee) | SCR-M04 |
| Proceed CTA | Proceed | SCR-M04 |
| Channel Search Placeholder | Search channels in this pack | SCR-M05 |
| Plan Review Heading | Here's a plan based on your selection | SCR-M06 |
| Plan Card | {N} TV Channels at ₹{price}/month | SCR-M06 |
| Confirm CTA | Confirm & Proceed | SCR-M06 |
| Summary Header | Summary | SCR-M07 |
| Channel Count | {N} TV Channels | SCR-M07 |
| Duration Breakdown | ₹{monthly} × {months} Months | SCR-M07 |
| Payment CTA | Proceed to pay | SCR-M07 |
| Cancel Heading | We're sad to see you go! | SCR-M10 |
| Cancel Warning | Your plan will be cancelled and you will no longer have access to your content. Are you sure you want to cancel? | SCR-M10 |
| Cancel Confirm | Yes, Cancel My Plan | SCR-M10 |
| Cancel Dismiss | I Don't Want to Cancel | SCR-M10 |
| Cancel Success | Plan cancelled successfully! | SCR-M11 |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Owner | | | |
| Technical Lead (MAPP) | | | |
| Technical Lead (HOBS) | | | |
| Design Lead | | | |
| QA Lead | | | |
| Business Stakeholder | | | |

---

*End of Document — Version 1.2*
