from django.urls import path, include
from vsearch_test.views import *

app_name = 'vsearch'
urlpatterns = [
	path('', SearchV.as_view(), name='entry'),
	path('<int:pk>/', Search_resultV.as_view(), name='result'),
	path('viewlog/', View_log.as_view(), name='viewlog'),
]