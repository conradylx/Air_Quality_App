from django.urls import path

from core import views
from core.views import ChartView

urlpatterns = [
    path('', views.index, name='home'),
    path('charts/', ChartView.as_view(), name="charts"),
]