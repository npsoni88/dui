# DUI - Docker UI
A simple yet helpful web front-end for docker newbies to help them manage their containers and images.

## How to use?
You simlpy need to pull the docker image and run the app as a container. Execute the following command

        docker run -itd -v /var/run/docker.sock:/var/run/docker.sock -p 8080:5000 dui:latest
