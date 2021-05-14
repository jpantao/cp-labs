# p05-jupyterhadoop
An introduction to map reduce with [Jupyter](https://jupyter.org/) and [Hadoop](http://hadoop.apache.org/).



Download the [Docker](https://www.docker.com/) image provided by the [professor](https://docentes.fct.unl.pt/joao-lourenco):
```bash 
docker pull joaomlourenco/spbd-1920-lab1
```

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

Now, just follow the instructions the professor left on the notebook. 
You can my implementations on the [code](code) directory.

---

### TODO: 
- Implement the sort map-reduce.