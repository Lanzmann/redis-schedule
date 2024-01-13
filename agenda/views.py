from rest_framework import viewsets
from .models import AgendaItem
from .serializers import AgendaItemSerializer


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = AgendaItem.objects.all()
    serializer_class = AgendaItemSerializer