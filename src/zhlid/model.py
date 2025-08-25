import torch
import torch.nn as nn
from typing import List, Union
from transformers import AutoModelForSequenceClassification, AutoTokenizer



class Model:
    def __init__(
        self,
        model_path: str,
        **kwargs
    ):
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path, **kwargs)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)    
    
    def get_id2label(
        self
    ):
        id2label = self.model.config.id2label
        return id2label

    def get_label2id(
        self
    ):
        label2id = self.model.config.label2id
        return label2id

    def predict(
        self,
        text: Union[str, List[str]]
    ):
        inputs = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            logits = self.model(**inputs.to("cuda"))["logits"][0]
        scores = nn.functional.softmax(logits, dim=-1)
        idx = torch.argmax(scores).item()
        pred_score = scores[idx].item()
        pred_score = round(pred_score, 10)
        id2label = self.get_id2label()
        pred_label = id2label[idx]

        return (pred_label, pred_score)


def load_model(model_path: str = "MusubiAI/ZHLID", **kwargs):
    return Model(model_path=model_path, **kwargs)

