FROM nikolaik/python-nodejs:latest

WORKDIR /home/pn

COPY . .

RUN pip install -r requirements.txt && npm install

EXPOSE 8000

CMD npm start
