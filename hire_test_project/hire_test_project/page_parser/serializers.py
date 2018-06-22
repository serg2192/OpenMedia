from rest_framework import serializers

__all__ = ('TagsPostInputSerializer', 'TagsPostOutputSerializer',
           'TagsGetInputSerializer', 'TagsGetOutputSerializer')

class TagsPostInputSerializer(serializers.Serializer):
    # Можно поменять на CharField чтобы ослабить валидацию
    url = serializers.URLField()

class TagsPostOutputSerializer(serializers.Serializer):
    task_id = serializers.CharField()

class TagsGetInputSerializer(serializers.Serializer):
    task_id = serializers.CharField()

class TagsGetOutputSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    a = serializers.IntegerField(required=False)
    h1 = serializers.IntegerField(required=False)
    h2 = serializers.IntegerField(required=False)
    h3 = serializers.IntegerField(required=False)
    urls = serializers.ListField(required=False)