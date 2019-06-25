from django.views.generic import View
from django.http import HttpResponse
import xml.etree.ElementTree as et
import json
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
"""json to xml part"""
class json_xml(View):
    def post(self,request):
        data1=request.body
        data = json.loads(data1)
        print(data)
        dc=[]
        for q in data:
            b=q["type"]
            if b["label"]=="Line":
                if len(q["coordinates"])==2:
                    dc.append({"label": b["label"], "value": b["value"], "coordinates": q["coordinates"]})
            elif b["label"] == "Rectangle":
                if len(q["coordinates"])==2:
                    dc.append({"label": b["label"], "value": b["value"], "coordinates": q["coordinates"]})
            elif b["label"] == "Polygon":
                if len(q["coordinates"]) > 2:
                    dc.append({"label": b["label"], "value": b["value"], "coordinates": q["coordinates"]})
        root = et.Element("annotations")
        version = et.SubElement(root, "version")
        version.text = str(1.1)
        for r in dc:
            print(r)
            labels = et.Element("labels")
            root.append(labels)
            label = et.SubElement(labels, "label")
            label.text = r["label"]
            type = et.SubElement(labels, "type")
            type.text = r["value"]
            coordinates = et.SubElement(labels, "coordinates")
            coordinates.text = str(r['coordinates'])
            tree = et.ElementTree(root)
            tree.write("test.xml")
        return HttpResponse(request,status=201)
