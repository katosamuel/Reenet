from apps.posts.models import Signals
from .models import Comment

def get_comments(request, post_id):
    try:
        if not post_id:
            return {"error": "post id not found"}
            
        post = Signals.objects.get(id=post_id)
        comments = post.comments.all()
        return comments
        
    except Signals.DoesNotExist:
        return {"error": "post not found"}

def post_comment(user, post_id, validated_data):
    post = Signals.objects.get(id=post_id)
    comment = Comment.objects.create(user=user, post=post, text_content=validated_data["text_content"])
    return comment;