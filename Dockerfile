# Используем базовый образ Python
FROM python:3.9-slim

# Установка системных зависимостей для OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Установка Python-зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Создание рабочей директории
WORKDIR /app

# Копирование кода приложения в контейнер
COPY . .

# Создание тома для сохранения видео
VOLUME /app/output

# Запуск скрипта
CMD ["python", "src/main.py"]
