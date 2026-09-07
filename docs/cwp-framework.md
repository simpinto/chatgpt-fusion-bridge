# Codex Work Package (CWP) framework

This project uses **Codex Work Packages (CWPs)** to keep local CAD automation bounded, reproducible, and quota-aware.

## Why CWPs exist

Open-ended agent sessions can mix planning, research, execution, recovery, documentation, and unrelated cleanup. For Fusion automation that is undesirable: it makes tests harder to reproduce and can waste limited agent usage.

A CWP separates planning from execution. ChatGPT or a human can define the test; Codex executes only the bounded local task against Fusion and reports evidence.

## Core operating rule

A normal CWP should have:

- **one objective**;
- **one measurable output**;
- **one acceptance test**;
- **maximum two recovery attempts**;
- an explicit **stop condition**.

Do not add opportunistic improvements, unrelated cleanup, architecture redesign, or web research unless the CWP explicitly authorizes them.

## Recommended flow

```text
Natural-language requirement / test goal
                ↓
Planning and specification
                ↓
        Codex Work Package
                ↓
             Codex
                ↓
          Autodesk Fusion MCP
                ↓
              Fusion
                ↓
       Independent verification
                ↓
        PASS / PARTIAL / FAIL
                ↓
      Testing journal / checkpoint
```

## Standard CWP template

```text
CWP-### — Title

Objective:
[one bounded outcome]

Prerequisites:
[required starting state]

Inputs:
[file paths, document names, structured specification]

Allowed actions/tools:
[only what is needed]

Procedure:
1. ...
2. ...
3. ...

Independent verification:
[measure/read/inspect resulting geometry or file]

PASS criteria:
- ...

FAIL criteria:
- ...

Recovery policy:
- Maximum two attempts.
- If the second attempt fails, stop and report.

Restrictions:
- Do not ...
- Do not continue to the next CWP.

Required report:
Status: PASS / PARTIAL / FAIL
Observed result:
Verification method:
Unexpected behavior:
```

## Verification hierarchy

Prefer evidence in this order where practical:

1. **Independent geometry interrogation** — BRep measurements, face geometry, bounding boxes, topology, volume, feature health.
2. **Round-trip verification** — export, reimport, and remeasure.
3. **Fusion inspection/measure tools** — explicit measured distances/diameters.
4. **Parameter table** — useful input evidence, but not sufficient alone to prove final geometry.
5. **Screenshot** — corroborating visual evidence, not dimensional proof by itself.

## Two-attempt recovery policy

When execution fails:

1. attempt the obvious safe correction;
2. try one reasonable alternative if required;
3. after the second failure, stop and return a concise failure report.

Do not let a bounded CWP turn into open-ended troubleshooting. Analyze difficult failures outside the execution task, then issue a new CWP if needed.

## Structured CAD specification

From CWP-006 onward, design intent should increasingly pass through an auditable intermediate specification before Fusion mutation.

Example:

```yaml
part:
  name: mounting_plate
  units: mm

body:
  type: rectangular_plate
  length: 80
  width: 40
  thickness: 8

holes:
  type: through
  diameter: 6
  count: 2
  centers:
    - [15, 20]
    - [65, 20]
```

The specification should be validated before modeling. Later CWPs will define explicit schema-to-Fusion parameter bindings and safe rejection rules.

## Test record fields

Each completed CWP should record, when available:

- CWP ID and title;
- date;
- Fusion version;
- OpenAI client/version;
- starting document;
- natural-language request;
- structured specification;
- exact execution instruction;
- expected result;
- actual result;
- independent measurements;
- verification method;
- screenshots or public sample artifacts;
- errors and recovery steps;
- model used, if known;
- Codex usage/status before and after, if available;
- PASS / PARTIAL / FAIL.

## Quota-efficiency metric

The project may track **VCO/A — Verified CAD Operations per unit of Codex Allowance**.

The objective is not to minimize messages in isolation; it is to maximize independently verified useful CAD operations for the available execution allowance.

Useful operation examples include:

- successful Fusion reads;
- created features;
- parameter updates;
- independent dimension checks;
- exports;
- successful round-trip imports;
- validated manufacturing features.

## Current CWP sequence

- CWP-002 — bracket creation — PASS
- CWP-003 — parameter modification and independent thickness verification — PASS
- CWP-004 — STEP export — PASS
- CWP-005 — STEP round-trip verification — PASS
- CWP-006 — natural-language-to-structured-CAD specification — PASS
- CWP-007 — structured-spec regeneration — NEXT

The historical initial modeling test predates the formal CWP numbering and remains documented separately.
