# ChatGPT–Fusion Bridge

A community effort to make Autodesk Fusion accessible through OpenAI tools, with practical workflows and setup instructions for non-programmers.

## Current status

**Core desktop proof-of-concept and first design-intent milestones have passed.** On one Windows test machine, the project has demonstrated:

- native Codex access to Autodesk Fusion's local MCP server;
- creation of a parametric mounting plate in a disposable Fusion document;
- parameter-driven regeneration with independent geometry verification;
- STEP export and round-trip reimport as a valid solid BRep;
- natural-language design intent translated into a structured CAD specification and then executed and independently verified in Fusion;
- structured-spec regeneration of an existing model without rebuilding it;
- constraint-safe, intent-based parameter binding using semantic relationships rather than independent raw coordinates.

The current CWP sequence has passed through **CWP-008B — Intent-Based Parameter Binding**. See the [testing journal](docs/testing-journal.md) and [CWP framework](docs/cwp-framework.md).

This remains an early demonstration on one machine, not an installable plugin or production-qualified CAD/CAM system. Independent repeatability on additional machines, browser access, broader feature coverage, manufacturing rules, validation logic, and CAM automation remain to be tested.

## Why this project exists

People should be able to describe a design task, work with an AI assistant, and refine an editable Fusion model without needing to become programmers. Autodesk provides a local MCP interface for Fusion. This project is testing how OpenAI clients can use that published interface reliably and what guidance or additional software is actually needed.

This is an independent community project, not affiliated with or endorsed by OpenAI, Autodesk, or Anthropic. Autodesk Fusion (formerly Fusion 360) is the target; AutoCAD is a separate product.

## Approach

1. Use Autodesk Fusion's existing MCP server before building custom integration software.
2. Keep Codex tasks bounded and measurable through Codex Work Packages (CWPs).
3. Separate planning/research from local execution to reduce wasted agent usage.
4. Verify generated or modified geometry independently instead of trusting only input parameters.
5. Preserve tested results, failed attempts, and recovery findings in a public journal.
6. Treat preflight, read-only diagnosis, and CAD mutation as separate phases.
7. Prefer semantic design variables and derived relationships over independent raw coordinates.
8. Add reusable abstractions only after repeated tests demonstrate a real need.
9. Explore ChatGPT browser access through a secure tunnel only after the local desktop path is stable.

## Validated capability chain

The project has now demonstrated this sequence:

**CONNECT → CREATE → MODIFY → EXPORT STEP → ROUND-TRIP VERIFY → NATURAL LANGUAGE → STRUCTURED CAD SPECIFICATION → REGENERATE EXISTING MODEL → INTENT-BASED PARAMETER BINDING → VERIFIED MODEL**

## Read the documentation

- [Research and connection options](docs/research.md)
- [Roadmap](docs/roadmap.md)
- [Testing journal](docs/testing-journal.md)
- [Codex Work Package framework](docs/cwp-framework.md)
- [First modeling test](docs/first-modeling-test.md)
- [Contributing](CONTRIBUTING.md)

## Next milestone

**CWP-009 — Input validation and safe rejection** will test whether invalid structured specifications are rejected before Fusion is mutated. Planned cases include negative dimensions, impossible hole sizes, out-of-bounds feature locations, and conflicting geometry.

## Participation and licensing

Non-programmers can help by describing workflows, testing instructions, and reporting confusing steps. Developers can help assess compatibility and propose focused improvements.

A reuse license has not yet been selected. Public visibility should not be interpreted as an open-source license grant. License selection remains an early roadmap item before accepting substantial external code contributions.
