FROM python:3
WORKDIR /usr/src/app
ENV DB_HOST=localhost
ENV DB_USER=root
ENV DB_PASSWORD=root
ENV TELEGRAM_TOKEN=00000000000000000000000
COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./start.py" ]