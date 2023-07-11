from rest_framework import serializers
from backend.gallery.serializers import GallerySer
from backend.profiles.serializers import UserSer
from .models import *

class CoordSer(serializers.ModelSerializer):
    """Для вывода сложности"""
    class Meta:
        model = Coords
        fields = (
            "latitude",
            "longitude",
            "height",
        )

class LevelSer(serializers.ModelSerializer):
    """Для вывода сложности"""
    class Meta:
        model = Level
        fields = (
            "name",
        )

class FilterSer(serializers.ModelSerializer):
    """Для вывода сложности"""
    class Meta:
        model = FilterPereval
        fields = (
            "name",
        )

class PerevalListSer(serializers.ModelSerializer):
    """Для вывода новых данных"""
    level = LevelSer()
    coord = CoordSer()
    filters = FilterSer()
    images = GallerySer(read_only=True)
    user = UserSer()

    class Meta:
        model = Pereval_added
        fields = (
            "date_added",
            "status",
            "beautyTitle",
            "user",
            "level",
            "coord",
            "filters",
            "images",
            "slug",
        )

class PerevalDetailSer(serializers.ModelSerializer):
    """Для вывода полных данных о перевале"""
    level = LevelSer()
    coord = CoordSer()
    filters = FilterSer()
    images = GallerySer(read_only=True)
    user = UserSer()

    class Meta:
        model = Pereval_added
        fields = (
            "date_added",
            "status",
            "beautyTitle",
            "title",
            "other_titles",
            "user",
            "level",
            "coord",
            "filters",
            "images",
            "file",
        )

class PerevalCreateSer(serializers.ModelSerializer):
    """Добавление перевала"""
    level = LevelSer()
    coord = CoordSer()
    filters = FilterSer()
    images = GallerySer(read_only=True)
    user = UserSer()

    class Meta:
        model = Pereval_added
        fields = (
            "date_added",
            "status",
            "beautyTitle",
            "title",
            "other_titles",
            "user",
            "level",
            "coord",
            "filters",
            "images",
            "file",
        )

    def create(self, request):
        request["user"] = self.context['request'].user
        pereval = Pereval_added.odjects.create(**request)
        return pereval