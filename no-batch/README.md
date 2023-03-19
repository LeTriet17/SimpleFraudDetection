
## Create the Dockerfile

The `Dockerfile` is made up of all the instructions required to build your image. If this is the first time you see this kind of file it might look intimidating but you will see it is actually easier than it looks. First take a look at the whole file:


## Build the image

Now that the `Dockerfile` is ready and you understand its contents, it is time to build the image. To do so, double check that you are within the `no-batch` directory and use the `docker build` command.
```bash
docker build -t fraud-detection .
```


## Run the container

Now that the image has been successfully built it is time to run a container out of it. You can do so by using the following command:

```bash
docker run --rm -p 80:80 fraud-detection
```

You should recognize this command from a previous ungraded lab. Let's do a quick recap of the flags used:
- `--rm`: Delete this container after stopping running it. This is to avoid having to manually delete the container. Deleting unused containers helps your system to stay clean and tidy.
- `-p 80:80`: This flags performs an operation knows as port mapping. The container, as well as your local machine, has its own set of ports. So you are able to access the port 80 within the container, you need to map it to a port on your computer. In this case it is mapped to the port 80 in your machine. 

At the end of the command is the name and tag of the image you want to run. 

After some seconds the container will start and spin up the server within. You should be able to see FastAPI's logs being printed in the terminal. 

Now head over to [localhost:80](http://localhost:80) and you should see a message about the server spinning up correctly.


