import json
import xml.etree.ElementTree as et
#import urllib
#import dicttoxml
#page = urllib.urlopen('http://quandyfactory.com/api/example')
#content = page.read()
#obj = json.loads(content)
with open("test2.json",'r') as elements:
    data=json.load(elements)
    dc=[]
    i=0
    for q in data["labels"]:
        #print(q)
        if q["type"] == "Rectangle":
            if len(q["coordinates"]) == 2:
                dc.append(tuple(q["coordinates"]))
        elif q["type"] == "Polygon":
            if len(q["coordinates"]) > 4:
                dc.append(tuple(q["coordinates"]))
        #elif q["type"] == "Line":
            #if len(q["coordinates"]) ==2:
                #dc.append(tuple(q["coordinates"]))
    #print(dc)
    root = et.Element("annotations")
    version = et.SubElement(root, "version")
    version.text = str(1.1)
    for p in data["labels"]:
        labels = et.Element("labels")
        root.append(labels)
        label = et.SubElement(labels, "label")
        label.text = p["label"]
        type = et.SubElement(labels, "type")
        type.text = p["type"]
        coordinates = et.SubElement(labels, "coordinates")
        coordinates.text = str(dc[i])
        tree = et.ElementTree(root)
        tree.write("test.xml")
        i=i+1