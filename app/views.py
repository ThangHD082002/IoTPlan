from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Sensor
from .serializers import SensorSerializer  # Tạo serializers.py để định nghĩa Serializer

@api_view(['GET'])
def sensor_data_list(request):
    # Lấy ra 100 phần tử đầu tiên từ cơ sở dữ liệu
    sensor_data = Sensor.objects.all().order_by('-time')[:100]

    # Sử dụng Serializer để chuyển đổi đối tượng thành dữ liệu JSON
    serializer = SensorSerializer(sensor_data, many=True)

    # Trả về dữ liệu JSON
    return Response(serializer.data, status=status.HTTP_200_OK)
