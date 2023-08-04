from rest_framework import viewsets
from testapp.api.serializers import HydJobSerializer
from testapp.models import HydJobs
class HydJobsCRUDCBV(viewsets.ModelViewSet):
    queryset = HydJobs.objects.all()
    serializer_class = HydJobSerializer