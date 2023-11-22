# Profiles microservice
Микровервис профилей в "Цифровом двойнике".

## Разработано с помощью:
- Python 3.11
- FastAPI
- PostgreSQL 
- SQLAlchemy v2
- Pydantic v2

## Сборка и запуск проекта:
    git clone https://github.com/AgroScience-Team/profiles-service.git

Если не создана docker-сеть `agronetwork`, то:

    docker create network agronetwork
    
Из корневой папки проекта:

    docker-compose up -d 

Swagger: `http://0.0.0.0:8001/docs`
