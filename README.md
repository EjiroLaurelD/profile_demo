For this task, I created my profile demo using a template.
I created a docker file and created an image from it which i have succesfully pushed to dockerhub.

- To build the image run `docker build -t profile-demo .` 
- To run the container use the command 
`docker run -d -it -p 8080:80 --name portfolio profile-demo`
- curl localhost:8080 or check you IP if you are working from an instance to be sure image is running.

- I created a profile on dockerhub and pushed my image to the hub with the fowllowing commands
- `docker login` this will prompt for your username and password
- commit the image to docker with this command ` docker commit <Container ID> <docker name>/<new name for image>:<verion>`
`docker commit 76573627526 ejirolaureld/profile-demo:2`

- After committing the image, I pushed to docker hub with the following command
`docker push ejirolaureld/profile-demo:2`

- This image has been pushed to Dockerhub.com
To pull, run the following command:
`docker pull ejirolaureld/profile-demo:2`

