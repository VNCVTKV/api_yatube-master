from posts.models import Post, Group, Comment
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'pub_date', 'text', 'image', 'group', 'author')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')



#admin token: 9060e867ad98463ffd05bd6c51556add6836351e 