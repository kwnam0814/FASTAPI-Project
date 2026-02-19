### 게시판 로직 구성
# 게시글 객체들을 저장할 리스트를 생성.
# 각 게시글의 고유한 식별 번호를 위한 변수 만들기.
# FastAPI의 본체인 main.py와 분리되었으므로, Endpoint를 연결할 Router를 생성.

# 공통 URL 경로 설정
# 여러 엔드포인트에서 공통적으로 사용하는 경로를 통합하여 관리.
# FastAPI에서는 APIRouter 인스턴스 생성 시 경로 접두사를 설정하여 코드 중복을 제거.
# 하위 메서드에서는 공통 경로를 제외한 나머지 경로만 정의함.
# tag를 통해 swagger를 그룹화할 수 있음.

# mysite/post_api.py

from fastapi import APIRouter
from .post import Post

router = APIRouter(prefix="/posts", tags=["Post"])

# 게시글 객체들을 저장하는 리스트
posts = []
post_id = 0

# 초기 데이터 추가를 위한 구문
posts.append(Post(1, "기본 제목", "기본 내용"))
post_id = 1


@router.post("")
def create_post():
    global post_id
    post_id += 1

    post = Post(post_id, "제목", "내용")

    # 리스트에 추가
    posts.append(post)

    return post


@router.get("")
def read_posts():
    # 게시글 리스트 전체를 반환
    return posts


@router.get("/{id}")
def read_post_by_id(id: int):
    # 리스트 내 객체들을 하나씩 검사
    for post in posts:
        # 객체의 식별자와 입력받은 식별자가 일치하는지 확인
        if post.id == id:
            return post
    return None


@router.put("/{id}")
def update_post(id: int):
    for post in posts:
        if post.id == id:
            # 객체의 속성 값 변경
            post.title = "수정된 제목"
            post.content = "수정된 내용"
            return post
    return None


@router.delete("/{id}")
def delete_post(id: int):
    # 리스트를 순회하며 인덱스(i)와 내용(post)을 함께 추출
    for i, post in enumerate(posts):
        if post.id == id:
            # 해당 인덱스의 데이터를 삭제하고 루프 종료
            posts.pop(i)
            return "삭제 완료"

    return "삭제 실패"
