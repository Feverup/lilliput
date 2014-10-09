from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'links', views.ShortLinkViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^(?P<hash>\w+)$', views.GoToURLView.as_view(), name='go'),
]
