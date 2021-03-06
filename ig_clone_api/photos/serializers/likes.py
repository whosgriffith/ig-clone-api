""" Like serializer. """

# Django REST Framework
from rest_framework import serializers
# Models
from ig_clone_api.photos.models import Photo
from ig_clone_api.photos.models import Like


class LikeModelSerializer(serializers.ModelSerializer):
    """ Like model serializer. """

    user = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        """ Meta class. """

        model = Like
        fields = ('user', 'photo')
        read_only_fields = ('user', 'photo')

    def validate(self, attrs):
        photo_pk = self.context['view'].kwargs["photo_pk"]
        try:
            photo = Photo.objects.get(id=photo_pk)
        except Photo.DoesNotExist:
            raise serializers.ValidationError({"detail": "The photo doesn't exist."})
        attrs["photo"] = photo
        return attrs

    def create(self, validated_data):
        # Get the photo pk from the view context (DRF-nested-routers) and
        # create the new like with the validated_data
        like, created = Like.objects.get_or_create(**validated_data)
        photo_pk = self.context['view'].kwargs["photo_pk"]
        photo = Photo.objects.get(id=photo_pk)
        if created:
            photo.total_likes += 1
            photo.save()
        return like
