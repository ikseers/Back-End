# FROM nginx:stable-alpine
# COPY nginx/default.conf /etc/nginx
# COPY nginx/default.conf /etc/nginx/conf.d
# EXPOSE 80
FROM nginx:1.25

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d
