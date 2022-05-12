# 1. build vue.js application
FROM node:lts-alpine AS build

ENV HOME=/home/app/

RUN mkdir -p $HOME
#Set work directory
WORKDIR $HOME

# copy application
COPY . $HOME

ENV VUE_APP_BASE_URL=""
ENV VUE_APP_REQUEST_TIMEOUT=0

#install all node packages
RUN yarn install && yarn run build

# 2. Setup nginx
FROM nginx:1.21.6-alpine

RUN mkdir -p /home/app/
WORKDIR /home/app/
COPY --from=build /home/app/.nginx/nginx.conf /etc/nginx/conf.d/default.conf

WORKDIR /usr/share/nginx/html
COPY --from=build /home/app/dist ./

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
