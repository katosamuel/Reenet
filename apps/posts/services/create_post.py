from apps.posts.models import Post

class CreatePost:
    def execute(self, *, author, content):
        post = Post.objects.create(author=author, signal_text=content)
        return post
    