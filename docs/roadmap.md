# Roadmap

Unchecked items are planned, not completed. Completed items reflect observed tests in the testing journal, not universal compatibility.

## M0 — Establish the project

- [x] Draft purpose, initial research, and test plan.
- [ ] Select a reuse license before substantial external code contributions.
- [x] Record Windows environment, Fusion version, Codex CLI version, and native MCP connection observations.

## M1 — Prove the desktop connection

- [x] Confirm Fusion MCP is available on the test machine.
- [x] Configure the local OpenAI client and verify native tools after restart.
- [x] Discover tools and record initial read operations.
- [x] Read the active document and inspect its design state.

Success: a documented read operation succeeds through the actual native connection.

## M2 — Create editable CAD geometry

- [x] Create a disposable mounting plate with two holes.
- [x] Confirm a named editable thickness parameter exists.
- [x] Preserve visual and textual evidence.

Success: editable solid geometry exists in a separate Fusion document.

## M3 — Parametric modification

- [x] Change `plate_thickness` from 6 mm to 10 mm.
- [x] Let Fusion recompute.
- [x] Independently measure the resulting 10.00 mm body thickness.

Success: a parameter change propagates to independently verified BRep geometry.

## M4 — Manufacturing interchange

- [x] Export the current mounting plate as STEP.
- [x] Inspect the STEP structure and dimensional envelope.
- [x] Reimport the STEP into a new disposable Fusion document.
- [x] Confirm one valid solid BRep, nonzero volume, 60 × 30 × 10 mm envelope, two through-holes, and correct hole centers.

Success: a neutral STEP artifact survives a full Fusion export/import round trip without observed dimensional or topological loss.

## M5 — Natural-language-to-structured-CAD specification

- [x] Translate a plain-English mounting-plate request into an explicit structured specification.
- [x] Validate derived values before modeling.
- [x] Create the part from that specification.
- [x] Independently verify 80 × 40 × 8 mm geometry, two 6 mm through-holes, and centers at (15,20) and (65,20) mm.

Success: natural-language design intent is converted into an auditable intermediate specification and then into independently verified Fusion geometry.

## M6 — Configuration-driven regeneration and design intent

### CWP-007 — Structured-spec regeneration

- [x] Revise an existing structured specification.
- [x] Update the existing parametric Fusion model rather than rebuild it from scratch.
- [x] Recompute and independently verify all changed values.
- [x] Confirm unchanged design intent remains invariant.

Observed result: the same model/body was reused, four existing parameters were updated, no duplicate bodies or parameters were created, the model regenerated to 100 × 50 × 12 mm with two Ø8 mm through-holes at (20,25) and (80,25), and all relevant features remained healthy.

Success: configuration changes deterministically regenerated the intended existing model.

### CWP-008 — Schema-to-parameter binding and recovery sequence

The first direct-binding attempt failed with `VCS_SKETCH_OVER_CONSTRAINTS` when a redundant driving distance was added to an already-constrained sketch. A later preflight also detected residual parameters from the failed attempt and stopped before additional mutation. These failures were preserved as evidence and used to revise the procedure.

Recovery findings:

- [x] Distinguish preflight blockers and read-only diagnosis from true CAD mutation attempts.
- [x] Restore the original four core parameters after residual CWP-008 state.
- [x] Audit actual sketch coordinate frame and dimension references read-only.
- [x] Identify missing origin anchor and whole-sketch translational freedom.
- [x] Add one coincident constraint from the plate lower-left corner to the sketch origin.
- [x] Verify whole-sketch translation is eliminated without over-constraining the sketch.

### CWP-008B — Intent-based parameter binding

- [x] Add one semantic parameter: `hole_edge_offset`.
- [x] Rebind existing positional dimensions instead of adding duplicate driving constraints.
- [x] Bind hole 1 X to `hole_edge_offset`.
- [x] Bind hole 2 X to `plate_length - hole_edge_offset`.
- [x] Bind both hole Y positions to `plate_width / 2`.
- [x] Verify `hole_edge_offset` 20→25 mm moves holes symmetrically to (25,25) and (75,25).
- [x] Verify `plate_width` 50→60 mm moves both holes automatically to Y=30 mm.
- [x] Confirm no direct positional sketch edit is required for these changes.
- [x] Confirm origin anchor remains intact, body count remains 1, no over-constraint occurs, and features stay healthy.

Current validated final state after CWP-008B:

- `plate_length = 100 mm`
- `plate_width = 60 mm`
- `plate_thickness = 12 mm`
- `hole_diameter = 8 mm`
- `hole_edge_offset = 25 mm`
- hole centers = (25,30) and (75,30)
- one valid solid body
- origin anchor intact
- sketch still reported under-constrained, but whole-sketch translation is removed and tested design intent is deterministic

Success: the structured specification now has a deterministic semantic parameter interface to Fusion for the tested mounting-plate layout.

### CWP-009 — Input validation and safe rejection

- [ ] Reject zero/negative dimensions.
- [ ] Reject hole centers or derived feature positions outside the part.
- [ ] Reject impossible hole diameters and geometric conflicts.
- [ ] Prove invalid input does not modify the Fusion model.

Success: invalid designs fail safely before CAD mutation.

## M7 — Reusable feature library

### CWP-010 — Primitive features

- [ ] Define reusable structured primitives for plate, hole, slot, pocket, boss, chamfer, fillet, and pattern.

### CWP-011 — Feature sequencing

- [ ] Verify deterministic feature order and healthy recomputation.

### CWP-012 — Feature modification

- [ ] Modify existing features without unnecessary recreation.

Success: a small reusable CAD vocabulary can be composed and edited reliably.

## M8 — Components and assemblies

- [ ] CWP-013: create multiple named components.
- [ ] CWP-014: position components deterministically.
- [ ] CWP-015: test one simple assembly relationship/joint.

Success: the bridge moves from isolated solids to structured assemblies.

## M9 — Manufacturing-oriented furniture/CNC parts

- [ ] CWP-016: create a parametric closet panel primitive.
- [ ] CWP-017: create and verify a System 32 drilling pattern.
- [ ] CWP-018: encode one connector-machining primitive such as Rafix or Minifix.
- [ ] CWP-019: create and relate a shelf and side panel.

Success: the system can represent practical cabinet/closet manufacturing geometry.

## M10 — Manufacturing metadata

- [ ] CWP-020: material metadata.
- [ ] CWP-021: edge-banding metadata.
- [ ] CWP-022: deterministic part naming and numbering.

Success: CAD parts carry manufacturing-relevant information in addition to geometry.

## M11 — CAD-to-CAM bridge

- [ ] CWP-023: manufacturing-face detection.
- [ ] CWP-024: machining-feature classification.
- [ ] CWP-025: map features to CAM operation types.
- [ ] CWP-026: tool metadata/assignment.
- [ ] CWP-027: minimal verified CNC-ready toolpath test.

Success: selected structured CAD features can be translated into a controlled CAM workflow.

## M12 — Reliability and regression

- [ ] CWP-028: golden-part regression suite.
- [ ] CWP-029: controlled failure and recovery tests.
- [ ] CWP-030: idempotency test; repeated instruction must not duplicate geometry or parameters.
- [ ] Repeat the beginner workflow from a fresh session.
- [ ] Collect independent setup reports from additional machines.

Success: the system is reproducible, safe under failure, and resistant to duplicate execution.

## M13 — Natural-language design system

- [ ] CWP-031: broader freeform request parsing.
- [ ] CWP-032: ambiguity detection and required-field reporting.
- [ ] CWP-033: preserve design intent when only one requested property changes.

Success: natural language becomes a safe front end to the structured CAD schema rather than a source of uncontrolled guessing.

## M14 — Product-level generation

- [ ] CWP-034: closet module.
- [ ] CWP-035: configurable cabinet.
- [ ] CWP-036: room-level multi-module generation.

Success: verified primitives and rules compose into higher-level products.

## Later — Browser access

- [ ] Confirm account permissions and secure-tunnel availability.
- [ ] Test the validated workflow through ChatGPT web.
- [ ] Resolve screenshot delivery, export access, disconnects, and document selection.
- [ ] Compare browser and local-desktop reliability and maintenance effort.

Public plugin distribution and multi-user hosting remain separate design decisions after the local workflow and safety model mature.
