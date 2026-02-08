FROM nikolaik/python-nodejs:python3.12-nodejs22

WORKDIR /home/pn

COPY . .

RUN pip install -r requirements.txt && npm install
RUN chmod +x ./docker/entrypoint.sh

EXPOSE 8000

CMD ["./docker/entrypoint.sh"]
