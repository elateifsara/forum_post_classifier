# Requirements

## Run locally

Run `pip install requirements.txt` to install all the needed libraries to run the app.
Then type in the terminal `flask run` or `python app.py` that will run the flask API.

**Note:**  
Make sure you run the model notebook to generate the model files you will need to run the app.

## Run the docker

- Build the docker first : `docker build -t demo-flask:v0 .`
- Run the docker : `docker run -p 8501:8501 demo-flask:v0`
- To test the app visit :  `http://localhost:5000`  

## Troubleshooting for docker  

- Check the docker file currently running: `docker ps`
- Shut down the docker container: `docker stop container_id`
- Check if the port is already used: `lsof -i tcp:8501`
- Kill currently running process: `kill -9 7240`

# Resources

This app is based on the available resources:
- [Develop a NLP Model in Python & Deploy It with Flask, Step by Step](https://towardsdatascience.com/develop-a-nlp-model-in-python-deploy-it-with-flask-step-by-step-744f3bdd7776)
- [Running a Flask application inside a Docker container.](https://felipefaria.medium.com/running-a-simple-flask-application-inside-a-docker-container-b83bf3e07dd5)
- [Build and Deploy your Machine Learning Application with Docker](https://dev.to/aminu_israel/build-and-deploy-your-machine-learning-application-with-docker-5322?fbclid=IwAR3lwF_Hzt5Gvte0Ci1GfbBJoABXoF9VEDdnvcsBQm5E9vSws1ZB7eVo7j8) 
- [SMS-Message-Spam-Detector](https://github.com/susanli2016/SMS-Message-Spam-Detector)
- [Simple transformers tutorial (which the model is built upon)](https://medium.com/swlh/simple-transformers-multi-class-text-classification-with-bert-roberta-xlnet-xlm-and-8b585000ce3a)
- For the model please check out the provided notebook using Colab.
