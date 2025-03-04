FROM ubuntu:20.04

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
  python3 python3-pip wget unzip && \
  apt-get clean

# Устанавливаем vosk-api
RUN pip3 install vosk

# Загружаем модель (замени ссылку на нужную)
WORKDIR /opt/vosk
RUN wget https://alphacephei.com/vosk/models/vosk-model-en-us-0.42-gigaspeech.zip && \
  unzip vosk-model-en-us-0.42-gigaspeech.zip && \
  rm vosk-model-en-us-0.42-gigaspeech.zip   

# Копируем скрипт для запуска сервиса
COPY server.py /opt/vosk/server.py

# Открываем порт
EXPOSE 2700

# Запускаем сервис
CMD ["python3", "/opt/vosk/server.py"]