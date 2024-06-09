# Profiles microservice
Микровервис профилей в "Цифровом двойнике".

## Разработано с помощью:
- Python 3.11
- FastAPI
- PostgreSQL 
- SQLAlchemy v2
- Pydantic v2
- AIOKafka

## Сборка и запуск проекта:
    git clone https://github.com/AgroScience-Team/profiles-service.git

Поднять Kafka: https://github.com/AgroScience-Team/kafka/blob/main/README.md    

Если не создана docker-сеть `agronetwork`, то:

    docker create network agronetwork
    
Выполнить миграции (при необходимости):

    docker compose -f docker-compose.yml run migrations

Из корневой папки проекта:

    docker compose up -d 

Swagger: `http://0.0.0.0:8001/docs`
