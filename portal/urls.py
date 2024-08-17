from django.urls import path

from . import views

urlpatterns = [
    #path('login/', views.login_view, name='login'),
    path('portal/', views.Portal_view.as_view(), name='portal'),

    path('login/',views.login_user,name='login'),
    path('submit/',views.submit_login, name='submit_login'),
    path('logout/',views.logout_user, name='logout'),
]