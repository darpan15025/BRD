
## Full Design Modules Overview (FigJam Board)

**Design Source:** [Login Revamp – Full FigJam Board](https://www.figma.com/board/psByt5QSY6vvmuAOmExFz7/Login-Revamp?node-id=0-1)

The FigJam board contains **8 design modules** covering the complete LIT-enabled Tata Play Fiber mobile experience. This section documents every module, its screens, user flows, and mapping to business scenarios.

### Design Module Map

| Module | FigJam Section | Customer State | Primary Flows | Scenario Ref |
|--------|----------------|----------------|---------------|--------------|
| **A** | Login Flow | All (pre-requisite) | Mobile login, OTP, password reset, first-time setup | Enables all LIT journeys |
| **B** | Home Dashboard | All active subscribers | Plan card, Quick Actions, What's New, bottom nav | Entry point for all LIT flows |
| **C** | Existing Fiber — No LIT | Fiber only | LIT Nudge, Standalone Purchase, Recharge + LIT, Change Plan + LIT | Scenarios 1, 1a, 1b |
| **D** | Manage LIT | Fiber + LIT | Change Plan, Cancel Plan | Scenarios 3, 6, 7–10 |
| **E** | Existing Fiber + LIT | Fiber + LIT | Home (Manage Live TV), Renewal, Combined payment | Scenarios 2, 5, 12 |
| **F** | Autopay | Fiber / Fiber + LIT | Autopay setup, cancel, LIT + automandate | Scenario 17 |
| **G** | Payment & Summary | All purchase/change flows | Order summary, itemized billing, proceed to pay | All payment journeys |
| **H** | Promotions | All | Cashback offer, referral banner | Cross-sell |

### End-to-End Experience Map

```
LOGIN (A) ──► HOME (B) ──┬──► PURCHASE LIT (C) ──► PAYMENT (G) ──► HOME (B)
                           │         ▲
                           │    LIT Nudge / Recharge upsell
                           │
                           ├──► MANAGE LIT (D) ──► PAYMENT (G)
                           │
                           ├──► RENEW FIBER+LIT (E) ──► PAYMENT (G)
                           │
                           └──► AUTOPAY (F)
```

---

## Module A — Login Flow

### A.1 Purpose

Authentication is the gateway to all LIT journeys. Customers must log in via RMN/CID before accessing Home, purchasing LIT, or managing their subscription.

### A.2 Screens

| Screen ID | Screen Name | Key Elements | User Actions |
|-----------|-------------|--------------|--------------|
| SCR-A01 | Welcome / Mobile Entry | Hero image, "Simply faster internet", RMN input, Privacy Policy checkbox, "Send OTP", "Login via WhatsApp" | Enter mobile, accept policy, send OTP |
| SCR-A02 | OTP Verification | "Verify your number", 6-digit OTP inputs, timer (00:20), "Didn't get it? Send Code again" | Enter OTP, resend |
| SCR-A03 | OTP Validating | "Validating..." loading state on CTA | Wait |
| SCR-A04 | CID + Password Login | Customer ID field, Password field, "Forget Password" link | Login with credentials |
| SCR-A05 | Reset Password — CID Entry | "Reset Password", CID input, "Send Temporary Code" | Request reset code |
| SCR-A06 | Reset Password — Set New | Temporary code + new password fields, password rules, "Set Password" | Complete reset |
| SCR-A07 | Set Password (First Login) | New password with strength rules (length, categories) | Set initial password |
| SCR-A08 | Welcome / Setup Loading | "Welcome {Name}", "Please wait, Setting up your experience…", educational "Did you know?" card, Skip | Wait or skip onboarding tip |
| SCR-A09 | Login Success | Success title and message | Auto-redirect to Home |

### A.3 Business Requirements — Login

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-A1 | Customer shall log in via RMN + OTP or CID + Password | Must Have |
| FR-A2 | WhatsApp OTP login option shall be available | Should Have |
| FR-A3 | Privacy Policy acceptance required before OTP send | Must Have |
| FR-A4 | OTP resend with countdown timer (e.g., 20 seconds) | Must Have |
| FR-A5 | Password reset via temporary code sent to RMN | Must Have |
| FR-A6 | First-time users guided through password setup with strength validation | Must Have |
| FR-A7 | Suspended accounts shall be blocked at login (no LIT access) | Must Have |
| FR-A8 | Post-login setup experience with skip option | Should Have |

### A.4 Login Copy Reference

| Element | Copy |
|---------|------|
| Hero headline | Simply faster internet |
| RMN prompt | Let's get you started |
| OTP heading | Verify your number |
| OTP subtext | OTP/Code has been sent to {RMN} |
| Privacy | Before login, I agree to accept Privacy Policy |
| WhatsApp CTA | Login via WhatsApp |
| Setup loading | Please wait, Setting up your experience… |

---

## Module B — Home Dashboard & Quick Actions

### B.1 Purpose

The Home screen is the central hub from which all LIT journeys begin. Quick Action tiles change based on whether the customer has LIT or not.

### B.2 Screens

| Screen ID | Screen Name | Key Elements |
|-----------|-------------|--------------|
| SCR-B01 | Home — Fiber Only | CURRENT PLAN card (200 MBPS, recharge date), Quick Actions, What's New referral banner, bottom nav (Home, Plans, Support, Profile) |
| SCR-B02 | Home — Fiber + LIT | Same as B01; Quick Action shows **"Manage Live TV"** (with "New" badge) instead of "Add Live TV" |
| SCR-B03 | Home — LIT Nudge Overlay | In-card LIT promotion on plan/recharge area |

### B.3 Quick Actions Grid

| Tile | Fiber Only | Fiber + LIT | Action |
|------|------------|-------------|--------|
| My Offer | ✓ | ✓ | View offers |
| Live Chat | ✓ | ✓ | Open chat |
| Add Money | ✓ | ✓ | Wallet top-up |
| Raise Request | ✓ | ✓ | Service request |
| Download Invoice | ✓ | ✓ | Invoice download |
| Wifi Settings | ✓ | ✓ | WiFi management |
| Manage Connection | ✓ | ✓ | Connection settings |
| **Add Live TV** | ✓ (New badge) | — | Start LIT purchase (Module C) |
| **Manage Live TV** | — | ✓ (New badge) | Open Manage LIT (Module D) |

### B.4 CURRENT PLAN Card Elements

| Element | Description |
|---------|-------------|
| Label | CURRENT PLAN |
| Speed | Unlimited Data at {SPEED} (e.g., 200 MBPS) |
| Recharge info | Next Recharge Date — {date} \| {time} |
| CTAs | Recharge, My Offers |
| Expand | Chevron-up to expand/collapse card details |

### B.5 What's New Section

| Element | Copy |
|---------|------|
| Section title | What's New |
| Referral banner | Friendship is rewarding! |
| Referral subtext | Refer your friend & Get 300 Cashback |
| CTA | Know More! |

### B.6 Business Requirements — Home

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-B1 | Home shall display personalized greeting ("Good Morning {Name}!") | Must Have |
| FR-B2 | CURRENT PLAN card shall show speed, recharge date, Recharge and My Offers CTAs | Must Have |
| FR-B3 | Quick Action "Add Live TV" with "New" badge for Fiber-only customers | Must Have |
| FR-B4 | Quick Action "Manage Live TV" with "New" badge for Fiber + LIT customers | Must Have |
| FR-B5 | Bottom navigation: Home, Plans, Support, Profile | Must Have |
| FR-B6 | Notification bell and wallet icons in header | Should Have |
| FR-B7 | What's New promotional banner for referrals | Should Have |

---

## Module C — Existing Fiber, No LIT (Purchase Flows)

### C.1 Purpose

Customers with active fiber but no LIT subscription can discover, evaluate, and purchase LIT through four entry paths designed in the FigJam board.

### C.2 Sub-Flows Overview

| Sub-Flow | Entry Point | Description | Scenario |
|----------|-------------|-------------|----------|
| **C1: LIT Nudge** | Recharge / Plan change in-app card | Contextual upsell during existing journey | 1a, 1b |
| **C2: LIT Add-on Purchase — Standalone** | Quick Action "Add Live TV" | Dedicated first-time LIT purchase | 1 |
| **C3: Recharge + LIT Add-on** | Recharge flow | Add LIT while renewing fiber | 1a |
| **C4: Immediate Change Plan + LIT Add-on** | Plan change flow | Upgrade fiber and add LIT together | 1b |

### C.3 Flow C1: LIT Nudge

**Trigger:** Customer is in Recharge or Plan Change journey  
**Purpose:** Upsell LIT without leaving the primary transaction

| Step | Screen | Elements | Action |
|------|--------|----------|--------|
| 1 | Recharge/Plan screen | LIT upsell card embedded in journey | View nudge |
| 2 | LIT Nudge Card | "Wanna try Live Internet TV?", OTT logos montage, "Live internet TV" label | Tap to explore |
| 3 | LIT Introduction | Full-screen or overlay explaining LIT value (channels + OTT apps) | Tap "Know more" |
| 4 | LIT Pack Selection | Channel packs, pricing, "Activate LIT pack" CTA | Select pack |
| 5 | Summary (bundled) | Fiber recharge/plan + LIT add-on line items, combined total (e.g., ₹8667) | Proceed to pay |

**Nudge Card Copy:**
- Heading: "Wanna try Live Internet TV?"
- Sub-card: "Make Your Plan More Entertaining"
- Subtext: "Add Live TV and enjoy more of what you love."
- CTA: "Add Now"
- Link: "Know more"

### C.4 Flow C2: LIT Standalone Purchase

**Entry:** Home → Quick Action "Add Live TV"  
**Precondition:** Fiber only, no LIT

| Step | Screen | Elements | Action |
|------|--------|----------|--------|
| 1 | Home | "Add Live TV" quick action (New badge) | Tap Add Live TV |
| 2 | LIT Introduction Page | LIT value proposition, cinematic background, OTT partner logos | Explore LIT |
| 3 | LIT Pack Selection | Available packs, channel count, monthly price, "Activate LIT pack" | Select pack |
| 4 | Language/Channel Selection | Same as Manage LIT language grid (shared component) | Select languages |
| 5 | Summary | LIT pack only; fiber expiry date sent for validity alignment | Proceed to pay |
| 6 | Payment | Standard MAPP payment | Complete payment |
| 7 | Confirmation | LIT activated; Home now shows "Manage Live TV" | Return to Home |

**Backend:** MAPP sends current fiber plan expiry date to LIT; places Add/Remove order (action `I`)

### C.5 Flow C3: Recharge + LIT Add-on

**Entry:** Home → Recharge OR CURRENT PLAN card → Recharge  
**Precondition:** Fiber only, no LIT

| Step | Screen | Elements | Action |
|------|--------|----------|--------|
| 1 | Recharge initiation | Standard recharge amount/plan selection | Select recharge |
| 2 | LIT upsell step | "Level up with LIT" or LIT nudge card; checkbox or Add Now | Opt in to LIT |
| 3 | LIT pack selection | Pack tiers with OTT logos | Select LIT pack |
| 4 | Summary | Fiber renewal (current + next period) + LIT add-on itemized | Review total |
| 5 | Payment | Combined charge for TPF + LIT | Proceed to pay |
| 6 | Confirmation | Both fiber renewed and LIT activated | Done |

**Pricing:** Customer charged for current period + next expiry of TPF + LIT  
**Backend:** Add/Remove order with LIT action `I`; expiry date sent for LAMP/LIT redirection

### C.6 Flow C4: Immediate Change Plan + LIT Add-on

**Entry:** Plans → Change Plan  
**Precondition:** Fiber only, customer wants new fiber plan + LIT

| Step | Screen | Elements | Action |
|------|--------|----------|--------|
| 1 | Plan browse | Available fiber plans (50/100/200 Mbps etc.) | Select destination plan |
| 2 | LIT add-on toggle | "Add LIT" card/bundle option on plan selection | Enable LIT |
| 3 | LIT pack selection | Pack selection within plan change context | Select LIT pack |
| 4 | Summary | Destination fiber plan + LIT add-on; bundled pricing | Review |
| 5 | Payment | Combined payment | Proceed to pay |
| 6 | Confirmation | Fiber plan changed + LIT activated | Done |

**Business Rules:**
- FDO change plan NOT allowed
- End date = Current Date + Destination Plan Validity
- MAPP places Change Package order (fiber) + Add/Remove order (LIT action `I`)

### C.7 Screen Inventory — Purchase Flows

| Screen ID | Screen Name | Module | Key Elements |
|-----------|-------------|--------|--------------|
| SCR-C01 | LIT Nudge Card | C1 | Wanna try Live Internet TV?, Add Now, Know more |
| SCR-C02 | LIT Introduction | C1, C2 | Hero imagery, OTT logos, value proposition, Explore CTA |
| SCR-C03 | LIT Pack Selection | C1–C4 | Pack cards, channel count, price, Activate LIT pack |
| SCR-C04 | Recharge + LIT Upsell | C3 | LIT toggle/card within recharge flow |
| SCR-C05 | Change Plan + LIT Bundle | C4 | Fiber plan cards with LIT add-on option |
| SCR-C06 | Bundled Summary | C1, C3, C4 | Fiber line item + LIT line item + taxes + total |
| SCR-C07 | Purchase Success | C1–C4 | Confirmation; updated Home with Manage Live TV |

### C.8 Business Requirements — Purchase

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-C1 | "Add Live TV" quick action visible for Fiber-only customers with "New" badge | Must Have |
| FR-C2 | LIT nudge card shown during Recharge and Plan Change journeys | Must Have |
| FR-C3 | Standalone purchase sends fiber plan expiry date to LIT for validity alignment | Must Have |
| FR-C4 | Recharge + LIT charges current + next TPF period + LIT | Must Have |
| FR-C5 | Change Plan + LIT uses Change Package order; no FDO | Must Have |
| FR-C6 | Summary shows itemized Fiber and LIT charges before payment | Must Have |
| FR-C7 | Post-purchase, Home quick action changes from "Add Live TV" to "Manage Live TV" | Must Have |
| FR-C8 | LIT introduction screen explains channels + OTT value proposition | Should Have |
| FR-C9 | "Know more" link on nudge opens LIT detail/introduction | Should Have |
| FR-C10 | MAPP places Add/Remove order (action `I`) on successful LIT purchase | Must Have |

---

## Module D — Manage LIT (Change Plan + Cancel Plan)

*See Sections 10 and 11 for detailed Manage LIT journeys and screen specifications.*

**Summary:** Fiber + LIT subscribers access via "Manage Live TV" quick action → Action Selector (Change plan / Cancel plan) → full change or cancel flows.

| Sub-Flow | Screens | Scenario Ref |
|----------|---------|--------------|
| Change Plan | SCR-M01 → SCR-M11 (9 screens) | 3, 7, 8, 9 |
| Cancel Plan | SCR-M01 → SCR-M02 → SCR-M10 → SCR-M11 | 6, 10 |

---

## Module E — Existing Fiber + LIT (Renewal & Combined Journeys)

### E.1 Purpose

Customers with both Fiber and LIT need renewal, advance recharge, and fiber plan change experiences that correctly handle the LIT subscription.

### E.2 Sub-Flows

| Sub-Flow | Description | Scenario | LIT Behavior |
|----------|-------------|----------|--------------|
| **E1: Same-Plan Renewal** | Customer renews fiber; LIT renews together | 5 | Combined price from getEndUserDetails |
| **E2: Fiber Change Plan Only** | Customer changes fiber; LIT unchanged | 2 | LIT unmodifiable; validity re-aligned |
| **E3: Advance Renewal** | Customer renews before expiry | 5 | Combined Fiber + LIT pricing |
| **E4: Paused & Resumed + LIT** | Fiber was paused, now resumed | 12 | Prorated + total; Add/Remove order |
| **E5: Combined Payment Review** | Summary with multiple services | — | Itemized LIT + other add-ons |

### E.3 Flow E1: Recharge / Advance Renewal (Fiber + LIT)

| Step | Screen | Elements | Action |
|------|--------|----------|--------|
| 1 | Home | CURRENT PLAN card, "Manage Live TV" visible | Tap Recharge |
| 2 | Renewal summary | Combined Fiber + LIT renewal price (from getEndUserDetails) | Review |
| 3 | Summary | Fiber plan line + LIT add-on line + "Current LIT add on charge" | Proceed to pay |
| 4 | Payment | Single payment for both services | Pay |
| 5 | Confirmation | Both renewed to same validity end date | Done |

### E.4 Flow E2: Fiber Change Plan Only (LIT Retained)

| Step | Screen | Elements | Action |
|------|--------|----------|--------|
| 1 | Plans → Change Plan | Fiber plan options; **no LIT modification** | Select new fiber plan |
| 2 | Comparison | Current vs. new fiber plan; note "Your TV plan will remain unchanged" | Confirm |
| 3 | Summary | Fiber plan change only; LIT line shows existing pack (read-only) | Proceed |
| 4 | Payment | Fiber plan price difference only | Pay |
| 5 | Confirmation | Fiber updated; LIT remains active; validity aligned | Done |

**Restrictions:** LIT redirection blocked during fiber-only plan change; combined Fiber + LIT change NOT supported (Scenario 4)

### E.5 Flow E4: Paused & Resumed Fiber + LIT Continue

| Step | Action | System Behavior |
|------|--------|-----------------|
| 1 | Customer logs into MAPP (resumed fiber) | App accessible |
| 2 | Navigate to LIT / Manage Live TV | Redirect to LIT platform |
| 3 | LIT calculates prorated + total based on expiry | Display pricing |
| 4 | Customer confirms | MAPP places Add/Remove order |
| 5 | HOBS fulfills | LIT entitlement restored |

**Blocked:** Paused but NOT resumed / Suspended — no app login (Scenario 13)

### E.6 Combined Payment Review Screens

The design includes summary screens for multi-service checkout:

| Screen | Services Shown | Example Pricing |
|--------|----------------|-----------------|
| LIT + Fiber Summary | LIT pack (538 channels, ₹2382) + Fiber renewal | ₹8667 total |
| Static IP Summary | Static IP add-on (₹200/month, prorated ₹14) | ₹17 total |
| Data Packs Summary | Data pack validity-based | ₹120 total |

### E.7 Business Requirements — Fiber + LIT

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-E1 | getEndUserDetails returns combined Fiber + LIT renewal price | Must Have |
| FR-E2 | Renewal summary shows "Current LIT add on charge" as separate line item | Must Have |
| FR-E3 | Fiber-only plan change hides/disables LIT modification options | Must Have |
| FR-E4 | Existing LIT remains active after fiber plan change; validity aligned | Must Have |
| FR-E5 | Combined Fiber + LIT plan change in single transaction blocked | Must Have |
| FR-E6 | Paused & resumed customers get prorated LIT pricing on continuation | Must Have |
| FR-E7 | Suspended customers cannot log in or access LIT | Must Have |
| FR-E8 | Summary screen supports multiple add-on line items (LIT, Static IP, Data Packs) | Should Have |

---

## Module F — Autopay

### F.1 Purpose

Fiber autopay customers who purchase LIT need clarity on how LIT charges interact with their automandate. The Autopay module in the design covers setup, management, and cancellation.

### F.2 Screens

| Screen ID | Screen Name | Key Elements |
|-----------|-------------|--------------|
| SCR-F01 | Autopay Dashboard | Current autopay status, linked plan, next debit date |
| SCR-F02 | Cancel Autopay | Confirmation flow for cancelling autopay mandate |
| SCR-F03 | Autopay + LIT Query State | Information on whether LIT is included in automandate (TBD) |

### F.3 Business Requirements — Autopay

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-F1 | When autopay customer purchases LIT standalone, system shall determine automandate inclusion | Must Have (TBD) |
| FR-F2 | Autopay cancellation shall not automatically cancel LIT (separate subscriptions) | Should Have |
| FR-F3 | Autopay changes (16 Sep design) shall be reflected per updated design spec | Must Have |
| FR-F4 | Customer shall see clear messaging if LIT is/is not part of autopay debit | Should Have |

**Open Question (Q4):** Will LIT price be automatically included in the automandate file for standalone LIT purchase?

---

## Module G — Payment & Summary (Shared Component)

### G.1 Purpose

A consistent Summary and Payment pattern is used across all LIT and fiber transactions. This module defines the shared UI component specifications.

### G.2 Summary Screen Pattern

| Element | Specification |
|---------|---------------|
| Header | Back arrow + "Summary" title |
| Service Card | Label badge (pack/service name), price, duration breakdown |
| Edit Action | Pencil icon — navigate back to selection |
| Remove Action | Trash icon — remove item or trigger cancel |
| Expand | Chevron-up on footer expands card to show specs, tags, NCF breakdown |
| Sticky Footer | Left: total price with expand toggle; Right: "Proceed to pay" (magenta CTA) |

### G.3 Itemized Billing Structure

| Line Item | Example | When Shown |
|-----------|---------|------------|
| Fiber Plan | 200 MBPS — ₹5,999/6 months | Recharge, plan change |
| LIT Add-on | 538 TV Channels — ₹2,382 (₹397 × 6 months) | Any LIT purchase/change |
| Current LIT add-on charge | ₹399/month | Renewal with existing LIT |
| Static IP | ₹200/month (prorated ₹14) | Add-on purchase |
| NCF | Includes Rs 153 network fee | LIT packs |
| Taxes (GST) | As applicable | All payments |
| Prorated upgrade | ₹180 for remaining period | LIT upgrade mid-cycle |
| **Total** | ₹8,667 | Footer |

### G.4 Payment Success / Failure

| State | UI Treatment |
|-------|--------------|
| Success | Green checkmark, transaction ID, "Back to Home" CTA |
| Failure | Error message, retry CTA, support link |
| Pending | Loading indicator, "Processing your payment…" |

### G.5 Business Requirements — Payment

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-G1 | All LIT transactions show itemized summary before payment | Must Have |
| FR-G2 | Summary supports multiple line items (fiber + LIT + add-ons) | Must Have |
| FR-G3 | Expandable summary card shows full pack specs and genre tags | Must Have |
| FR-G4 | Sticky footer displays total and "Proceed to pay" on all payment screens | Must Have |
| FR-G5 | Payment success returns customer to Home with updated state | Must Have |
| FR-G6 | Payment failure does not submit HOBS order | Must Have |
| FR-G7 | Prorated amounts shown as separate line item when applicable | Must Have |

---

## Module H — Promotions & Cross-Sell

### H.1 Screens

| Screen ID | Screen Name | Elements |
|-----------|-------------|----------|
| SCR-H01 | Cashback Offer | "Get free one month as cashback" promotion |
| SCR-H02 | Referral Banner | "Friendship is rewarding!", "Refer your friend & Get 300 Cashback" |
| SCR-H03 | Manage Services Promotion | Service promotion when no add-ons subscribed (Scenario 18) |

### H.2 Business Requirements — Promotions

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-H1 | Manage Services page promotes LIT, WiFi+, Static IP when customer has no add-ons | Must Have |
| FR-H2 | Referral banner on Home "What's New" section | Should Have |
| FR-H3 | Cashback promotion displayed per campaign rules | Should Have |

---

## Complete Screen Index (All Modules)

| Screen ID | Module | Screen Name |
|-----------|--------|-------------|
| SCR-A01–A09 | Login | Authentication flows |
| SCR-B01–B03 | Home | Dashboard variants |
| SCR-C01–C07 | Purchase | LIT acquisition flows |
| SCR-M01–M11 | Manage LIT | Change/Cancel flows |
| SCR-E01–E05 | Fiber + LIT | Renewal/change flows |
| SCR-F01–F03 | Autopay | Autopay management |
| SCR-G01–G04 | Payment | Summary/Payment/Success/Failure |
| SCR-H01–H03 | Promotions | Cross-sell |

**Total unique screens across design: ~45+**

---

## Design-to-Scenario Traceability Matrix

| Design Module | Flow | Scenario # | Customer State |
|---------------|------|------------|----------------|
| C2 Standalone Purchase | Add Live TV → Intro → Pack → Pay | 1 | Fiber, No LIT |
| C3 Recharge + LIT | Recharge → LIT upsell → Pay | 1a | Fiber, No LIT |
| C4 Change Plan + LIT | Plan change → LIT bundle → Pay | 1b | Fiber, No LIT |
| E2 Fiber Change Only | Plan change (LIT locked) | 2 | Fiber + LIT |
| D Change Plan | Manage Live TV → Change | 3, 7, 8, 9 | Fiber + LIT |
| — Combined change blocked | — | 4, 11 | Fiber + LIT |
| E1 Renewal | Recharge combined price | 5 | Fiber + LIT |
| D Cancel Plan | Manage Live TV → Cancel | 6, 10 | Fiber + LIT |
| E4 Paused/Resumed | LIT continuation | 12 | Fiber + LIT (paused) |
| — Suspended blocked | Login blocked | 13 | Suspended |
| — Entitlement display | Manage Plan / Home | 14, 15 | All |
| F Autopay + LIT | Autopay purchase | 17 | Fiber Autopay |
| H Manage Services | Service promotion | 18 | No add-ons |
| — Recharge for others | Continue only | 19 | Third-party |
