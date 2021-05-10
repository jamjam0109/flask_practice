![](static/assets/usage.gif)

## git clone 
```console
$ git clone https://github.com/jamjam0109/mbo.git
$ cd mbo 
```

## virtualenv 세팅
```console
$ virtualenv venv 
$ source venv/bin/activate
```

## pip install
```console
$ pip install -r requirements.txt
```

## flask_uploads.py 수정 
- ~/venv/lib/python3.x/site-packages/flask_uploads.py 의 384번째 라인 수정
- secure_filename 함수 제거 
변경 전 
```python
return lowercase_ext(secure_filename(filename))
```
---
변경 후 
```python
return lowercase_ext(filename)
```

## 실행 
```console
$ python app.py
```


