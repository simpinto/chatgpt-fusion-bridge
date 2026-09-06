# Research and connection options

Research date: 2026-09-06. Product interfaces and eligibility may change. The following distinguishes vendor documentation from our untested engineering assessment.

## Documented foundation

Autodesk documents two different MCP servers: a local server for a running Fusion session, and a cloud Data MCP server for projects, folders, and related data. The local server is the relevant starting point for editing an active CAD model.

Source: [Autodesk Fusion MCP overview](https://help.autodesk.com/view/fusion360/ENU/?guid=FMCP-OVERVIEW).

Autodesk's Claude workflow guide describes inspecting models, capturing views, changing parameters, executing Fusion API scripts, creating simple parametric geometry, and exporting files. It identifies repetitive workflows as stronger current use cases than complex model generation. These are vendor-described capabilities, not results verified by this project.

Source: [Autodesk workflow guide](https://www.autodesk.com/products/fusion-360/blog/how-to-improve-your-fusion-workflow-with-the-claude-desktop-connector/).

## Option A: local desktop connection

Path: OpenAI desktop client -> local Fusion MCP -> active Fusion document.

Autodesk documents enabling Fusion MCP under Preferences > General > API, with a default local endpoint of `http://127.0.0.1:27182/mcp`. OpenAI documents local MCP clients and Streamable HTTP support. Together these suggest a direct connection is feasible; an end-to-end test is still required.

Sources: [Autodesk connection instructions](https://help.autodesk.com/view/ADSKMCP/ENU/?guid=ADSKMCP_FusionDesktopMcp_connecting_to_the_fusion_mcp_server_html), [OpenAI MCP documentation](https://learn.chatgpt.com/docs/extend/mcp?surface=cli).

Assessment: best first prototype because it has fewer moving parts and lets the user inspect changes alongside Fusion. Configuration may suffice; no custom add-in should be assumed necessary. Local transport does not mean offline AI inference or that model context stays on the workstation.

## Option B: ChatGPT browser connection

Path: ChatGPT web -> Secure MCP Tunnel -> local Fusion MCP -> active document.

OpenAI documents private-server access through an outbound tunnel client. It requires a tunnel identity, runtime API key, appropriate permissions, and developer-mode access. The Fusion workstation and tunnel must remain available. Browser access does not automatically provide an interactive CAD viewport or downloadable local exports.

Sources: [Secure MCP Tunnel](https://developers.openai.com/api/docs/guides/secure-mcp-tunnels), [Connect and test a plugin](https://developers.openai.com/plugins/deploy/connect-chatgpt).

Assessment: useful when browser access matters, but adds operational complexity. A private tunnel prototype and a publicly distributed plugin are different scopes; OpenAI documents public endpoint requirements for distribution.

## Unresolved questions

- Does the participant's Fusion version and license expose MCP?
- Does the installed OpenAI client successfully discover and invoke the tools?
- Which exact tool schemas and operations are available?
- How are screenshots, exports, errors, and long operations handled?
- How do we confirm the correct active document and avoid duplicated changes after retries?
- What account eligibility, usage limits, and costs apply? No pricing promises are made.
- How repeatable is the same task across different machines and client versions?

## Decision

Start with the desktop proof of concept. Reconsider browser access after one complete modeling workflow is repeatable. Connection method alone does not guarantee better geometry or equivalent results to Claude.
