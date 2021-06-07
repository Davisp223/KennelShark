from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from index import views as index_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls'), name='index'),
    path('ui/', include('ui.urls'), name='ui'),
    path('login/', auth_views.LoginView.as_view(template_name='index/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index/logout.html'), name='logout'),
]
