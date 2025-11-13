from django.urls import path

from .views import MenuView

urlpatterns = [
    path('tree/', MenuView.as_view(), name='menu_root'),
    path('tree/<path:menu_path>/', MenuView.as_view(), name='menu_item'),
]
