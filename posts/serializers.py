from rest_framework import serializers
from posts.models import Post, Comment
from django.contrib.auth.models import User


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='post-highlight', format='html')


    class Meta:
        model = Post
        fields = ('url', 'id', 'highlight', 'owner','image','title', 'content','name','subscribe', 'draft', 'comment')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='comment-highlight', format='html')

    class Meta:
        model = Comment
        fields =('url', 'id', 'highlight', 'content','owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts= serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'last_name', 'email','posts')

    def create(self, validated_data):
        """
        Create and return a new `comment` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `comment` instance, given the validated data.
        """
        instance.content = validated_data.get('content', instance.content)
        instance.title = validated_data.get('title', instance.title)
        instance.name = validated_data.get('name', instance.name)
        instance.subscribe = validated_data.get('subscribe', instance.subscribe)
        instance.draft = validated_data.get('draft', instance.draft)
        instance.save()
        return instance


