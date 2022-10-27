ARG NODE_VERSION=16.14-alpine

FROM node:${NODE_VERSION} as node

FROM node as client-local-build

ARG APP_HOME=/app/

WORKDIR ${APP_HOME}

COPY package.json .
COPY yarn.lock .

RUN yarn install

COPY . ${APP_HOME}

CMD [ "yarn", "run", "start" ]