# Requirements

## Run locally

Run `pip install requirements.txt` to install all the needed libraries to run the app.
Then type in the terminal `streamlit run post_categ.py` that will run the streamlit app.

**Note:**  
Make sure you run the model notebook to generate the model files you will need to run the app.

## Run the docker

- Build the docker first : `docker build -t demo-streamlit:v0 .`
- Run the docker : `docker run -p 8501:8501 demo-streamlit:v0`
- To test the app visit :  `http://localhost:8501/`  

## Troubleshooting for docker  

- Check the docker file currently running: `docker ps`
- Shut down the docker container: `docker stop container_id`
- Check if the port is already used: `lsof -i tcp:8501`
- Kill currently running process: `kill -9 7240`

## Resources

This app is based on the available resources:
- [Deploy an NLP model with Streamlit and Heroku](https://medium.com/analytics-vidhya/deploy-an-nlp-model-with-streamlit-and-heroku-5f0ae4b9048c#b77d)
-[Deploy a machine learning application with Streamlit and Docker on AWS](https://towardsdatascience.com/how-to-deploy-a-semantic-search-engine-with-streamlit-and-docker-on-aws-elastic-beanstalk-42ddce0422f3)
- [Build and Deploy your Machine Learning Application with Docker](https://dev.to/aminu_israel/build-and-deploy-your-machine-learning-application-with-docker-5322?fbclid=IwAR3lwF_Hzt5Gvte0Ci1GfbBJoABXoF9VEDdnvcsBQm5E9vSws1ZB7eVo7j8) 
- [Simple transformers tutorial (which the model is built upon)](https://medium.com/swlh/simple-transformers-multi-class-text-classification-with-bert-roberta-xlnet-xlm-and-8b585000ce3a)
- For the model please check out the provided notebook using Colab.
