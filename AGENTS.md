# Agent operating rules — ChatGPT–Fusion Bridge

These instructions are intended for AI coding/automation agents working in this repository.

## Primary goal

Develop and document a reliable, beginner-friendly workflow for controlling Autodesk Fusion through documented OpenAI tooling and Autodesk Fusion MCP capabilities.

Prefer the existing Autodesk Fusion MCP interface. Do not create a custom Fusion add-in or parallel integration layer unless a tested limitation demonstrates that one is necessary.

## Quota-aware execution

Minimize unnecessary autonomous work.

Before acting:

1. Read only the files relevant to the assigned task.
2. Read the latest relevant checkpoint or testing-journal entry.
3. Do not scan the whole repository unless the task genuinely requires it.
4. Do not perform web research unless explicitly requested or required to resolve a documented blocker.

## Codex Work Package discipline

For CWP tasks:

- execute only the requested CWP;
- preserve the stated starting document and unrelated files;
- verify the expected baseline fingerprint before mutation;
- use explicit PASS/FAIL criteria;
- independently verify outputs where possible;
- stop when the requested objective is complete;
- do not continue into the next CWP.

See `docs/cwp-framework.md`.

## Baseline and preflight policy

Before a mutation task, confirm enough state to identify the intended known-good model. Depending on the CWP, this may include:

- document name;
- body count;
- parameter names/count and critical values;
- critical dimensions and feature locations;
- origin/coordinate-frame anchor state;
- sketch/timeline feature health.

If the starting state materially differs, stop with `PRECONDITION FAIL`. Do not silently recover inside an unrelated task.

Preflight blockers such as modal dialogs, a wrong active document, Fusion busy state, or temporary tool unavailability do not count as CAD mutation attempts.

## Read-only diagnosis

Read-only inspection does not consume the mutation retry budget. Prefer diagnosis before speculative editing when the failure involves:

- sketch over-constraint;
- uncertain dimension references;
- unknown coordinate-frame anchoring;
- parameter conflicts;
- feature-health uncertainty.

Useful diagnostics include parameter lists, sketch-dimension audits, constraint-topology audits, global bounding boxes, edge-relative measurements, and BRep interrogation.

## Mutation failure policy

Use a maximum of two **targeted CAD mutation attempts** unless a task explicitly authorizes more:

1. Make one planned mutation.
2. Recompute and verify sketch/feature health immediately.
3. If it fails, revert that mutation when practical.
4. Try one reasonable targeted alternative.
5. If the second true mutation attempt fails, stop and document the failure.

Do not stack multiple speculative changes before checking health. Do not convert a bounded task into open-ended experimentation.

## Constraint-safe CAD rules

- Audit existing driving dimensions and geometric constraints before adding new ones.
- Prefer rebinding existing dimensions to parameter expressions over adding parallel driving constraints.
- Distinguish global coordinates from edge-relative or feature-relative dimensions.
- Intentionally anchor the coordinate frame when absolute placement matters.
- Do not fully rebuild a sketch merely to bypass an over-constraint problem.
- If a constrained refactor is genuinely required, preserve/recover the last known-good state and document the reason.

## Design-intent parameterization

Prefer semantic design variables and derived relationships over independent raw coordinates.

Example validated pattern:

```text
hole_edge_offset = 25 mm
Hole 1 X = hole_edge_offset
Hole 2 X = plate_length - hole_edge_offset
Hole Y   = plate_width / 2
```

This better preserves symmetry and centerline intent than independent X/Y values.

## Fusion safety

- Prefer disposable documents for tests.
- Do not modify confidential or unrelated user designs.
- Do not overwrite existing Fusion documents or exports unless explicitly instructed.
- Verify geometry through read/measure/BRep inspection rather than trusting only the values used to create it.
- Screenshots are corroborating evidence, not sufficient dimensional verification by themselves.
- Record unexpected Fusion behavior and recovery steps.

## Structured CAD direction

For design-generation tasks, prefer this flow:

**natural language → structured specification → validation → semantic parameter binding → Fusion mutation → independent verification**

Do not silently invent unspecified manufacturing features, dimensions, materials, tolerances, fillets, chamfers, hardware, or CAM operations.

When a specification is ambiguous or invalid, prefer safe rejection or an explicit missing-field report over guessing.

## Repository discipline

- Preserve historical test reports even when later tests improve the workflow.
- Preserve failed attempts and recovery findings when they materially improve the procedure.
- Distinguish documented capability, planned capability, and verified result.
- Keep test evidence concise and reproducible.
- Never commit passwords, API keys, account identifiers, credentials, private designs, or confidential customer information.
- Do not add generated binary artifacts unless they are intentionally selected as public test evidence.

## Documentation expectations

For meaningful tests, record:

- objective;
- environment;
- baseline fingerprint;
- prompt/specification;
- expected result;
- actual result;
- independent verification;
- preflight blockers;
- read-only diagnostics;
- mutation attempts;
- errors/recovery;
- PASS / PARTIAL / FAIL / PRECONDITION FAIL / BLOCKED;
- next bounded milestone.

Use the testing journal as the public record of observed results.
