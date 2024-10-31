from django.urls import path
from .views import UserProfileApiView

urlpatterns = [
    path('list/', UserProfileApiView.as_view(), name='list_users'),  
    path('crear-usuarios/', UserProfileApiView.as_view(), name='crear_usuario'),
    path('actualizar-usuarios/<int:pkid>/', UserProfileApiView.as_view(), name='actualizar_usuario'),
    path('eliminar-usuarios/<int:pkid>/', UserProfileApiView.as_view(), name='eliminar_usuario'),
]
