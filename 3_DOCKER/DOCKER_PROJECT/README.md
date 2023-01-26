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

1. Create a new conda environment for provide proper environment, <br>to execute the app.py in your local machine. let's create a new environment "industryready" 

- **conda create -n ENV_NAME**

![](./images/1_conda_create_n_ENV.PNG)
