# Open API 라이브러리
- 설치방법
```bash
pip install git+https://github.com/dev-bleck/api_project.git
```

- 사용방법
```python
from my_api import naver_api

search_api(url, naver_keys["CLIENT_ID"], naver_keys["CLIENT_SECRET"], params = params)

translate_api(text, url, naver_keys["CLIENT_ID"], naver_keys["CLIENT_SECRET"]) # default source = "en", target ="


```
