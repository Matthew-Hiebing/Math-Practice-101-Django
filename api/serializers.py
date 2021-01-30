from rest_framework import serializers


class GamePropertiesSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        preference = instance['splash_screen']['preference']
        content = instance['splash_screen']['content']

        return {
            'splash_screen': {
                'splash_screen_text': content.splash_screen_message,
                'splash_screen_preference': preference.display_on_refresh
            },
        }
