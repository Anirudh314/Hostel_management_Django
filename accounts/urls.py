from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^$', views.home),
    url(r'^building/$', views.building, name="buildings" ),
    url(r'^floormapLG/$', views.floormapLG, name="floormapLG" ),
    url(r'^floormapL1/$', views.floormapL1, name="floormapL1" ),
    url(r'^floormapL2/$', views.floormapL2, name="floormapL2" ),
    url(r'^floormapMG/$', views.floormapMG, name="floormapMG" ),
    url(r'^floormapM1/$', views.floormapM1, name="floormapM1" ), 
    url(r'^roomform/$', views.book_room, name='book_room'),  
    url(r'^register/$', views.register1 , name = "register1"),
    url(r'^register_wr/$', views.register2 , name = "register2"),
    url(r'^register_corr/$', views.register3 , name = "register3"),
    url(r'^home_page/$',views.home_page,name="home_page"),
    url(r'^profile/$',views.profile,name="profile"),
    url(r'^home_page_booked/$',views.home_page_booked,name="home_page_booked"),
    url(r'^login/$',login,{'template_name':'accounts/login.html'}),
    url(r'^logout/$',logout,{'template_name':'accounts/home.html'}),

]
