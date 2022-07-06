from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework.serializers import ModelSerializer
from .models import InstallDetails
from .documents import InstallDocument


class InstallSerializder(ModelSerializer):
    class Meta:
        model = InstallDetails
        fields = ['carrier', ]


class InstallDocSerializer(DocumentSerializer):
    class Meta:
        document = InstallDocument
        fields = ['carrier', ]