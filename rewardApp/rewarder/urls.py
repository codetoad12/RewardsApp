from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
router=DefaultRouter()
router_home=DefaultRouter()

router.register('home-view',views.HomeViewSet)

router.register('AdminView',views.AdminViewSet)
router.register('Task',views.TaskViewSet)

#print(router.urls)
urlpatterns=router.urls
#print(urlpatterns)