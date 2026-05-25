from apps.posts.models import Signals
from .serializers import CommentSerializer
from .models import Comment

def get_comments(request, post_id):
    try:
        if not post_id:
            return {"error": "post id not found"}
    except post.DoesNotExist:
        return {"error": "post not found"}
    
    post = Signals.objects.get(id=post_id)
    comments = post.comments.all()
    serializer = CommentSerializer(comments, many=True)
    return comments

def post_comment(request, post_id):
    return {"message": "comment created"}