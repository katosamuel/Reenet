from apps.comments.queries import CommentQueries

class DeleteComment():
    @staticmethod
    def execute(post_id: int, comment_id: int) -> bool:
        comment = CommentQueries.get_comment(post_id=post_id, comment_id=comment_id)
        comment.delete()
        return True
