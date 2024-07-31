FROM ubuntu:latest
WORKDIR /mnt/e/Backup-IBM-2024/GitHub/curriculo-bruno
COPY requirements.txt ./
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 6419
COPY . .
CMD [ "grip", "BRUNO_LUIS_SANTINATO_Curriculum-Update-English-2024.md" ]
