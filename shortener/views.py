from django.views.generic import RedirectView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from .models import ShortLink
from .serializers import ShortLinkSerializer


class ShortLinkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ShortLink to be viewed or edited.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer

    def create(self, request, *args, **kwargs):
        try:
            self.object = ShortLink.objects.get(original_url=request.data['original_url'])
        except ShortLink.DoesNotExist:
            self.object = None

        if self.object:
            serializer = self.get_serializer(self.object)
            status_code = status.HTTP_200_OK
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            status_code = status.HTTP_201_CREATED

        if not self.object:
            self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status_code, headers=headers)


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
