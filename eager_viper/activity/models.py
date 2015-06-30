from datetime import date

from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers
from rest_framework.reverse import reverse


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Activity(BaseModel):
    owner = models.ForeignKey(User, related_name="activities")
    title = models.CharField(max_length=255)

    class Meta:
        unique_together = ('owner', 'title',)

    def __str__(self):
        return self.title


class Stat(BaseModel):
    activity = models.ForeignKey(Activity, related_name='stats')
    date = models.DateField(default=date.today)
    count = models.PositiveIntegerField()

    class Meta:
        unique_together = ('activity', 'date',)


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault())
    _links = serializers.SerializerMethodField()

    def get__links(self, obj):
        return {"stats": reverse("stats",
                                 kwargs={"activity_pk": obj.pk},
                                 request=self.context.get('request')),
                }

    class Meta:
        model = Activity
        fields = ('id', 'url', 'owner', 'title', '_links')


class StatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stat
        fields = ('id', 'url', 'date', 'count')


class StatUpdateSerializer(serializers.HyperlinkedModelSerializer):
    activity = serializers.HyperlinkedRelatedField(read_only=True,
                                                   view_name='activity-detail')
    date = serializers.DateField(read_only=True)

    class Meta:
        model = Stat
        fields = ('id', 'url', 'activity', 'date', 'count')
