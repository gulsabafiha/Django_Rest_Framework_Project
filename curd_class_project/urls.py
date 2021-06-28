from django.contrib import admin
from django.urls import path,include
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.UserAddShow.as_view(),name='addshow'),   
    path('delete/<int:id>/',views.UserDelete.as_view(),name='delete'),
    path('update/<int:id>/',views.UpdateView.as_view(),name='update'),
    path('api/',include('enroll.api.urls')),
]
