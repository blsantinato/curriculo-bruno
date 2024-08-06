FROM redhat/ubi8
WORKDIR /mnt/e/Backup-IBM-2024/GitHub/curriculo-bruno
COPY requirements.txt ./
RUN yum update -y && yum install -y python3 python3-pip
#RUN apt-get install -y python-grip
RUN python3 -m pip install --no-cache-dir -r requirements.txt
EXPOSE 6419
COPY . .
CMD [ "grip", "BRUNO_LUIS_SANTINATO_Curriculum-Update-English-2024.md" ]
