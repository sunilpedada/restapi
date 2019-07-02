from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .seralizing import emp
class crud(ModelViewSet):
        queryset =User.objects.all()
        serializer_class = emp
#class rpm(View):
    #def get(self,request):
        #return render(request,"registration.html")
    #def post(self,request):
        #one=request.POST["a"]
        #second = str(request.POST["b"])
        #third = request.POST["c"]
        #fourth = request.POST["d"]
        #fifth= request.POST["e"]
        #f = User(username=one,password=second,first_name=third,last_name=fourth,email=fifth)
        #f.save()
        #return HttpResponse(request,"ok")
#class dis(View):
    #def get(self,request):
        #r=User.objects.get(username="kohli")
        #return HttpResponse(request,r)