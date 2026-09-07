# First modeling and STEP round-trip test
Date: 2026-09-06. Environment: Windows, Fusion 2705.1.11, native Codex MCP connection.

## Scope
A flat mounting plate is the first small bracket example. This is an automation demonstration, not a load-rated or production-qualified bracket. Only thickness is a named editable user parameter; the outline and hole sketch geometry are fixed.

## Results
| Check | Result |
|---|---|
| New separate document | Created; existing document left open |
| Initial geometry | One solid, 60 x 30 x 4 mm |
| Holes | Two through holes, diameter 6 mm; centers (10,15) and (50,15) mm |
| Parameter change | plate_thickness changed from 4 mm to 6 mm |
| Final geometry | One solid, 60 x 30 x 6 mm |
| Initial volume | 6973.805329 mm3 |
| Final volume | 10460.707993 mm3 |
| Feature health | Sketch and extrusion healthy |
| Export | STEP and editable F3D archive created locally |
| STEP reimport | Opened in a separate Fusion document |
| Reimport checks | Dimensions, two cylindrical holes, volume and healthy base feature passed |
| Visual check | Exported viewport PNG inspected; rectangular plate with two holes visible |

Volume was independently compared against (60*30 - 2*pi*3^2)*thickness. Bounding-box tolerance was 0.001 mm and volume tolerance 0.01 mm3. Measured hole centers matched the intended positions. STEP contains geometry, not the original named parameter/timeline.

## Recovery finding
The first creation attempt stopped before sketch creation because Fusion rejected changing the root component name. The new test document remained open. The recovery script checked its name and that it contained no bodies or sketches, omitted the unsupported rename, and completed the plate. It did not rerun blindly or create a duplicate model.

## Evidence boundaries
The F3D file was exported successfully but not reopened in this test. There was no cloud save. The original modeled document and STEP reimport remain open. Binary deliverables are currently local, not uploaded to this repository. Browser/tunnel access and independent repeatability on a second machine remain untested.

## Reproduction
The scripts in examples/mounting-plate record the executed creation attempt, guarded recovery, and geometry verifier. The creation attempt intentionally preserves the observed failure for transparency; do not run it as a polished installer. For a fresh working implementation, remove the unsupported root.name assignment before execution. Call scripts through fusion_mcp_execute with featureType script. The verifier uses readOnly true. To test the change, set the plate_thickness parameter expression to '6 mm', recompute, then run the verifier again. Export through Fusion's ExportManager and reimport STEP with ImportManager; the STEP geometry verifier substitutes t=6.0 for the absent user parameter.

Next: turn this observed sequence into a clean, independently repeated beginner walkthrough, then test a more representative L-bracket.
