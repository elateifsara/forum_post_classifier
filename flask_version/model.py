import os
import tarfile
from simpletransformers.classification import ClassificationModel
import re
from bs4 import BeautifulSoup

def unpack_model(model_name=''): 
    tar = tarfile.open(f"{model_name}.tar.gz", "r:gz")
    tar.extractall()
    tar.close()
    
unpack_model('amazonforum-bert-categclass')

# define hyperparameter
train_args ={"reprocess_input_data": True,
            "overwrite_output_dir": True,
            "fp16":False,
            "num_train_epochs": 4}

# Create a ClassificationModel
model = ClassificationModel(
    "bert", "outputs/",
    num_labels=11,
    args=train_args,
    use_cuda=False
)

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\'\“\”\’\|@,;]')
    
def clean_text(text):
    """
        text: a string
        return: modified initial string
    """
    text = BeautifulSoup(text, "lxml").text # HTML decoding
    text = text.lower() # lowercase text
    text = REPLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text
    return text

class_list = ['Fulfillment By Amazon', 'Selling on Amazon',
    'Amazon Marketplace Web Service (MWS)',
    'Amazon Sponsored Products', 'Account Health', 'Global Selling',
    'Amazon Pay', 'Groups',
    'Health,Safety,Sustainability,Security & Compliance',
    'Login With Amazon', 'Amazon Custom']

def predict(post):
    predictions, raw_outputs = model.predict([clean_text(post)])
    return class_list[predictions[0]]