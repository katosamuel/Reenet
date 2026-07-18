from apps.comments.models import Comment
from apps.posts.queries import PostQueries

class CreateComment:
    @staticmethod
    def execute(user, post_id: int, content: str) -> Comment:
        post =  PostQueries.get_post(post_id=post_id)
        comment = Comment.objects.create(user=user, post=post, content=content)
        return comment