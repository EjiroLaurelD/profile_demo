FROM nginx:latest

# Install dependencies
WORKDIR  /usr/share/nginx/html

# copy files into html directory
COPY  . .

# exposes port 80 on the container
EXPOSE 80
