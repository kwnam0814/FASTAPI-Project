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
