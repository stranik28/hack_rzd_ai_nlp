# hack_rzd_ai_nlp

# Для запуска прописать
```angular2html
docker compose up --build
```

# Для подключения к ML образу нужно прописать адресс 
```angular2html
./server/routers/verify.py
```
```
response = requests.post('http://ml:7777/send', files=files)
```