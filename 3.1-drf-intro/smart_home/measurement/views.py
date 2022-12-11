from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorViewUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementsView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        sensor = get_object_or_404(Sensor, id=self.request.data.get('sensor'))
        return serializer.save(sensor=sensor) 


