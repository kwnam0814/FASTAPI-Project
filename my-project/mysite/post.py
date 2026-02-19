### 게시글 클래스 정의
# 데이터의 기본 단위가 되는 클래스를 작성.

# mysite/post.py


class Post:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
