from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('relief_center/', include('relief_center.urls')),
    path('wanted_item/', include('wanted_item.urls'))
]
