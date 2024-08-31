# Docker ShadowSocks server

### Подготовка

Перед началом работы скопируйте файл **example-config.yml** как **config.yml** и в нем сконфигурируйте столько экземпляров ShadowSocks сколько вам нужно.

Создайте файл Docker Compose командой

    python3 main.py

### Работа с Docker Compose

Первый запуск

    docker-compose up -d

Перезагрузка для применения изменений

    docker-compose restart

Остановка

    docker-compose down
