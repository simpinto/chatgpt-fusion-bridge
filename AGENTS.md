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
- use explicit PASS/FAIL criteria;
- independently verify outputs where possible;
- stop when the requested objective is complete;
- do not continue into the next CWP.

See `docs/cwp-framework.md`.

## Failure policy

Use a maximum two-attempt recovery policy unless a task explicitly authorizes more:

1. Try the obvious safe correction.
2. Try one reasonable alternative.
3. If the second attempt fails, stop and document the failure.

Do not convert a bounded execution task into open-ended experimentation.

## Fusion safety

- Prefer disposable documents for tests.
- Do not modify confidential or unrelated user designs.
- Do not overwrite existing Fusion documents or exports unless explicitly instructed.
- Verify geometry through read/measure/BRep inspection rather than trusting only the values used to create it.
- Screenshots are corroborating evidence, not sufficient dimensional verification by themselves.
- Record unexpected Fusion behavior and recovery steps.

## Structured CAD direction

For design-generation tasks, prefer this flow:

**natural language → structured specification → validation → Fusion mutation → independent verification**

Do not silently invent unspecified manufacturing features, dimensions, materials, tolerances, fillets, chamfers, hardware, or CAM operations.

When a specification is ambiguous or invalid, prefer safe rejection or an explicit missing-field report over guessing.

## Repository discipline

- Preserve historical test reports even when later tests improve the workflow.
- Distinguish documented capability, planned capability, and verified result.
- Keep test evidence concise and reproducible.
- Never commit passwords, API keys, account identifiers, credentials, private designs, or confidential customer information.
- Do not add generated binary artifacts unless they are intentionally selected as public test evidence.

## Documentation expectations

For meaningful tests, record:

- objective;
- environment;
- prompt/specification;
- expected result;
- actual result;
- independent verification;
- errors/recovery;
- PASS / PARTIAL / FAIL;
- next bounded milestone.

Use the testing journal as the public record of observed results.
