import adsk.core, adsk.fusion, json, math

def run(_context: str):
    d = adsk.fusion.Design.cast(adsk.core.Application.get().activeProduct)
    bodies = d.rootComponent.bRepBodies
    assert bodies.count == 1
    b = bodies.item(0)
    box = b.boundingBox
    dims = [(box.maxPoint.x-box.minPoint.x)*10,(box.maxPoint.y-box.minPoint.y)*10,(box.maxPoint.z-box.minPoint.z)*10]
    holes = []
    for f in b.faces:
        c = adsk.core.Cylinder.cast(f.geometry)
        if c: holes.append({'diameter_mm':c.radius*20, 'center_mm':[c.origin.x*10,c.origin.y*10]})
    t=d.userParameters.itemByName('plate_thickness').value*10
    expected=(60*30-2*math.pi*3**2)*t
    volume=b.volume*1000
    assert all(abs(a-e)<0.001 for a,e in zip(dims,[60,30,t]))
    assert len(holes)==2 and all(abs(h['diameter_mm']-6)<0.001 for h in holes)
    assert abs(volume-expected)<0.01
    health=[{'name':d.timeline.item(i).name,'health':int(d.timeline.item(i).healthState)} for i in range(d.timeline.count)]
    print(json.dumps({'dimensions_mm':dims,'holes':holes,'volume_mm3':volume,'expected_volume_mm3':expected,'timeline':health,'passed':True}))
