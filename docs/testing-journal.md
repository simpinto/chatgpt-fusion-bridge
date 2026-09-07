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
- Added a persistent `mcp_servers.fusion` entry using the local endpoint and a 120-second tool timeout.
- Outcome: transport, discovery, and one read operation passed.

## 2026-09-06 — Native desktop connection passed after restart

- Fusion tools were present in the native Codex tool catalog and invoked directly.
- Open-document, active-command, API-documentation, and read-only script checks succeeded.
- Fusion version reported: 2705.1.11.
- Outcome: native discovery and read-only execution passed.

## 2026-09-06 / 2026-09-07 — CWP baseline series

The project adopted bounded **Codex Work Packages (CWPs)**: one objective, measurable acceptance criteria, explicit stop conditions, limited recovery, and independent verification.

### CWP-002 — Bracket creation

**Status: PASS**

- A disposable mounting plate with two through-holes was created.
- A named `plate_thickness` user parameter existed.
- Visual evidence confirmed the plate, holes, and parameter table.

### CWP-003 — Parameter modification and independent verification

**Status: PASS**

- `plate_thickness` changed from 6 mm to 10 mm.
- Fusion recomputed.
- Independent geometry measurement verified **10.00 mm** thickness.

### CWP-004 — Manufacturing interchange: STEP export

**Status: PASS — export artifact structurally verified**

- Artifact: `outputs/bracket-test/CWP-004-mounting-plate.step`.
- STEP units: millimeters.
- STEP geometry envelope was consistent with **60 × 30 × 10 mm**.
- Hole-center-related geometry appeared near `(10,15)` and `(50,15)` mm.
- File terminated correctly with `END-ISO-10303-21;`.

### CWP-005 — STEP round-trip verification

**Status: PASS**

- Fusion STEP `ImportManager` imported the file into a separate disposable document.
- One valid solid BRep with nonzero volume was created.
- Measured dimensions: **60.00 × 30.00 × 10.00 mm**.
- Hole centers: **(10.00,15.00)** and **(50.00,15.00)** mm.
- Imported base feature was healthy.

### CWP-006 — Natural-language-to-structured-CAD specification

**Status: PASS**

Natural-language intent was translated into a structured specification for an 80 × 40 × 8 mm plate with two Ø6 mm through-holes at `(15,20)` and `(65,20)` mm. Fusion created a separate solid BRep and independent geometry interrogation confirmed all requested dimensions and hole locations.

This established:

**natural language → structured CAD specification → Fusion model → independent BRep verification**.

### CWP-007 — Structured-spec regeneration

**Status: PASS**

The existing CWP-006 model was reused and regenerated from a revised specification rather than rebuilt.

Changes:

- `plate_length`: 80 → 100 mm
- `plate_width`: 40 → 50 mm
- `plate_thickness`: 8 → 12 mm
- `hole_diameter`: 6 → 8 mm
- hole centers updated to `(20,25)` and `(80,25)`

Verification:

- same original body remained;
- original sketch and extrusion remained in the timeline;
- duplicate bodies: none;
- duplicate parameters: none;
- final body count: 1;
- measured geometry: **100 × 50 × 12 mm**;
- two Ø8 mm through-holes at `(20,25)` and `(80,25)`;
- relevant features healthy.

This established configuration-driven regeneration of an existing model.

## CWP-008 — Schema-binding attempt and recovery findings

CWP-008 required several bounded attempts before the final intent-based binding passed. The failures are retained because they exposed important Fusion constraint and workflow behavior.

### Initial CWP-008 attempt

**Status: FAIL**

- First blocker: Fusion's Change Parameters dialog was open. No geometry mutation occurred.
- After the dialog was closed, the first true CAD mutation failed with `VCS_SKETCH_OVER_CONSTRAINTS` while adding a new driving linear distance to already-constrained sketch geometry.
- Key lesson: do not add parallel driving dimensions before auditing the existing constraint graph.

### Revised CWP-008 preflight

**Status: PRECONDITION FAIL**

The revised procedure stopped before mutation because the active model no longer matched the validated CWP-007 baseline. Residual parameters from the failed binding attempt remained:

- `hole_1_x = 25 mm`
- `hole_2_x = 75 mm`
- `hole_centerline_y = 20 mm`

The holes were at `(25,25)` and `(75,25)`. The stop-on-precondition rule prevented further contamination.

### CWP-008R0 — Baseline rollback

**Status: FAIL — partial rollback succeeded, absolute coordinate restoration did not**

Rollback actions:

- restored positional driving-dimension expressions;
- removed the three residual positional parameters after they became unreferenced;
- restored the four original core parameters.

Final dimensions remained correct at **100 × 50 × 12 mm**, but hole centers became `(20,30)` and `(80,30)` rather than `(20,25)` and `(80,25)`.

This indicated a coordinate-frame problem rather than an internal dimension problem.

### CWP-008R1 — Coordinate-frame and constraint audit

**Status: PASS — read-only diagnostic**

Observed global bounding box:

- X: 0 → 100 mm
- Y: 5 → 55 mm
- Z: 0 → 12 mm

Observed hole centers:

- `(20,30)`
- `(80,30)`

Edge-relative hole offsets were still correct:

- 20 mm from left/right edges;
- 25 mm above the lower plate edge.

Constraint audit found:

