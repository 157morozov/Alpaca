from . import views
from django.urls import path


urlpatterns = [
    path('test', views.TestAPIView.as_view(), name='test'),
    path('test/<int:pk>', views.TestAPIView.as_view(), name='test.pk'),
]
