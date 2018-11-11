from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:relief_center_id>/',
         views.create, name='wanted_item_create'),
    path('update/<int:relief_center_id>/<int:wanted_item_id>/',
         views.update, name='wanted_item_update'),
    path('delete/<int:relief_center_id>/<int:wanted_item_id>/',
         views.delete, name='wanted_item_delete')
]
