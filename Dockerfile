FROM nikolaik/python-nodejs:latest

WORKDIR /home/pn

COPY . .

RUN pip install -r requirements.txt && npm install

EXPOSE 5000

USER pn

CMD npm run dev