FROM node:16

WORKDIR /app

RUN npm install yarn
COPY package.json ./
RUN yarn

COPY ./static/index.html ./static/index.html
COPY server.js ./server.js

EXPOSE 8999

ENTRYPOINT [ "node", "server.js" ]