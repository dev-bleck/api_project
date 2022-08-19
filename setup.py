# setup.py 파일이 있으면 pip로 설치 가능
from setuptools import setup

setup(
    name = "myapi", # 이 이름으로 패키지 설치
    version = "0.0.1", # 릴리즈.메이저.마이너 넘버
    description = "my api lib", # 설명
    url = "https://github.com/dev-bleck/api_project.git",
    author = "bleck", # 개발자 이름
    author_email = "bleckshitup@gmail.com",
    packages = ["my_api"], # 패키지 명
    install_requires = [
        "requests"
    ] # import한 library
)