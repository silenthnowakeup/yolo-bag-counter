# YOLO Object Counter
#### Этот проект представляет собой систему подсчета строительных мешков на видео с использованием модели YOLO и OpenCV. Видео обрабатывается в контейнере Docker, результаты сохраняются в указанную папку на хосте.

## Требования

- python 3+
- Docker
- opencv-python
- ultralytics

## Установка и запуск
### 1. Клонирование репозитория

```
git clone https://github.com/silenthnowakeup/yolo-bag-counter.git  
cd yolo-object-counter
```

### 2. Добавление весов модели
Скачайте файл с весами модели YOLO (например, **best.pt**) и поместите его в корневую директорию проекта.

### 3. Структура проекта

Убедитесь, что структура вашего проекта выглядит следующим образом:

```
/project-directory
│
├── best.pt
├── Dockerfile
├── requirements.txt
├── src
│   ├── main.py
│   ├── ObjectCounter.py
├── input
│   └── Задание.mp4
└── output
```

### 4. Создание и запуск контейнера Docker

```
# Создание Docker-образа
docker build -t yolo-object-counter .

# Запуск контейнера с монтированием папок input и output
docker run -v $(pwd)/output:/app/output -v $(pwd)/input:/app/input yolo-object-counter
```

### 5. Результаты

После завершения обработки видео файл с результатами будет доступен в папке **output**.
