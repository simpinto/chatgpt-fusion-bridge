# Testing journal

## 2026-09-06 — Research baseline

Documentation was reviewed and two possible connection approaches were identified. No connection to a live Fusion session was tested. No geometry was generated, measured, or exported by this project.

## 2026-09-06 — First local read-only probe passed

- Environment: Windows; Codex CLI 0.153.1 available. Fusion was already running with MCP enabled. Fusion version and license category were not established.
- Connection: local HTTP at `http://127.0.0.1:27182/mcp`.
- Method: JSON-RPC requests from PowerShell, not yet native Codex tool dispatch.
- Initialization: succeeded using MCP protocol 2024-11-05; server identified itself as MCP Server Adapter 1.0.0.
- Tool discovery: succeeded. Advertised tools included `fusion_mcp_read`, `fusion_mcp_execute`, `fusion_mcp_update`, and `fusion_mcp_electronics_read`.
- Read test: `fusion_mcp_read` with `{"queryType":"document","operation":"open"}` succeeded and reported one active, unmodified, unsaved document.
- An initial HTTP GET returned 405; JSON-RPC POST requests succeeded. A rejected GET alone does not establish that the server is unavailable.
- No design changes, screenshot capture, saves, or exports were performed.
- Added a persistent `mcp_servers.fusion` entry using the local endpoint and a 120-second tool timeout. Restart/native tool discovery remained to be verified.
- Outcome: transport, discovery, and one read operation passed. Full client integration remained partial at this point.

## 2026-09-06 — Native desktop connection passed after restart

- The user restarted Codex while Fusion remained open.
- Fusion tools were present in the native tool catalog and invoked directly; no PowerShell HTTP fallback was used for these tests.
- Open-document query: succeeded; one active, unmodified, unsaved document.
- Active-command query: default Select command; no interactive command dialog reported.
- API documentation query: succeeded.
- Read-only script: succeeded and reported Fusion version 2705.1.11, a Fusion design, zero root bodies, zero root sketches, and zero component occurrences.
- No geometry changes, screenshots, saves, or exports were performed.
- Outcome: native discovery, read calls, documentation access, and read-only script execution passed.

## 2026-09-06 / 2026-09-07 — CWP baseline series

The project adopted bounded **Codex Work Packages (CWPs)**: one objective, one measurable result, explicit acceptance criteria, a maximum two-attempt recovery policy, and a stop condition. The intent is to reduce unnecessary autonomous exploration and improve reproducibility and quota efficiency.

### CWP-002 — Bracket creation

**Status: PASS**

- A disposable Fusion mounting plate model was created with two through-holes.
- A named user parameter `plate_thickness` was present.
- At the start of the later regeneration test, `plate_thickness` was 6 mm.
- Visual evidence confirmed the plate, holes, and parameter table.
- This test established creation of editable geometry; independent dimensional checks were handled by subsequent CWPs.

### CWP-003 — Parameter modification and independent verification

**Status: PASS**

- Requested change: `plate_thickness` from 6 mm to 10 mm.
- Fusion recomputed the model.
- Independent verification used Fusion's Measure tool on geometry rather than trusting the parameter field alone.
- Measured distance: **10.00 mm**.
- Selected vertices showed Z positions of 0.00 mm and 10.00 mm.
- Outcome: parameter change propagated correctly to BRep geometry.

### CWP-004 — Manufacturing interchange: STEP export

**Status: PASS — export artifact structurally verified**

- Export artifact: `outputs/bracket-test/CWP-004-mounting-plate.step`.
- STEP content identified product `Fusion Bridge - Mounting Plate Test`.
- Units: millimeters (`SI_UNIT(.MILLI.,.METRE.)`).
- Geometry envelope in the STEP data was consistent with **60 × 30 × 10 mm**.
- Hole-center-related geometry was visible near `(10,15)` and `(50,15)` mm.
- File termination included `END-ISO-10303-21;`.
- Round-trip readability was intentionally reserved for CWP-005.

### CWP-005 — STEP round-trip verification

**Status: PASS**

Input:
`outputs/bracket-test/CWP-004-mounting-plate.step`

Verification:

- Fusion STEP `ImportManager` imported the file into a new disposable document.
- One imported BRep body existed.
- The body was a valid solid with nonzero volume.
- Measured dimensions: **60.00 × 30.00 × 10.00 mm**.
- Hole count: **2**.
- Hole centers: **(10.00, 15.00)** and **(50.00, 15.00)** mm.
- Two cylindrical Z-axis through-hole faces were identified.
- Imported base-feature health: healthy.
- Geometry integrity: OK.
- The disposable imported document was named `Untitled`, which was normal for the chosen import path.

This completed the baseline manufacturing-neutral round trip:

**Fusion source → STEP export → new Fusion document → valid BRep → independent geometry verification**.

### CWP-006 — Natural-language-to-structured-CAD specification

**Status: PASS**

Natural-language request:

> Create a rectangular mounting plate that is 80 mm long, 40 mm wide, and 8 mm thick. Add two 6 mm diameter through-holes. Place both holes on the longitudinal centerline of the plate. The first hole center must be 15 mm from the left edge and the second hole center must be 15 mm from the right edge.

Structured specification:

```yaml
part:
  name: CWP-006-mounting-plate
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

Specification validation:

- `80 - 15 = 65 mm`.
- Plate centerline in Y = 20 mm.
- All requested dimensions and hole locations matched the interpreted structured specification.

Fusion verification:

- Separate disposable document: `CWP-006-mounting-plate`.
- Valid solid BRep: YES.
- Length: **80.00 mm**.
- Width: **40.00 mm**.
- Thickness: **8.00 mm**.
- Hole count: **2**.
- Hole diameter: **6.00 mm**.
- Hole centers: **(15.00, 20.00)** and **(65.00, 20.00)** mm.
- Both holes span from Z = 0.00 mm through Z = 8.00 mm.
- Body has nonzero volume.
- Fusion features were healthy.
- Unexpected behavior: none.

This established the first tested abstraction pipeline:

**natural language → structured CAD specification → Fusion model → independent BRep verification**.

## Current validated capability chain

**CONNECT → CREATE → MODIFY → EXPORT STEP → ROUND-TRIP VERIFY → NATURAL LANGUAGE → STRUCTURED CAD SPECIFICATION → VERIFIED MODEL**

## Next planned test

### CWP-007 — Structured-spec regeneration

Test whether a revised structured specification can update an existing parametric Fusion model without rebuilding it from scratch. The regenerated model must then pass independent geometry verification.

The purpose is to prove configuration-driven CAD rather than one-shot model generation.

## Template for future tests

- CWP ID and title:
- Date:
- Operating system:
- Fusion version and license category:
- OpenAI client and version:
- Connection method:
- Model, if known:
- Starting document (use a disposable sample):
- Natural-language request, if applicable:
- Structured specification, if applicable:
- Exact execution prompt:
- Expected result:
- Actual result:
- Independent measurements or export checks:
- Verification method:
- Evidence (redacted screenshots or public sample files):
- Errors and recovery steps:
- Codex usage/status before and after, when available:
- Outcome: PASS / PARTIAL / FAIL / NOT TESTED

Never include API keys, passwords, private account identifiers, or confidential designs. A screenshot alone is not evidence that all dimensions are correct; record independent measurements where relevant.

## Historical first modeling report

An earlier 4-to-6 mm modeling/export test is preserved in [first-modeling-test.md](first-modeling-test.md). It remains useful as the first observed automation and recovery record. The later CWP series above is the current bounded-test framework and should be treated separately rather than rewriting that historical result.
