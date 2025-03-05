"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from tickets import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('guests',views.GuestViewSet)

router.register('movies',views.ModelViewSet)

router.register('reservations',views.ReservationViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),

    #1
    path('django/jsonresponsenomodel/',views.no_rest_no_model),
    #2
    path('django/jsonresponsefrommodel/',views.no_rest_with_model),

    #3
    path('rest/fbv/',views.fbv),

    #4
    path('rest/fbv/<int:pk>',views.fbv_detail),

    #5
    path('rest/cbv/',views.CBV_List.as_view()),

    #6
    path('rest/cbv/<int:pk>',views.CBV_pk.as_view()),

    #7
    path('rest/mixin/',views.Mixin_List.as_view()),

    #8
    path('rest/mixin/<int:pk>',views.Mixin_pk.as_view()),

    #9
    path('rest/generics/',views.Generic_List.as_view()),

    #10
    path('rest/generics/<int:pk>',views.Generic_pk.as_view()),

    #11
    path('rest/viewset/',include(router.urls)),
]
