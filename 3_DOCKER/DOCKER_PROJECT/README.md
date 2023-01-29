# DOCKER PROJECT

<span style="font-size:20px;">**Problem Statement:**</span><span style="font-size:16px;"> Create an application in flask web framework, converting it as a Docker image file and run it as a Docker container to execute the application.</span>

Steps:

1. Create app.py file as the base file to execute the application.

2. Create requirements.txt file for the required packages and libraries and frameworks.

3. Create a Dockerfile to run requirements.txt file and execute app.py (application) file.


File and code:

1. app.py file

```PYTHON
from flask import Flask
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])

def home():
    return "Hello World"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```
2. requirements.txt file

```TEXT
flask
numpy
pandas
```

3. Dockerfile 

```DOCKER
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## OPTIONAL STEPS:

1. Create a new conda environment for provide proper environment, <br>to execute the **app.py** in your local machine. **let's create a new environment "industryready"** 

- **conda create -n ENV_NAME**

![](./images/1_conda_create_n_ENV.PNG)

2. Listing out all the conda environment.

- **conda env list**

![](./images/2_conda_env_list.PNG)

3. To activate the conda environment Here, in this case **environment name<br>(or) ENV_NAME** is "industryready"

- **conda activate ENV_NAME**

![](./images/3_conda_activate_industryready.PNG)

4. To deactivate that environment, use this command

- **conda deactivate**

![](./images/4_conda_deactivate.PNG)

<br>

5. Doing all the above steps :

![](./images/gif/1_creating_conda_env.gif)



## Let's build our project docker image:

1. To build docker image, use this command

- **docker build -t docker-project .**

![](./images/5_creating_custome_docker_image.PNG)

this is docker image 

![](./images/8_project_docker_img.PNG)

2. Check our custome project docker image

- **docker ps**

![](./images/9_docker_ps_for_dockerProject.PNG)

![](./images/6_created_docker_image.PNG)

3. Run docker container

- **docker run -d -p 5000:5000 docker-project**

![](./images/7_created_docker_container.PNG)

4. check whether docker container is running or not using **docker ps** command

![](./images/gif/2_creating_docker_image.gif)

5. **Completing the project**

![](./images/gif/3_project_completed.gif)

 **This is the output displayed from our custome docker image, docker container:**

![](./images/11_completion_of_project.PNG)


<br>Now, we created our own flask application and build our docker image and run docker container **successfully** getting the expected output further we can **push this image to docker hub** too.


## <span align="center">Thank you</span> 