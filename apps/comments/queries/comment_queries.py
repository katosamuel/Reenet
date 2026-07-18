from apps.posts.queries import PostQueries
from apps.comments.models import Comment

class CommentQueries:

    @staticmethod
    def get_comment(post_id: int, comment_id: int) -> Comment:
        # post = PostQueries.get_post(post_id=post_id)
        comment = Comment.objects.get(id=comment_id, post__id=post_id)
        return comment
    
    @staticmethod
    def get_comment_list(post_id: int) -> Comment:
        post = PostQueries.get_post(post_id=post_id)
        comments = Comment.objects.filter(post=post)
        return comments