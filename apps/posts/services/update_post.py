
class UpdatePost:
    def execute(self, *, post, validated_data):
        post.save(update_fields=validated_data["signal_text"])
        return post