# Codex Work Package (CWP) framework

This project uses **Codex Work Packages (CWPs)** to keep local CAD automation bounded, reproducible, and quota-aware.

## Why CWPs exist

Open-ended agent sessions can mix planning, research, execution, recovery, documentation, and unrelated cleanup. For Fusion automation that is undesirable: it makes tests harder to reproduce and can waste limited agent usage.

A CWP separates planning from execution. ChatGPT or a human can define the test; Codex executes only the bounded local task against Fusion and reports evidence.

## Core operating rule

A normal CWP should have:

- one objective;
- measurable acceptance criteria;
- an expected starting-state fingerprint;
- explicit preflight checks;
- a bounded mutation budget;
- independent verification;
- an explicit stop condition.

Do not add opportunistic improvements, unrelated cleanup, architecture redesign, or web research unless the CWP explicitly authorizes them.

## Recommended flow

```text
Natural-language requirement / test goal
                ↓
Planning and specification
                ↓
        Codex Work Package
                ↓
             Preflight
                ↓
      Read-only diagnosis/audit
                ↓
       Planned CAD mutation
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

## Baseline fingerprint

Before a mutation CWP, record enough state to prove the intended model is active and uncontaminated. Depending on the test, include:

- document name;
- body count;
- parameter names/count and critical values;
- sketch count;
- timeline feature count;
- critical dimensions/feature locations;
- origin/coordinate-frame anchor state;
- feature health;
- known-good bounding box or BRep measurements.

If the starting state materially differs, stop with `PRECONDITION FAIL` rather than attempting recovery inside an unrelated CWP.

## Preflight vs diagnosis vs mutation

CWP-008 demonstrated that not every failure should consume the mutation retry budget.

### Preflight blockers

Examples:

- modal Fusion dialog open;
- wrong active document;
- Fusion temporarily busy;
- required tool temporarily unavailable.

These are not CAD mutation attempts.

### Read-only diagnostics

Examples:

- parameter inspection;
- sketch-dimension inspection;
- constraint-topology audit;
- coordinate-frame audit;
- BRep measurement;
- feature-health inspection.

These do not consume the mutation retry budget.

### CAD mutation attempts

Examples:

- changing a parameter expression;
- adding/removing/rebinding a driving dimension;
- adding/removing a geometric constraint;
- modifying sketch-driving logic.

Unless a CWP explicitly states otherwise, allow a maximum of **two targeted mutation attempts**.

## Mutation discipline

Prefer one mutation at a time:

1. make one targeted change;
2. recompute Fusion;
3. verify sketch and timeline health;
4. confirm expected body/parameter counts;
5. continue only if the model remains healthy.

Do not stack multiple speculative changes and diagnose only afterward.

If one change causes an unhealthy sketch or feature, revert that change before trying the permitted alternate strategy.

## Constraint-safe parameter binding

CWP-008 established these rules:

1. Audit the existing constraint graph before adding driving dimensions.
2. Rebind existing driving dimensions where possible rather than adding parallel constraints.
3. Distinguish global coordinate position from edge-relative or feature-relative dimensions.
4. Intentionally anchor the model coordinate frame when absolute placement matters.
5. Prefer semantic design variables and derived relationships over independent raw coordinates.

Example validated intent binding:

```text
hole_edge_offset = 25 mm

Hole 1 X = hole_edge_offset
Hole 2 X = plate_length - hole_edge_offset
Hole Y   = plate_width / 2
```

This is preferred over independent `hole_1_x`, `hole_2_x`, and `hole_centerline_y` values when the actual design intent is symmetric end offsets on a longitudinal centerline.

## Structured CAD specification

Design intent should pass through an auditable intermediate specification before Fusion mutation.

Prefer intent-oriented schemas where practical.

Example:

```yaml
part:
  name: mounting_plate
  units: mm

body:
  type: rectangular_plate
  length: 100
  width: 60
  thickness: 12

holes:
  type: through
  diameter: 8
  count: 2
  layout:
    type: symmetric_end_offsets
    edge_offset: 25
    centerline: longitudinal
```

The application layer may derive Fusion-driving expressions such as:

```text
hole_1_x = hole_edge_offset
hole_2_x = plate_length - hole_edge_offset
hole_y = plate_width / 2
```

The specification should be validated before modeling or regeneration.

## Controlled refactor rule

Do not rebuild a sketch or model merely to bypass a failed constraint operation.

A narrowly scoped refactor is allowed only when read-only analysis demonstrates that the current topology cannot safely express the intended design, and only if:

1. the reason is documented;
2. the previous known-good state is recoverable;
3. only the minimum necessary dimensions/constraints/features are changed;
4. geometry is independently verified afterward.

## Standard CWP template

```text
CWP-### — Title

Objective:
[one bounded outcome]

Baseline fingerprint:
[required known-good starting state]

Inputs:
[file paths, document names, structured specification]

Preflight:
[conditions that must be true before mutation]

Read-only diagnosis, if required:
[constraint/parameter/feature audit]

Allowed mutation:
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
- Preflight and read-only diagnostics do not count as mutation attempts.
- Maximum two targeted mutation attempts unless explicitly overridden.
- If the second true mutation attempt fails, stop and report.

Restrictions:
- Do not ...
- Do not continue to the next CWP.

Required report:
Status: PASS / PARTIAL / FAIL / PRECONDITION FAIL / BLOCKED
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

## Failure preservation

Do not overwrite a failed result simply because a recovery later succeeds.

Record:

- original failure;
- precondition failures separately from CAD failures;
- read-only diagnostic findings;
- recovery steps;
- the final successful bounded test.

This preserves engineering evidence and allows procedures to improve from observed Fusion behavior.

## Test record fields

Each completed CWP should record, when available:

- CWP ID and title;
- date;
- Fusion version;
- OpenAI client/version;
- baseline fingerprint;
- starting document;
- natural-language request;
- structured specification;
- exact execution instruction;
- expected result;
- actual result;
- independent measurements;
- verification method;
- screenshots or public sample artifacts;
- preflight blockers;
- read-only diagnostics;
- mutation attempts;
- errors and recovery steps;
- model used, if known;
- Codex usage/status before and after, if available;
- PASS / PARTIAL / FAIL / PRECONDITION FAIL / BLOCKED.

## Quota-efficiency metric

The project may track **VCO/A — Verified CAD Operations per unit of Codex Allowance**.

The objective is not to minimize messages in isolation; it is to maximize independently verified useful CAD operations for the available execution allowance.

Read-only diagnosis can be quota-efficient when it prevents repeated failed mutations. The CWP-008 recovery sequence is an example: a coordinate-frame audit revealed the missing origin anchor and avoided further speculative edits.

## Current CWP sequence

- CWP-002 — bracket creation — PASS
- CWP-003 — parameter modification and independent thickness verification — PASS
- CWP-004 — STEP export — PASS
- CWP-005 — STEP round-trip verification — PASS
- CWP-006 — natural-language-to-structured-CAD specification — PASS
- CWP-007 — structured-spec regeneration — PASS
- CWP-008 initial schema binding — FAIL; redundant driving constraint exposed
- CWP-008R1 — coordinate-frame/constraint audit — PASS
- CWP-008R2 — origin-anchor stabilization — PASS
- CWP-008B — intent-based parameter binding — PASS
- CWP-009 — input validation and safe rejection — NEXT

The historical initial modeling test predates the formal CWP numbering and remains documented separately.
