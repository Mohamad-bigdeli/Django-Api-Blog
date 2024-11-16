from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]
class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ["id", "author", "title", "image", "content", "snippet", "status", "absolute_url", "relative_url", "created_date", "published_date"]
        read_only_fields = ["author"]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_url(obj.pk)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        rep["category"] = CategorySerializer(instance.category, 
                                            context={"request":request}).data        
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("content", None)
        return rep
    
    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(user__id=self.context.get("request").user.id) 
        return super().create(validated_data)