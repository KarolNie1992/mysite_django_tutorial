"""
Url for viewOnSnow app
"""

from django.urls import path
from django.conf.urls.i18n import i18n_patterns

from . import views


app_name = 'viewonsnow'


urlpatterns = [
    # ex: /
    path('', views.viewonsnow_index, name='viewonsnow_index'),
    #example: viewonsnow/api/data/11
    path('api/data/<int:calc_id>', views.get_data, name='api-data'),
    path('api/chart/data/', views.ChartData.as_view()),
]
