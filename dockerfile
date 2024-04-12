FROM nikolaik/python-nodejs:latest

WORKDIR /home/pn

COPY . .

RUN pip install -r requirements.txt && npm install

RUN npm run style

EXPOSE 5000

USER pn

CMD npm run app