# flask_study
공부 내용을 적어보자  
## 기본 템플릿  
```
FLASK_STUDY
├── app
├── model
├── resources
├── templates
├── model
├── tests
├── app.py
└── test_app.py
```
## 테스트 코드 실행
```
$ ptw  # 지속적으로 변화 관찰 가능
$ pytest  # 일시적 테스트
```
## Flask 실행
실행 파일이 app.py라면 `flask run` 으로 실행 가능
```
$ FLASK_APP=run.py flask run 
```
* templates 디렉토리 아래에 html을 넣은 후 `render_template` 함수를 통해서 불러 올수 있음
* 디렉토리명이 다르다면 인식이 안됨 
* html 내부 함수 
    * `{{value}}`: `template_render`함수 인자로 받아 올 수 있음
    * `{{url_for()}}`: 해당 url로 이동