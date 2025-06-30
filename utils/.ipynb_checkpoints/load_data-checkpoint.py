from sklearn.utils.class_weight import compute_class_weight 
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer
from transformers import DataCollatorWithPadding
from sklearn.model_selection import StratifiedKFold, KFold
from transformers import set_seed 
import copy
import evaluate
import re
import torch 
from sklearn.preprocessing import LabelEncoder 
set_seed(42)

def clean_text(text): 
    special_chars = r'[\"\[\]\',]'
    cleaned_text = re.sub(special_chars, '', text)
    # replace - or _ with space 
    special_chars = r'[\_\-]'
    cleaned_text2 = re.sub(special_chars,' ', cleaned_text)
    return cleaned_text2 

clf_metrics = evaluate.combine(["accuracy", "f1", "precision", "recall"])

def sigmoid(x):
   return 1/(1 + np.exp(-x))

def compute_metrics(eval_pred):
   predictions, labels = eval_pred
   predictions = sigmoid(predictions)
   predictions = (predictions > 0.5).astype(int).reshape(-1)
   return clf_metrics.compute(predictions=predictions, references=labels.astype(int).reshape(-1))

tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')  
# re-format output 
def clean_text(text): 
    special_chars = r'[\_/-]'
    cleaned_text = re.sub(special_chars,' ', text)                # replace - or _ or / with space 
    cleaned_text = re.sub(r'[^a-zA-Z0-9 -/()]', '', cleaned_text) # remove any non-alphanumeric /space character
    return cleaned_text.lower()   
# to create a batch of examples. This dynamically pads the text to the lenght of the longest element in the batch. 
def preprocess(example):
        # preprocess and tokenize data 
        text = f"{example['Statement Description']}"       # our text to be labeled is the description of the KD
        text = text[13:]                                   # remove "Knowledge of" since it's the same for every KD
        text = clean_text(text)                            # remove special characters
        one_hot = list(example.values())[0:9]              # read one-hot encoding 
        example = tokenizer(text)                          # tokenize text 
        example['labels'] = torch.tensor(one_hot).float()
        return example 

def preprocess8(example):
    # preprocess and tokenize data 
    text = f"{example['Statement Description']}"       # our text to be labeled is the description of the KD
    text = text[13:]                                   # remove "Knowledge of" since it's the same for every KD
    text = clean_text(text)                            # remove special characters
    one_hot = list(example.values())[1:9]              # read one-hot encoding 
    example = tokenizer(text)                          # tokenize text 
    example['labels'] = torch.tensor(one_hot).float()
    return example 

def preprocess_csec(example):
    # preprocess and tokenize data 
    text = f"{example['topics']}"       # our text to be labeled is the description of the KD
    text = clean_text(text)                            # remove special characters
    one_hot = list(example.values())[1:10]              # read one-hot encoding 
    example = tokenizer(text)                          # tokenize text 
    example['labels'] = torch.tensor(one_hot).float()
    return example 

def preprocess_csec8(example):
    # preprocess and tokenize data 
    text = f"{example['topics']}"       # our text to be labeled is the description of the KD
    text = clean_text(text)                            # remove special characters
    one_hot = list(example.values())[2:10]              # read one-hot encoding 
    example = tokenizer(text)                          # tokenize text 
    example['labels'] = torch.tensor(one_hot).float()
    return example 
#### 

def get_new_labels(y): 
    y_new = LabelEncoder().fit_transform([''.join(str(l)) for l in y])
    return y_new 