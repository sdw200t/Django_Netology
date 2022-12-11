from django.urls import path

from measurement.views import MeasurementsView, SensorView, SensorViewUpdate

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorViewUpdate.as_view()),
    path('measurements/', MeasurementsView.as_view()),
]
