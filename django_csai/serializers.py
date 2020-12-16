from rest_framework import serializers

from django_csai.models import Dictionary, Document


class DictionarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dictionary
        fields = ['text', 'label', 'start', 'end', 'document']


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    annotations = DictionarySerializer(many=True, read_only=True)

    class Meta:
        model = Document
        fields = ['document', 'annotations']
