from django.shortcuts import render,get_object_or_404,redirect

from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from .serializers import AdminSerializer,AdminUserFacingSerializer,TaskSerializer

from .models import AdminFacing,Task,Profile
from .forms import AdminForm
# Create your views here.

class HomeTemplateHTMLRender(TemplateHTMLRenderer):
    def get_template_context(self, data, renderer_context):
        data = super().get_template_context(data, renderer_context)
        if not data:
            return {}
        else:
            return data

class HomeViewSet(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=AdminUserFacingSerializer
    serializer_data=AdminUserFacingSerializer(queryset,many=True)
    template_name='home.html'

    #renderer_classes=[HomeTemplateHTMLRender]  

    def retrieve(self, request, *args, **kwargs):
        #return Response(self.template_name)
        print(request)
        return render(request,self.template_name, {'data': self.serializer_data.data})

class AdminViewSet(viewsets.ModelViewSet):
    queryset=AdminFacing.objects.all()
    serializer_class=AdminSerializer
    
    template_name='admin.html'

    def retrieve(self, request, *args, **kwargs):
        
        return render(request,self.template_name,{})

class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer