from rest_framework import generics

from framework.models import FrameworkModel
from serializers import FrameworkSerializer


class FrameworkListView(generics.ListAPIView):
    queryset = FrameworkModel.objects.all()
    serializer_class = FrameworkSerializer


class FrameworkListLanguageView(generics.ListAPIView):
    queryset = FrameworkModel.objects.all()
    serializer_class = FrameworkSerializer

    def get_queryset(self):
        return self.queryset.filter(language=self.kwargs.get('language'))
