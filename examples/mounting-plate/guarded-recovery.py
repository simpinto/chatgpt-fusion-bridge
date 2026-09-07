import adsk.core, adsk.fusion, json

def run(_context: str):
    app = adsk.core.Application.get()
    doc = app.activeDocument
    assert doc.name == 'Fusion Bridge - Mounting Plate Test', 'Unexpected active document'
    doc.name = 'Fusion Bridge - Mounting Plate Test'
    design = adsk.fusion.Design.cast(app.activeProduct)
    design.designType = adsk.fusion.DesignTypes.ParametricDesignType
    root = design.rootComponent
    assert root.bRepBodies.count == 0 and root.sketches.count == 0, 'Test document not empty'
    design.userParameters.add('plate_thickness', adsk.core.ValueInput.createByString('4 mm'), 'mm', 'Editable thickness for bridge validation')
    sk = root.sketches.add(root.xYConstructionPlane)
    sk.name = '60 x 30 mm plate with two 6 mm holes'
    lines = sk.sketchCurves.sketchLines.addTwoPointRectangle(adsk.core.Point3D.create(0,0,0), adsk.core.Point3D.create(6,3,0))
    for line in lines:
        line.isFixed = True
    for x in [1.0,5.0]:
        circle = sk.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(x,1.5,0),0.3)
        circle.isFixed = True
    profile = max([sk.profiles.item(i) for i in range(sk.profiles.count)], key=lambda p: p.areaProperties().area)
    feat = root.features.extrudeFeatures.addSimple(profile, adsk.core.ValueInput.createByString('plate_thickness'), adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    feat.name = 'Plate thickness extrusion'
    feat.bodies.item(0).name = 'Mounting plate'
    sk.isVisible = False
    app.activeViewport.fit()
    print(json.dumps({'document': doc.name, 'bodies': root.bRepBodies.count, 'thickness_expression': design.userParameters.itemByName('plate_thickness').expression}))
