from django.urls import path,include
from enroll.api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('curd',views.UserViewset,basename='user')

urlpatterns=[
    path('',include(router.urls))
]