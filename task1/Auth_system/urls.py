from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
        path('login/',views.login,name='login'),
        path('regisration/',views.registration,name='registration'),
        path('dash/',views.dash,name='dash'),
        path('logout/',views.logut,name='logout'),
        path('additem/',views.additem,name='additem'),
        path('deleteitem/<int:itemid>/',views.deleteitem,name='deleteitem'),
        path('updateitem/<int:itemid>/',views.updateitem,name='updateitem'),
        path('',views.home,name='home'),
        path('viewmore/(<int:itemid>)(<str:category>)/',views.viewmore,name='viewmore'),
        path('viewmoreseller/<int:itemid>/',views.viewmoreseller,name='viewmoreseller'),
        path('adminlogin/',views.adminlogin,name='adminlogin'),
        path('admindash/',views.admindash,name='admindash'),
       # path('addcategory/',views.addcategory,name='addcategory'),

]