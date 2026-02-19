### 게시판 로직 구성
# 게시글 객체들을 저장할 리스트를 생성.
# 각 게시글의 고유한 식별 번호를 위한 변수 만들기.
# FastAPI의 본체인 main.py와 분리되었으므로, Endpoint를 연결할 Router를 생성.

# mysite/post_api.py

from fastapi import APIRouter
from .post import Post

router = APIRouter()

# 게시글 객체들을 저장하는 리스트
posts = []
post_id = 0

# Create - 게시글 작성
# 특정 주소로 요청을 보낼 때 새로운 게시글 객체를 생성하고 리스트에 추가.
# mysite/post_api.py 내부에 추가


@router.get("/posts/create")
def create_post():
    # 식별자 1 증가
    global post_id
    post_id += 1

    # 새로운 게시글 객체 생성
    post = Post(post_id, "제목", "내용")

    # 리스트에 추가
    posts.append(post)

    return post


## Read - 전체 게시글 조회
# 현재 리스트에 저장된 모든 게시글 데이터를 반환.
# 데이터 확인을 위해 초기화 로직을 추가할 수 있음.
# mysite/post_api.py 내부에 추가

# 초기 데이터 추가를 위한 구문
posts.append(Post(1, "기본 제목", "기본 내용"))
post_id = 1


@router.get("/posts")
def read_posts():
    # 게시글 리스트 전체를 반환
    return posts


# Read - 단일 게시글 조회
# 단일 게시글을 식별하기 위한 id가 필요.


# 경로 매개변수(path parameter)
# 주소 경로에 변수를 포함하여 데이터를 전달하는 방식.
# 중괄호를 사용하여 변수명을 지정.
@router.get("/articles/{id}")
def get_article(id: int):
    # 매개변수로 전달받은 id를 활용
    return f"글 번호: {id}"


# 단일 게시글 조회
# 리스트를 순회하며 요청받은 식별자와 일치하는 객체를 탐색.
# mysite/post_api.py 내부에 추가


@router.get("/posts/{id}")
def read_post_by_id(id: int):
    # 리스트 내 객체들을 하나씩 검사
    for post in posts:
        # 객체의 식별자와 입력받은 식별자가 일치하는지 확인
        if post.id == id:
            return post
    return None


# Update - 게시글 수정
# 특정 식별자의 게시글을 찾아 내부 데이터를 변경.

# mysite/post_api.py 내부에 추가


@router.get("/posts/{id}/update")
def update_post(id: int):
    for post in posts:
        if post.id == id:
            # 객체의 속성 값 변경
            post.title = "수정된 제목"
            post.content = "수정된 내용"
            return post
    return None


# 게시글 삭제
# 특정 식별자와 일치하는 게시글을 찾아 리스트에서 제거.

# mysite/post_api.py 내부에 추가


@router.get("/posts/{id}/delete")
def delete_post(id: int):
    # 리스트를 순회하며 인덱스(i)와 내용(post)을 함께 추출
    for i, post in enumerate(posts):
        if post.id == id:
            # 해당 인덱스의 데이터를 삭제하고 루프 종료

            return posts.pop(i)

    return "삭제 실패"