- lower-left plate corner was at `(0,5)` rather than the sketch origin;
- no plate corner or rectangle center was anchored to the origin;
- the sketch was under-constrained;
- the plate outline and holes could translate together;
- hole-position dimensions were edge-relative to the lower-left plate corner, not global coordinates.

Diagnosis:

- whole-sketch translation / missing origin anchor;
- edge-relative hole dimensions;
- under-constrained sketch allowed solver translation.

No mutations were performed.

### CWP-008R2 — Origin anchor recovery and baseline stabilization

**Status: PASS**

One targeted mutation was performed:

- added one coincident constraint between the existing lower-left plate corner and the existing sketch origin.

Results:

- origin anchor: YES;
- final bounding box: X 0→100, Y 0→50, Z 0→12 mm;
- hole centers restored to `(20,25)` and `(80,25)`;
- final parameters returned to exactly four core parameters;
- body count remained 1;
- features remained healthy;
- whole-sketch translation was eliminated;
- sketch still reported UNDER-CONSTRAINED, but the translational degree of freedom relevant to this failure was removed.

### CWP-008B — Intent-Based Parameter Binding

**Status: PASS**

The stabilized model was converted from independent coordinate control to semantic design-intent control.

Added semantic parameter:

- `hole_edge_offset = 20 mm`

Existing positional dimensions were rebound in place:

- hole 1 X → `hole_edge_offset`
- hole 1 Y → `plate_width / 2`
- hole 2 X → `plate_length - hole_edge_offset`
- hole 2 Y → `plate_width / 2`

No new driving constraints were added and no over-constraint occurred.

Regeneration Test A:

- changed `hole_edge_offset` 20 → 25 mm;
- measured hole centers became `(25,25)` and `(75,25)`;
- plate remained 100 × 50 × 12 mm;
- Ø8 mm through-hole behavior remained invariant.

Regeneration Test B:

- changed `plate_width` 50 → 60 mm;
- derived centerline became Y = 30 mm automatically;
- measured hole centers became `(25,30)` and `(75,30)`;
- no direct positional sketch edit was required.

Final validated state:

- `plate_length = 100 mm`
- `plate_width = 60 mm`
- `plate_thickness = 12 mm`
- `hole_diameter = 8 mm`
- `hole_edge_offset = 25 mm`
- body count = 1
- origin anchor intact
- sketch state = UNDER-CONSTRAINED
- feature health = HEALTHY
- direct positional sketch editing required for tested layout changes = NO

### Consolidated findings from CWP-008

1. **Preflight failures are not CAD mutation attempts.** Modal dialogs, wrong active documents, and temporary tool blockers must be classified separately from actual modeling failures.
2. **Read-only diagnostics should not consume the mutation retry budget.** Constraint topology and coordinate-frame audits are often cheaper than trial-and-error edits.
3. **Do not add redundant driving constraints.** Rebind existing dimensions whenever possible.
4. **Use a baseline fingerprint before mutation.** Check document, body count, parameter names/count, critical dimensions, origin anchor, and feature health before continuing.
5. **Separate coordinate frame from design dimensions.** Edge-relative dimensions can remain correct even when an under-constrained sketch translates globally.
6. **Anchor the model coordinate frame intentionally.** A minimal origin constraint removed the whole-sketch translational freedom without rebuilding the model.
7. **Prefer semantic design variables over raw coordinates.** `hole_edge_offset` plus derived expressions preserved symmetry and centerline intent more robustly than independent X/Y parameters.
8. **Mutate incrementally.** Change one driver, recompute, verify health, then continue.
9. **Preserve failed attempts as engineering evidence.** The recovery sequence materially improved the project's CAD-agent procedure.

## Current validated capability chain

**CONNECT → CREATE → MODIFY → EXPORT STEP → ROUND-TRIP VERIFY → NATURAL LANGUAGE → STRUCTURED CAD SPECIFICATION → REGENERATE EXISTING MODEL → CONSTRAINT-SAFE INTENT BINDING → VERIFIED MODEL**

## Next planned test

### CWP-009 — Input validation and safe rejection

Test whether invalid structured specifications are rejected before Fusion mutation. Candidate cases include negative dimensions, impossible hole sizes, out-of-bounds feature locations, and conflicting geometry.

## Template for future tests

- CWP ID and title:
- Date:
- Operating system:
- Fusion version and license category:
- OpenAI client and version:
- Connection method:
- Model, if known:
- Baseline fingerprint:
- Starting document:
- Natural-language request, if applicable:
- Structured specification, if applicable:
- Exact execution prompt:
- Expected result:
- Actual result:
- Independent measurements or export checks:
- Verification method:
- Evidence:
- Preflight blockers:
- Read-only diagnostics:
- Mutation attempts:
- Errors and recovery steps:
- Codex usage/status before and after, when available:
- Outcome: PASS / PARTIAL / FAIL / PRECONDITION FAIL / BLOCKED

Never include API keys, passwords, private account identifiers, or confidential designs. A screenshot alone is not evidence that all dimensions are correct; record independent measurements where relevant.

## Historical first modeling report

An earlier 4-to-6 mm modeling/export test is preserved in [first-modeling-test.md](first-modeling-test.md). It remains useful as the first observed automation and recovery record. The later CWP series above is the current bounded-test framework and should be treated separately rather than rewriting that historical result.
