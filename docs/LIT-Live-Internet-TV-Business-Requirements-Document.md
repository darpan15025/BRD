# Business Requirements Document (BRD)

## Tata Play Fiber Mobile Application (MAPP)
### Feature: LIT — Live Internet TV

---

| Field | Value |
|-------|-------|
| **Document Version** | 1.1 |
| **Date** | September 17, 2026 |
| **Status** | Draft |
| **Product** | Tata Play Fiber (TPF) Mobile App |
| **Feature Name** | LIT (Live Internet TV) — Manage LIT Module |
| **Design Reference** | [Login Revamp – FigJam (Manage LIT Section)](https://www.figma.com/board/psByt5QSY6vvmuAOmExFz7/Login-Revamp?node-id=0-1) |
| **Design Scope** | Manage LIT flows only (Change Plan + Cancel Plan) |
| **Source Inputs** | MAPP Scenario Matrix (LIT Integration), FigJam Design (Manage LIT section, node 168:3578) |

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Business Objectives](#2-business-objectives)
3. [Scope](#3-scope)
4. [Stakeholders](#4-stakeholders)
5. [Definitions & Acronyms](#5-definitions--acronyms)
6. [User Personas & Segments](#6-user-personas--segments)
7. [High-Level Solution Overview](#7-high-level-solution-overview)
8. [Functional Requirements](#8-functional-requirements)
9. [Business Rules & Constraints](#9-business-rules--constraints)
10. [User Journeys & Scenarios](#10-user-journeys--scenarios)
11. [API & Integration Requirements](#11-api--integration-requirements)
12. [UI/UX & Design Requirements](#12-uiux--design-requirements)
13. [Non-Functional Requirements](#13-non-functional-requirements)
14. [Assumptions & Dependencies](#14-assumptions--dependencies)
15. [Open Questions & Pending Decisions](#15-open-questions--pending-decisions)
16. [Out of Scope](#16-out-of-scope)
17. [Acceptance Criteria](#17-acceptance-criteria)
18. [Appendix A — Scenario Matrix](#appendix-a--scenario-matrix)
19. [Appendix B — API Catalog](#appendix-b--api-catalog)

---

## 1. Executive Summary

Tata Play Fiber (TPF) is introducing **LIT (Live Internet TV)** as an add-on service within the Tata Play Fiber Mobile Application (MAPP). LIT enables fiber subscribers to access live television content over the internet as a bundled or standalone subscription aligned with their fiber plan lifecycle.

This Business Requirements Document defines the end-to-end business, functional, and integration requirements for enabling LIT within MAPP. **Version 1.1 focuses the UI/UX design reference on the Manage LIT module** (Change Plan and Cancel Plan flows) as specified in the updated FigJam design board. The document also covers supporting backend scenarios for purchase, renewal, upgrade/downgrade, cancellation, and profile synchronization across multiple customer states.

The solution requires coordinated changes across:

- **MAPP (Mobile App)** — Frontend journeys, redirection to LIT, order placement, and entitlement display
- **HOBS (Backend)** — Order orchestration, LIT wrapper APIs, subscriber entitlement, and profile sync
- **LIT Platform** — Subscription management, pricing, proration, and callback to MAPP

---

## 2. Business Objectives

| # | Objective | Success Metric |
|---|-----------|----------------|
| O1 | Enable fiber customers to discover, purchase, and manage LIT add-on within MAPP | LIT attach rate on eligible fiber base |
| O2 | Maintain billing and validity alignment between Fiber and LIT subscriptions | Zero misaligned renewal dates for bundled customers |
| O3 | Provide self-service LIT plan changes without contact center dependency | Reduction in LIT-related support calls |
| O4 | Promote value-added services (LIT, WiFi+, Static IP) via dedicated Manage Services experience | Increased multi-service adoption |
| O5 | Ensure consistent subscriber identity across Fiber and LIT (RMN, email, subscriber ID) | Profile sync success rate |

---

## 3. Scope

### 3.1 In Scope

- LIT add-on purchase for existing fiber customers (standalone and combined with recharge/plan change)
- LIT plan management (upgrade, downgrade, swap, cancellation) via Manage LIT journey
- Fiber plan change with existing LIT subscription handling
- Combined renewal pricing for fiber + LIT (same-plan renewal)
- LIT drop/cancellation during active tenure
- LIT package and channel details display in MAPP
- LIT subscriber ID in subscriber details
- RMN/email profile update propagation to LIT
- Manage Services dedicated page with service promotion
- HOBS wrapper APIs and MAPP callback API for LIT integration
- Paused & resumed fiber scenarios with LIT continuation

### 3.2 Out of Scope (for this release)

See [Section 16 — Out of Scope](#16-out-of-scope).

---

## 4. Stakeholders

| Role | Responsibility |
|------|----------------|
| Product Owner (TPF) | Feature prioritization, business sign-off |
| MAPP Frontend Team | UI implementation, LIT redirection flows |
| MAPP Backend Team | Order APIs, LIT callback receiver, HOBS integration |
| HOBS Team | Wrapper APIs, order fulfillment, entitlement management |
| LIT Platform Team | Subscription lifecycle, pricing, proration, redirection URLs |
| DigiSales Team | Online sales journey, payment link integration |
| QA Team | End-to-end scenario validation |
| UAT Business Users | Acceptance testing per scenario matrix |

---

## 5. Definitions & Acronyms

| Term | Definition |
|------|------------|
| **MAPP** | Tata Play Fiber Mobile Application |
| **LIT** | Live Internet TV — OTT/live TV add-on service |
| **HOBS** | Home Order & Billing System — backend orchestration platform |
| **TPF** | Tata Play Fiber |
| **RMN** | Registered Mobile Number |
| **FDO** | Fiber Date of Operation — plan change effective date rules |
| **Add/Remove Order** | HOBS order type with action `I` (Insert/Add) or `O` (Remove) for LIT |
| **Change Package Order** | HOBS order for fiber plan changes |
| **Prorated Price** | Partial charge/credit based on remaining validity |
| **Autopay / Automandate** | Recurring payment mandate for fiber renewal |
| **BAU** | Business As Usual — no change to existing flow |

---

## 6. User Personas & Segments

### 6.1 Customer Segments

| Segment | Description |
|---------|-------------|
| **S1: Fiber Only** | Active fiber subscriber without LIT |
| **S2: Fiber + LIT** | Active fiber subscriber with active LIT add-on |
| **S3: Fiber Autopay** | Fiber subscriber on autopay mandate |
| **S4: Paused Fiber** | Fiber connection paused (resumed or not resumed) |
| **S5: Suspended** | Account suspended — app login restricted |
| **S6: Recharge for Others** | User recharging another subscriber's account |

### 6.2 Primary Use Cases

1. Purchase LIT as first-time add-on
2. Renew fiber and LIT together
3. Change fiber plan while retaining LIT
4. Change LIT plan independently
5. Upgrade/downgrade/swap LIT plan
6. Cancel/drop LIT during tenure
7. View LIT packages, channels, and entitlements
8. Discover and promote services on Manage Services page

---

## 7. High-Level Solution Overview

### 7.1 Architecture Flow

```
┌─────────────┐     Redirection URL      ┌─────────────┐
│    MAPP     │ ───────────────────────► │     LIT     │
│  (Mobile)   │ ◄─────────────────────── │  Platform   │
└──────┬──────┘     Callback / Response   └─────────────┘
       │
       │ submitOrder / getEndUserDetails / getSubscriberDetails
       ▼
┌─────────────┐     LIT Wrapper APIs     ┌─────────────┐
│    HOBS     │ ◄──────────────────────► │     LIT     │
│  (Backend)  │                          │   Backend   │
└─────────────┘                          └─────────────┘
```

### 7.2 Core Integration Pattern

1. **Subscribe Journey**: MAPP calls HOBS `getRedirectionUrl` (subscribe) → redirects customer to LIT → LIT returns selection/pricing → MAPP places Add/Remove order (`I`) via `submitOrder`
2. **Manage Journey**: MAPP calls HOBS `getRedirectionUrl` (manage) → redirects to LIT for plan change → MAPP receives callback → places Add/Remove order (`I` & `O`) as applicable
3. **Entitlement Display**: MAPP fetches LIT package/channel details and subscriber entitlements via HOBS wrapper APIs

---

## 8. Functional Requirements

### 8.1 LIT Discovery & Purchase (Fiber Only — No LIT)

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-1.1 | MAPP shall display LIT as an available add-on during recharge, plan change, and standalone purchase journeys | Must Have |
| FR-1.2 | For standalone LIT purchase, MAPP shall send current fiber plan expiry date to LIT for redirection | Must Have |
| FR-1.3 | MAPP shall place Add/Remove order with LIT add-on action `I` upon successful LIT selection | Must Have |
| FR-1.4 | For Recharge + LIT, customer shall be charged for current period + next expiry of TPF + LIT | Must Have |
| FR-1.5 | For Immediate Change Plan + LIT, MAPP shall place Change Package order; FDO change plan shall NOT be allowed | Must Have |
| FR-1.6 | End date for Immediate Change Plan + LIT shall equal Current Date + Destination Plan Validity | Must Have |

### 8.2 Fiber Plan Management (Fiber + LIT)

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-2.1 | During fiber-only plan change, customer shall NOT be able to modify LIT products | Must Have |
| FR-2.2 | Existing LIT subscription shall remain active; validity aligned with new fiber plan validity | Must Have |
| FR-2.3 | MAPP shall invoke LIT Pricing API and submit Change Plan order for fiber change | Must Have |
| FR-2.4 | Combined Fiber + LIT plan change in a single transaction shall NOT be supported | Must Have |
| FR-2.5 | MAPP shall restrict LIT redirection during fiber-only plan change journey | Must Have |

### 8.3 LIT Plan Management (Fiber + LIT)

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-3.1 | LIT plan change shall be supported through dedicated Manage LIT journey | Must Have |
| FR-3.2 | MAPP shall redirect to LIT and receive callback for LIT plan changes | Must Have |
| FR-3.3 | MAPP shall place Add/Remove order with LIT action `I` and `O` as applicable | Must Have |
| FR-3.4 | LIT Upgrade: HOBS shall return prorated price + total price; HOBS processes LIT Modify Plan | Must Have |
| FR-3.5 | LIT Swap: Same process as upgrade; no fiber update required | Must Have |
| FR-3.6 | LIT Downgrade: FDO not applicable; change processed instantly via Add/Remove order | Must Have |
| FR-3.7 | LIT Cancellation: MAPP places Add/Remove order with action `O`; HOBS unsubscribes and suspends LIT | Must Have |
| FR-3.8 | Combined Fiber upgrade/downgrade + LIT upgrade/downgrade in single transaction shall NOT be allowed | Must Have |

### 8.4 Renewal & Recharge

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-4.1 | For same-plan renewal, `getEndUserDetails` API shall return combined Fiber + LIT renewal price | Must Have |
| FR-4.2 | Customer shall be able to renew both services in a single renewal journey | Must Have |

### 8.5 LIT Cancellation / Drop

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-5.1 | Customer shall remove LIT add-on through MAPP during active tenure | Must Have |
| FR-5.2 | MAPP shall submit Add/Remove order with action `O` | Must Have |
| FR-5.3 | LIT entitlement shall be suspended immediately upon fulfillment | Must Have |
| FR-5.4 | If LIT drop without order is allowed, drop option shall be available across all fiber journeys | Should Have |

### 8.6 Paused / Suspended Fiber

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-6.1 | For paused & resumed fiber, customer logs into MAPP, redirected to LIT; LIT provides prorated + total amount | Must Have |
| FR-6.2 | MAPP places Add/Remove order in HOBS for paused/resumed LIT continuation | Must Have |
| FR-6.3 | Suspended customers (paused but not resumed) shall NOT be permitted TPF app login; MAPP → LIT redirection not feasible | Must Have |

### 8.7 Common MAPP Changes

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-7.1 | HOBS wrapper API shall provide LIT package and channel details for MAPP display | Must Have |
| FR-7.2 | `getSubscriberDetails` API shall return LIT Subscriber ID | Must Have |
| FR-7.3 | On RMN/email update in MAPP, HOBS shall update LIT subscriber profile via LIT Update Subscriber Profile API | Must Have |
| FR-7.4 | MAPP profile update journey shall remain unchanged from user perspective | Must Have |

### 8.8 Manage Services Page

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-8.1 | Dedicated Manage Services page shall display Static IP, WiFi+, LIT, and other value-added services | Must Have |
| FR-8.2 | If customer has not subscribed to any add-on services, service promotion shall be displayed | Must Have |
| FR-8.3 | Customer with active LIT shall see manage/continue options appropriate to their state | Must Have |

### 8.9 Recharge for Others

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-9.1 | If target subscriber has LIT, recharger shall see Continue option only | Must Have |
| FR-9.2 | Manage and Remove options shall NOT be available in recharge-for-others journey for LIT | Must Have |

### 8.10 Autopay

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-10.1 | When fiber autopay customer purchases LIT standalone, system shall determine if LIT price is included in automandate file | Must Have (pending decision) |

### 8.11 Unchanged Journeys (BAU)

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-11.1 | One RMN journey — no change | BAU |
| FR-11.2 | Ownership change journey — no change | BAU |
| FR-11.3 | Relocation journey — no change | BAU |

---

## 9. Business Rules & Constraints

| Rule ID | Rule |
|---------|------|
| BR-01 | LIT validity shall align with fiber plan validity for bundled customers |
| BR-02 | FDO (Fiber Date of Operation) is NOT applicable for LIT plan changes |
| BR-03 | LIT downgrade is processed instantly — no future-dated change |
| BR-04 | Combined fiber + LIT plan change transactions are prohibited |
| BR-05 | Combined fiber upgrade/downgrade + LIT upgrade/downgrade transactions are prohibited |
| BR-06 | LIT entitlement suspension is immediate upon cancellation/drop fulfillment |
| BR-07 | Suspended accounts cannot access MAPP; LIT redirection blocked |
| BR-08 | During fiber-only plan change, LIT products cannot be modified |
| BR-09 | Recharge-for-others: LIT allows Continue only — no Manage or Remove |
| BR-10 | Immediate Change Plan + LIT: end date = Current Date + Destination Plan Validity |
| BR-11 | Prorated pricing applies for LIT upgrade and paused/resumed fiber scenarios |

---

## 10. User Journeys & Scenarios

### 10.1 Journey: LIT Add-on Purchase (Standalone)

**Precondition:** Customer has active fiber, no LIT  
**Actor:** Fiber subscriber  

| Step | Action | System Response |
|------|--------|-----------------|
| 1 | Customer navigates to LIT / Manage Services | MAPP displays LIT promotion or purchase CTA |
| 2 | Customer selects LIT add-on | MAPP sends current plan expiry date to LIT |
| 3 | MAPP redirects to LIT platform | LIT displays plans, channels, pricing |
| 4 | Customer confirms LIT selection | LIT returns selection to MAPP via callback |
| 5 | MAPP places Add/Remove order (action `I`) | HOBS fulfills; LIT entitlement activated |
| 6 | Customer returns to MAPP | Confirmation screen; LIT visible in Manage Services |

### 10.2 Journey: Recharge + LIT Add-on

**Precondition:** Customer has active fiber, no LIT  
**Actor:** Fiber subscriber  

| Step | Action | System Response |
|------|--------|-----------------|
| 1 | Customer initiates recharge | Standard recharge flow |
| 2 | Customer selects LIT add-on | Expiry date sent for LAMP/LIT redirection |
| 3 | Customer completes payment | Charged for current + next TPF + LIT expiry |
| 4 | MAPP places Add/Remove order | HOBS fulfills both fiber renewal and LIT add |

### 10.3 Journey: Manage LIT (Plan Change)

**Precondition:** Customer has active fiber + LIT  
**Actor:** Fiber + LIT subscriber  

| Step | Action | System Response |
|------|--------|-----------------|
| 1 | Customer opens Manage LIT | MAPP calls manage redirection URL API |
| 2 | Redirect to LIT platform | LIT shows current plan, upgrade/downgrade/swap options |
| 3 | Customer selects new LIT plan | Prorated + total price displayed |
| 4 | LIT callback to MAPP | MAPP places Add/Remove order (`I` & `O`) |
| 5 | HOBS processes Modify Plan | Updated LIT entitlement reflected in MAPP |

### 10.4 Journey: LIT Drop / Cancellation

**Precondition:** Customer has active fiber + LIT  
**Actor:** Fiber + LIT subscriber  

| Step | Action | System Response |
|------|--------|-----------------|
| 1 | Customer selects Remove LIT | Confirmation prompt |
| 2 | Customer confirms removal | MAPP submits Add/Remove order (action `O`) |
| 3 | HOBS fulfills | LIT unsubscribed and suspended immediately |
| 4 | MAPP updates UI | LIT no longer shown as active service |

### 10.5 Journey: Fiber Change Plan Only (with existing LIT)

**Precondition:** Customer has active fiber + LIT  
**Actor:** Fiber + LIT subscriber  

| Step | Action | System Response |
|------|--------|-----------------|
| 1 | Customer initiates fiber plan change | LIT modification options hidden/disabled |
| 2 | Customer selects new fiber plan | MAPP invokes LIT Pricing API |
| 3 | MAPP submits Change Package order | Existing LIT remains; validity aligned to new fiber plan |
| 4 | No LIT redirection occurs | Fiber plan updated; LIT unchanged |

---

## 11. API & Integration Requirements

### 11.1 New HOBS APIs

| API | Endpoint | Purpose |
|-----|----------|---------|
| LIT Subscribe Redirection | `GET/POST /lit/subscribe/getRedirectionUrl` | Obtain LIT URL for new subscription journey |
| LIT Manage Redirection | `GET/POST /lit/manage/getRedirectionUrl` | Obtain LIT URL for manage/change plan journey |
| LIT Subscriber Entitlement | `GET /lit/getSubscriberEntitlement/{subscriberId}` | Fetch LIT entitlements for a subscriber |
| Subscriber Entitlements | `GET /SubscriberServices/subscriberEntitlements` | Combined entitlement data |
| Pack to Channel Mapping | `GET /lit/packtochannel/{packName}` | Channel list for a LIT pack |
| Update Subscriber Profile | `POST /lit/lit/updateSubscriberProfile` | Sync RMN/email changes to LIT |

**Base URL (UAT):** `https://apiuathobs.tataplayfiber.co.in`

### 11.2 New MAPP API

| API | Direction | Purpose |
|-----|-----------|---------|
| LIT Callback Receiver | LIT → MAPP | Receive subscription/plan selection data from LIT platform after redirection |

### 11.3 Modified Existing APIs

| API | Change Required |
|-----|-----------------|
| `submitOrder` | Support LIT add-on with action `I` (add) and `O` (remove); Change Package for fiber + LIT scenarios |
| `getEndUserDetails` | Return combined Fiber + LIT renewal price for same-plan renewal |
| `getSubscriberDetails` | Return LIT Subscriber ID in response |

### 11.4 API Sequence — Subscribe Flow

```
MAPP → HOBS: getRedirectionUrl (subscribe)
HOBS → MAPP: redirection URL
MAPP → LIT: redirect user
LIT → MAPP: callback with plan selection
MAPP → HOBS: submitOrder (LIT action I)
HOBS → LIT: activate subscription
HOBS → MAPP: order confirmation
```

---

## 12. UI/UX & Design Requirements — Manage LIT Module

**Design Source:** [FigJam — Login Revamp (Manage LIT Section)](https://www.figma.com/board/psByt5QSY6vvmuAOmExFz7/Login-Revamp?node-id=0-1)

> **Design Scope Note:** This BRD references only the **Manage LIT** section of the design board, comprising two primary flows: **Change Plan** and **Cancel Plan**. Purchase, recharge, and nudge flows are documented in the scenario matrix (Appendix A) but are out of scope for this design section.

### 12.1 Manage LIT — Flow Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         MANAGE LIT ENTRY                                 │
│  Home Screen → Quick Actions → "Manage live TV" (New badge)             │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    ACTION SELECTOR (Bottom Sheet)                        │
│  "What would you like to do?"                                           │
│  ┌─────────────────┐    ┌─────────────────┐                           │
│  │  Change plan    │    │  Cancel plan    │                           │
│  └────────┬────────┘    └────────┬────────┘                           │
└───────────┼──────────────────────┼────────────────────────────────────┘
            │                      │
            ▼                      ▼
   ┌────────────────┐     ┌────────────────────────┐
   │  CHANGE PLAN   │     │     CANCEL PLAN        │
   │  (9 screens)   │     │     (4 screens)        │
   └────────────────┘     └────────────────────────┘
```

### 12.2 Screen Inventory — Manage LIT (from FigJam Design)

#### Flow A: Change Plan

| Screen ID | Screen Name | Key Elements | CTA / Action |
|-----------|-------------|--------------|--------------|
| SCR-M01 | Home Screen — Quick Action | Current plan card (200 MBPS), Quick Actions grid, **Manage live TV** tile with "New" badge | Tap Manage live TV |
| SCR-M02 | Action Selector (Bottom Sheet) | Heading: "What would you like to do?"; Subtext: "Manage your Live TV plan in just a few taps"; Two options: Cancel plan, Change plan | Select Change plan |
| SCR-M03 | Manage Plan Overview | **Your Plan** section: price (₹399/month), 130 TV channels, 1 Extra box; **My Channels** link; channel logo grid with View All; collapsible genre categories (Movies, Sports, News, etc.); "Discover a best fit" prompt | Change Plan (sticky footer) |
| SCR-M04 | Language Selection (Subscribe) | Heading: select languages for channels; Grid of language cards (English, Hindi, Marathi, Telugu, Tamil, Kannada, Malayalam, Bengali, etc.); Live footer: channel count + price (e.g., "531 Channels \| ₹399/month (Includes Rs 153 network fee)") | Proceed |
| SCR-M05 | Your Channels (Browse) | Search bar: "Search channels in this pack"; Language filter chips (English ×, Hindi ×); Genre categories with channel counts: TV Shows (161), Sports (25), Movies (48), News (45), Spiritual (11), Kids (15) | Select category to expand |
| SCR-M06 | Plan Details (Review) | Heading: "Here's a plan based on your selection"; Plan card: "538 TV Channels at ₹346/month"; Genre tags; Channel icon grid; Sparkle/promo banner | Confirm & Proceed |
| SCR-M07 | Summary (Collapsed) | Header: "Summary"; LIT pack card with label badge, channel count, price (₹2382), duration (₹397 × 6 Months); Edit (pencil) and Remove (trash) icons; Sticky footer: total ₹2382 + "Proceed to pay" | Proceed to pay |
| SCR-M08 | Summary (Expanded) | Expanded pack card with specs list (monitor icon: screen count; globe icon: language details); OTT/genre tags; Full pricing breakdown | Proceed to pay |
| SCR-M09 | Payment Confirmation | Final order summary with LIT pack details and payment CTA | Complete payment |

#### Flow B: Cancel Plan

| Screen ID | Screen Name | Key Elements | CTA / Action |
|-----------|-------------|--------------|--------------|
| SCR-M01 | Home Screen — Quick Action | Same entry as Change Plan flow | Tap Manage live TV |
| SCR-M02 | Action Selector (Bottom Sheet) | Same action selector | Select Cancel plan |
| SCR-M10 | Cancel Confirmation (Bottom Sheet) | Sad face icon; Heading: "We're sad to see you go!"; Warning: "Your plan will be cancelled and you will no longer have access to your content. Are you sure you want to cancel?"; Close (×) button | Yes, Cancel My Plan / I Don't Want to Cancel |
| SCR-M11 | Cancel Success | Green checkmark icon; Heading: "Plan cancelled successfully!"; Dimmed home screen background | Auto-dismiss or navigate to Home |

### 12.3 UI Component Specifications

| Component | Specification |
|-----------|---------------|
| **Color Theme** | Dark theme; deep purple headers; vibrant magenta/pink primary CTAs (Pay Now, Change Plan, Confirm) |
| **Navigation** | Android navbar with back button; screen title in header bar |
| **Bottom Sheet** | Used for action selector and cancel confirmation; drag indicator at top |
| **Sticky Footer** | Price summary (left) + primary CTA button (right); chevron-up to expand price details |
| **Filter Chips** | Removable language tags (e.g., English ×, Hindi ×); genre filter chips |
| **Channel Cards** | Medium channel chips with logo, channel name, and metadata badge |
| **Plan Card** | Label badge, channel count, monthly price, duration breakdown, edit/remove actions |
| **Language Grid** | 3-column grid of selectable language icon cards |
| **Genre Accordion** | Collapsible dropdown rows with genre name, channel count, and chevron |
| **Search Bar** | Animated placeholder: "Search channels in this pack" with filter icon |
| **Price Display** | Itemized: base price, network fee (NCF), discount percentage, total |
| **Badges** | "New" badge on Manage live TV quick action; genre/OTT tags on plan cards |

### 12.4 Interaction & Behavior Requirements

| ID | Requirement |
|----|-------------|
| UX-M01 | Manage live TV quick action shall display "New" badge for eligible subscribers |
| UX-M02 | Action selector bottom sheet shall overlay home screen with dimmed background |
| UX-M03 | Language selection shall update channel count and price in sticky footer in real time |
| UX-M04 | Channel search shall filter results within the selected LIT pack |
| UX-M05 | Language filter chips shall be removable; removing a chip updates channel list |
| UX-M06 | Genre categories shall expand/collapse on tap to show channel list |
| UX-M07 | Summary screen chevron-up shall expand/collapse pack detail card |
| UX-M08 | Edit (pencil) icon on summary shall navigate back to plan selection |
| UX-M09 | Remove (trash) icon on summary shall trigger cancel/remove flow |
| UX-M10 | Cancel confirmation shall require explicit "Yes, Cancel My Plan" tap |
| UX-M11 | "I Don't Want to Cancel" shall dismiss bottom sheet and return to previous screen |
| UX-M12 | Cancel success shall show confirmation with green checkmark before auto-dismiss |
| UX-M13 | Prorated price and total price shall be displayed before payment on plan change |
| UX-M14 | Loading state shall be shown during MAPP → LIT redirection |
| UX-M15 | Error states from LIT callback or HOBS order failure shall provide retry option |

### 12.5 Copy & Messaging (from Design)

| Context | Copy |
|---------|------|
| Quick Action Label | Manage live TV |
| Action Selector Heading | What would you like to do? |
| Action Selector Subtext | Manage your Live TV plan in just a few taps |
| Manage Plan Section | Your Plan |
| Channel Link | My Channels |
| Discovery Prompt | Discover a best fit |
| Language Selection | Select one or more languages & get all channels of selected languages |
| Channel Search | Search channels in this pack |
| Plan Review | Here's a plan based on your selection |
| Summary Header | Summary |
| Payment CTA | Proceed to pay |
| Change Plan CTA | Change Plan |
| Confirm CTA | Confirm & Proceed |
| Cancel Heading | We're sad to see you go! |
| Cancel Warning | Your plan will be cancelled and you will no longer have access to your content. Are you sure you want to cancel? |
| Cancel Confirm | Yes, Cancel My Plan |
| Cancel Dismiss | I Don't Want to Cancel |
| Cancel Success | Plan cancelled successfully! |

---

## 13. Non-Functional Requirements

| ID | Category | Requirement |
|----|----------|-------------|
| NFR-01 | Performance | LIT redirection URL shall be obtained within 3 seconds |
| NFR-02 | Performance | Order submission post-LIT callback shall complete within 5 seconds |
| NFR-03 | Availability | LIT integration APIs shall maintain 99.5% uptime |
| NFR-04 | Security | All MAPP ↔ HOBS ↔ LIT communication over HTTPS/TLS |
| NFR-05 | Security | LIT callback shall be authenticated and validated before order placement |
| NFR-06 | Audit | All LIT orders shall be logged with subscriber ID, action, timestamp, and order ID |
| NFR-07 | Compatibility | Feature shall work on supported iOS and Android app versions per TPF release matrix |
| NFR-08 | Localization | All user-facing strings shall support English (Hindi optional per product decision) |

---

## 14. Assumptions & Dependencies

### 14.1 Assumptions

- LIT platform is operational and provides stable redirection and callback mechanisms
- HOBS wrapper APIs will be available before MAPP frontend integration begins
- Fiber plan expiry date is the authoritative date for LIT validity alignment
- Proration logic is owned and calculated by LIT platform; MAPP displays returned values
- Design in Figma (node 4189-54157) is approved and final for development

### 14.2 Dependencies

| Dependency | Owner | Impact |
|------------|-------|--------|
| HOBS LIT wrapper APIs | HOBS Team | Blocks all LIT journeys |
| LIT callback specification | LIT Team | Blocks order placement post-redirection |
| MAPP callback API | MAPP Backend | Blocks LIT → MAPP data handoff |
| Figma design approval | Design Team | Blocks frontend development |
| DigiSales integration (if in scope) | DigiSales Team | Blocks online sales journey |
| Autopay automandate file update | Billing Team | Blocks autopay + LIT scenario |

---

## 15. Open Questions & Pending Decisions

| # | Question | Owner | Status |
|---|----------|-------|--------|
| Q1 | Online sales journey — how will LIT be integrated? | Prasad / DigiSales | Discussion pending |
| Q2 | DigiSales Payment Link journey — LIT support? | Prasad / DigiSales | Discussion pending |
| Q3 | 2-step verification (Portal) — impact on LIT journeys? | Prasad / DigiSales | Discussion pending |
| Q4 | Autopay: Will LIT price be automatically included in automandate file for standalone LIT purchase? | Billing / Product | Open |
| Q5 | If LIT drop without order is allowed, should drop be included in all fiber journeys? | Product | Open |
| Q6 | One RMN, ownership change, relocation — confirmed BAU with no LIT-specific changes? | Product | Confirmed BAU |

---

## 16. Out of Scope

- Combined Fiber + LIT plan change in a single transaction
- Combined Fiber upgrade/downgrade + LIT upgrade/downgrade in a single transaction
- LIT access for suspended (paused, not resumed) customers
- FDO-based future-dated LIT plan changes
- Modifications to one RMN, ownership change, and relocation journeys (BAU)
- LIT Manage and Remove in recharge-for-others journey

---

## 17. Acceptance Criteria

### 17.1 Scenario-Based Acceptance

All 22 scenarios defined in the source scenario matrix (Appendix A) shall pass UAT with documented evidence.

### 17.2 General Acceptance

| Criteria | Validation Method |
|----------|-------------------|
| LIT purchase completes end-to-end for fiber-only customer | UAT Scenario 1 |
| Fiber + LIT renewal shows combined price | UAT Scenario 5 |
| LIT plan change via Manage LIT works with proration | UAT Scenarios 7–9 |
| LIT cancellation suspends entitlement immediately | UAT Scenarios 6, 10 |
| Combined transactions correctly blocked | UAT Scenarios 4, 11 |
| Profile update syncs to LIT | UAT Scenario 16 |
| Manage Services shows promotion for unsubscribed customers | UAT Scenario 18 |
| Recharge-for-others restricts LIT actions | UAT Scenario 19 |
| All HOBS APIs return expected responses | API integration testing |
| Manage LIT UI matches FigJam design (Manage LIT section) | Design QA review |

---

## Appendix A — Scenario Matrix

| S.No | Scenario | Customer State | Journey / Use Case | Key System Behavior |
|------|----------|----------------|--------------------|---------------------|
| 1 | LIT Add-on Purchase — Standalone | Fiber, No LIT | Standalone purchase | Expiry date sent; Add/Remove order (I) |
| 1a | Recharge + LIT Add-on | Fiber, No LIT | Recharge with LIT | Charge current + next TPF + LIT; Add/Remove order |
| 1b | Immediate Change Plan + LIT | Fiber, No LIT | Plan change with LIT | Change Package order; no FDO; end date = today + validity |
| 2 | Fiber Change Plan Only | Fiber + LIT | Fiber plan change | LIT unmodifiable; validity aligned; Change Plan order |
| 3 | LIT Change Plan Only | Fiber + LIT | Manage LIT | Redirect to LIT; callback; Add/Remove (I & O) |
| 4 | Fiber + LIT Change Plan | Fiber + LIT | Combined change | **NOT SUPPORTED** — separate transactions required |
| 5 | Recharge / Advance Renewal | Fiber + LIT | Same-plan renewal | getEndUserDetails returns combined price |
| 6 | LIT Drop / Cancellation | Fiber + LIT | Remove LIT | Add/Remove (O); immediate suspension |
| 7 | Fiber Continue + LIT Upgrade | Fiber + LIT | LIT upgrade | Prorated + total price; Modify Plan |
| 8 | Fiber Continue + LIT Swap | Fiber + LIT | LIT swap | Same as upgrade; no fiber update |
| 9 | Fiber Continue + LIT Downgrade | Fiber + LIT | LIT downgrade | Instant; no FDO; Add/Remove order |
| 10 | Fiber Continue + LIT Cancellation | Fiber + LIT | LIT cancel | Add/Remove (O); unsubscribe + suspend |
| 11 | Fiber + LIT Combined Upgrade/Downgrade | Fiber + LIT | Combined change | **NOT ALLOWED** |
| 12 | Paused & Resumed + LIT Continue | Fiber + LIT (paused) | LIT continuation | Prorated + total; Add/Remove order |
| 13 | Paused, Not Resumed / Suspended | Suspended | Any LIT journey | **NOT ALLOWED** — no app login |
| 14 | LIT Package & Channel Details | All | Display | HOBS wrapper API |
| 15 | LIT Subscriber Details | All | Profile | getSubscriberDetails returns LIT Subscriber ID |
| 16 | RMN / Email Update | All | Profile update | HOBS → LIT Update Subscriber Profile |
| 17 | Autopay + LIT Standalone | Fiber Autopay | LIT purchase | Automandate inclusion — **TBD** |
| 18 | Manage Services Page | All | Service hub | Promotion if no services selected |
| 19 | Recharge for Others | Third-party recharge | LIT active | Continue only; no Manage/Remove |
| 20 | One RMN | All | BAU | No change |
| 21 | Ownership Change | All | BAU | No change |
| 22 | Relocation Journey | All | BAU | No change |

---

## Appendix B — API Catalog

### B.1 HOBS LIT APIs (UAT)

```
Base: https://apiuathobs.tataplayfiber.co.in

GET  /lit/subscribe/getRedirectionUrl
GET  /lit/manage/getRedirectionUrl
GET  /lit/getSubscriberEntitlement/{subscriberId}
GET  /lit/packtochannel/{packName}
POST /lit/lit/updateSubscriberProfile
```

### B.2 Additional Entitlement API

```
GET https://apiuathobs.tataplay.com/SubscriberServices/subscriberEntitlements
```

### B.3 Existing MAPP/HOBS APIs (Modified)

```
POST submitOrder          — LIT add-on orders (I/O), Change Package
GET  getEndUserDetails    — Combined Fiber + LIT renewal pricing
GET  getSubscriberDetails — Include LIT Subscriber ID
```

### B.4 New MAPP API

```
POST [TBD]/lit/callback   — Receive LIT platform response post-redirection
```

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Owner | | | |
| Technical Lead (MAPP) | | | |
| Technical Lead (HOBS) | | | |
| QA Lead | | | |
| Business Stakeholder | | | |

---

*End of Document*
