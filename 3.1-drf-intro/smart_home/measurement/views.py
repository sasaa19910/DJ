# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,CreateAPIView

from .serializers import SensorSeralizer, MeasurementSeralizer, SensorDetaliSeralizer
from .models import Sensor, Measurement







class SensorCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSeralizer


class SensorRetrieveView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetaliSeralizer


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSeralizer