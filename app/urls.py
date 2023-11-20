from django.urls import path
from .views import sensor_data_list

urlpatterns = [
    path('api/sensor-data/', sensor_data_list, name='sensor_data_list'),
    # Các đường dẫn khác của ứng dụng của bạn...
]