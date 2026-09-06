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
