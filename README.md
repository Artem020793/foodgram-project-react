# Продуктовый помощник

Foodgram - социальная сеть для публикации рецептов. Сайт выполнен на основе django rest framework и react. В Foodgram реализована функция подписки на авторов, добавление рецептов в избранное, ингредиенты в список покупок, скачивать список покупок

## Для использования сайта перейдите по ссылке http://51.250.106.189

Для доступа к админке

http://51.250.106.189/admin

Логин: artem@mail.ru
Пароль admin

# Для локального запуска

Загрузите репозиторий

```bash
git@github.com:Artem020793/foodgram-project-react.git
```

Перейдите в папку /infra/

```bash
cd infra/
```

Заполните .env файлы. Например:

DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

Выполните команды

```bash
docker-compose up -d --build
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic --no-input
docker-compose exec backend python manage.py import_csv
```

перейдите http://localhost/
