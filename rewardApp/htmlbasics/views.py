from django.shortcuts import render,redirect
from .models import AdminModel
# Create your views here.

def index(request):

    app_name=request.POST.get('app_name')
    app_link=request.POST.get('app_link')
    app_category=request.POST.get('app_cat')
    app_sub_category=request.POST.get('app_subcat')

    model=AdminModel()
    model.app_name=app_name
    model.link=app_link
    model.category=app_category
    model.sub_category=app_sub_category

    model.save()
    
    print(app_name)
    return render (request,'admin.html',{})
"""""
def admin_view(request):
    model=AdminModel()
    template='admin.html'

    if(request.method=="POST"):
        print(request.POST)
        return redirect('index')
"""""