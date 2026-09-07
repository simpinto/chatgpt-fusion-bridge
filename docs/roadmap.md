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

## M6 — Configuration-driven regeneration

### CWP-007 — Structured-spec regeneration

- [ ] Revise an existing structured specification.
- [ ] Update the existing parametric Fusion model rather than rebuild it from scratch.
- [ ] Recompute and independently verify all changed values.
- [ ] Confirm unchanged design intent remains invariant.

Success: configuration changes deterministically regenerate the intended existing model.

### CWP-008 — Schema-to-parameter binding

- [ ] Define explicit mapping between schema fields and Fusion user parameters.
- [ ] Ensure intended schema variables are not hidden as hard-coded geometry.
- [ ] Verify each schema change affects only the intended feature or dimension.

Success: the structured specification has a deterministic parameter interface to Fusion.

### CWP-009 — Input validation and safe rejection

- [ ] Reject zero/negative dimensions.
- [ ] Reject hole centers outside the part.
- [ ] Reject impossible or conflicting feature requests.
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
