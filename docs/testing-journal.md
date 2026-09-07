# Testing journal

## 2026-09-06 — Research baseline

Documentation was reviewed and two possible connection approaches were identified. No connection to a live Fusion session was tested. No geometry was generated, measured, or exported by this project.

## 2026-09-06 — First local read-only probe passed

- Environment: Windows; Codex CLI 0.153.1 available. Fusion was already running with MCP enabled. Fusion version and license category were not established.
- Connection: local HTTP at `http://127.0.0.1:27182/mcp`.
- Method: JSON-RPC requests from PowerShell, not yet native Codex tool dispatch.
- Initialization: succeeded using MCP protocol 2024-11-05; server identified itself as MCP Server Adapter 1.0.0.
- Tool discovery: succeeded. Advertised tools included fusion_mcp_read, fusion_mcp_execute, fusion_mcp_update, and fusion_mcp_electronics_read.
- Read test: `fusion_mcp_read` with `{"queryType":"document","operation":"open"}` succeeded and reported one active, unmodified, unsaved document.
- An initial HTTP GET returned 405; JSON-RPC POST requests succeeded. A rejected GET alone does not establish that the server is unavailable.
- No design changes, screenshot capture, saves, or exports were performed.
- Added a persistent `mcp_servers.fusion` entry using the local endpoint and a 120-second tool timeout. Restart/native tool discovery remains to be verified.
- Outcome: transport, discovery, and one read operation passed. Full client integration remains partial.
- Next: restart the desktop client, verify Fusion tools are loaded, then inspect a disposable design before modeling.

## 2026-09-06 — Native desktop connection passed after restart

- The user restarted Codex while Fusion remained open.
- Fusion tools were present in the native tool catalog and invoked directly; no PowerShell HTTP fallback was used for these tests.
- Open-document query: succeeded; one active, unmodified, unsaved document.
- Active-command query: default Select command; no interactive command dialog reported.
- API documentation query: succeeded.
- Read-only script: succeeded and reported Fusion version 2705.1.11, a Fusion design, zero root bodies, zero root sketches, and zero component occurrences.
- No geometry changes, screenshots, saves, or exports were performed.
- Outcome: native discovery, read calls, documentation access, and read-only script execution passed. This demonstrates a working local OpenAI-client connection on this machine, not universal compatibility or completed CAD automation.
- Next milestone: create and validate a simple parametric test part and export.

## Template for future tests

- Date:
- Operating system:
- Fusion version and license category:
- OpenAI client and version:
- Connection method:
- Model, if known:
- Starting document (use a disposable sample):
- Exact prompt:
- Expected result:
- Actual result:
- Measurements or export checks:
- Evidence (redacted screenshots or public sample files):
- Errors and recovery steps:
- Outcome: passed / partial / failed / not tested

Never include API keys, passwords, private account identifiers, or confidential designs. A screenshot alone is not evidence that all dimensions are correct; record independent measurements where relevant.

## 2026-09-06 — Modeling milestone

Created a flat mounting plate, verified a 4-to-6 mm thickness change, exported STEP/F3D and a viewport image, and reimported STEP with matching measured geometry. See [full report and recovery finding](first-modeling-test.md). F3D reopening and cloud save were not tested.
