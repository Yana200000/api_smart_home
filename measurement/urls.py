from django.urls import path

from .views import SensorsListCreateView, SensorView, MeasurementCreateView, SensorChangeView

urlpatterns = [
    path('sensors/', SensorsListCreateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('sensors/update/<pk>/', SensorChangeView.as_view()),
    path('sensors/<pk>/', SensorView.as_view())
]