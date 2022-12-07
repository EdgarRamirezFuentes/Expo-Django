from PingManagement import views
from rest_framework import routers
from django.urls import path, include
from PingManagement.consumers import GraphConsumer

app_name = 'PingManagement'

router = routers.SimpleRouter()
router.register('', views.PingViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('make-ping/<destination>/<int:count>/', views.PinggerView.as_view())
]

ws_urlpatterns = [
    path('ws/graph/',GraphConsumer)
]