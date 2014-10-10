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
            self.object = ShortLink.objects.get(original_url=request.DATA['original_url'])
        except ShortLink.DoesNotExist:
            self.object = None

        serializer = self.get_serializer(self.object, data=request.DATA,
                                         files=request.FILES)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            self.pre_save(serializer.object)
        except ValidationError as err:
            # full_clean on model instance may be called in pre_save,
            # so we have to handle eventual errors.
            return Response(err.message_dict, status=status.HTTP_400_BAD_REQUEST)

        if self.object is None:
            self.object = serializer.save(force_insert=True)
            self.post_save(self.object, created=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        self.object = serializer.save(force_update=True)
        self.post_save(self.object, created=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
