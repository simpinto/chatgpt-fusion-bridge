# ChatGPT–Fusion Bridge

A community effort to make Autodesk Fusion accessible through OpenAI tools, with practical workflows and setup instructions for non-programmers.

## Current status

**Research and planning. No working integration has been verified by this project yet.** This repository currently contains documentation, not an installable plug-in.

## Why this project exists

People should be able to describe a design task, work with an AI assistant, and refine an editable Fusion model without needing to become programmers. Autodesk provides an MCP interface used by Claude. We are investigating how OpenAI clients can use that published interface and what guidance or additional software is needed.

This is an independent community project, not affiliated with or endorsed by OpenAI, Autodesk, or Anthropic. Autodesk Fusion (formerly Fusion 360) is the target; AutoCAD is a separate product.

## Approach

1. Test a local OpenAI/Codex desktop connection to Fusion's existing MCP server.
2. Document a repeatable beginner-friendly setup.
3. Validate a simple parametric modeling and export workflow.
4. Add reusable instructions or software only where testing demonstrates a need.
5. Explore ChatGPT browser access through a secure tunnel as a later milestone.

We aim to use documented interfaces, not reproduce Claude's implementation.

## Read the documentation

- [Research and connection options](docs/research.md)
- [Roadmap](docs/roadmap.md)
- [Testing journal](docs/testing-journal.md)
- [Contributing](CONTRIBUTING.md)

## First demonstration we want to achieve

Create a mounting bracket in a disposable Fusion document, change a named dimension, verify the resulting geometry, and export a STEP file. Record the exact environment, prompts, results, and failures so another person can repeat it.

## Participation and licensing

Non-programmers can help by describing workflows, testing instructions, and reporting confusing steps. Developers can help assess compatibility and propose focused improvements.

A reuse license has not yet been selected. Public visibility should not be interpreted as an open-source license grant. License selection is an early roadmap item, before accepting substantial external code contributions.
