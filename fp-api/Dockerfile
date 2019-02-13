FROM node:8

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .
RUN rm data.json 
RUN rm Dockerfile

EXPOSE 3000
CMD [ "node", "app.js" ]