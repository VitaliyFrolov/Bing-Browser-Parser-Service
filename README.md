# Python Browser Parser Service

## Стек
- FastAPI + BeautifulSoup4
- Python
- Venv
- Docker
- Uvicorn

## Как этим пользоваться ?
Для получения данных о запросе необходимо дернуть ручку по url `/search?query={Ваш запрос}`.
Данные вернутся в формате JSON.
Пример ответа:
```
{
    "rank": number,
    "title": title,
    "link": link
}
```

Данный сервис работает с браузером www.bing.com

## Для запуска сервиса воспользуйтесь командой
``` bash
make build
```
После запустится контейнер API будет готов к использованию