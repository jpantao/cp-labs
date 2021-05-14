# p05-jupyterhadoop
An introduction to map reduce with [Jupyter](https://jupyter.org/) and [Hadoop](http://hadoop.apache.org/).



Download the [Docker](https://www.docker.com/) image provided by the [professor](https://docentes.fct.unl.pt/joao-lourenco):
```bash 
docker pull joaomlourenco/spbd-1920-lab1
```
The logs of the attack can be downloaded from [https://www.dropbox.com/s/0r8902uj9yum7dg/web.log?dl=0](https://www.dropbox.com/s/0r8902uj9yum7dg/web.log?dl=0)

**Running the docker image with the mount:**
```bash
docker run -v $(pwd)/code:/home/jovyan/work/code -p 8888:8888 joaomlourenco/spbd-1920-lab1
```

I prefer to edit the code for the mappers and reducers locally, so I have them on the
[code](code) directory and run *-v* option in order to have the local files 
available inside the container.
Follow the links on the output of the previous command to access the notebook through your browser.


**To get a shell the container:**
```bash
docker exec -it $( docker container ls | grep joaomlourenco/spbd-1920-lab1 | awk '{print $1}') /bin/bash
```

---

### TODO: 
1. Count the number of unique IP addresses involved on the attack.
2. For each interval of 10 seconds, provides the following
information: [number of request, average execution time,
maximum time, minimum time].
3. Create an inverted index that for each interval of 10 second,
has a list of (unique) IPs executing accesses.