from apps.posts.queries.post_queries import PostQueries

class DeletePost:
    @staticmethod
    def execute(post_id):
        post = PostQueries().get_post(post_id)
        if post is not None:
            post.delete()
            return True
        return False

        