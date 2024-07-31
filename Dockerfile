FROM python:3
WORKDIR /mnt/e/Backup-IBM-2024/GitHub/curriculo-bruno
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "grip", "BRUNO_LUIS_SANTINATO_Curriculum-Update-English-2024.md" ]
