from django.views.generic import RedirectView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ShortLink
from .serializers import ShortLinkSerializer


class ShortLinkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ShortLink to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer


class GoToURLView(RedirectView):
    """
    Redirects shortened URL to real URL
    """

    def get_redirect_url(self, **kwargs):
        try:
            obj = ShortLink.objects.get(hash=kwargs['hash'])
            return obj.original_url
        except ShortLink.DoesNotExist:
            return None
