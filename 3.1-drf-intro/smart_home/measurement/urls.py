from django.urls import path
from django.contrib import admin
from measurement.views import SensorCreateView, SensorRetrieveView,  MeasurementView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/',  SensorCreateView.as_view()),
    path('sensors/<int:pk>/', SensorRetrieveView.as_view()),
    path('measurements/',  MeasurementView.as_view()),
]
