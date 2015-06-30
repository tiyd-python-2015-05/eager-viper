from activity.models import ActivitySerializer, StatSerializer, Activity, Stat, \
    StatUpdateSerializer
from django.db import IntegrityError
from rest_framework import viewsets, generics
from rest_framework.exceptions import NotAcceptable


class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        return self.request.user.activities.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StatsView(generics.ListCreateAPIView):
    serializer_class = StatSerializer

    def get_queryset(self):
        return self.activity.stats.all()

    def perform_create(self, serializer):
        try:
            serializer.save(activity=self.activity)
        except IntegrityError:
            raise NotAcceptable("Data for this day already exists.")

    def dispatch(self, request, *args, **kwargs):
        activity_pk = kwargs['activity_pk']
        self.activity = Activity.objects.get(pk=activity_pk)
        return super().dispatch(request, *args, **kwargs)


class StatView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StatUpdateSerializer

    def get_queryset(self):
        return Stat.objects.filter(activity__owner=self.request.user)
