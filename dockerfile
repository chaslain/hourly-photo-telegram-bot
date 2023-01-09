FROM "amazon/aws-lambda-python"


WORKDIR '/var/task'
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY bot bot


CMD ["bot.index.handler"]