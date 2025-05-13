from rest_framework.serializers import ModelSerializer, SlugRelatedField
from uploader.serializers import ImageSerializer
from uploader.models import Image

from core.models import Livro


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"


class LivroListRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1
