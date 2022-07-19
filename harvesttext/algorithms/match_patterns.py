import re
import jieba
import jieba.posseg
from harvesttext import HarvestText

def AllEnglish():
    return lambda x: bool(re.fullmatch(r"[a-zA-Z]*",x))

def AllEnglishOrNum():
    return lambda x: bool(re.fullmatch(r"[a-zA-Z0-9]*",x))

def UpperFirst():
    return lambda x: bool(re.fullmatch(r"[A-Z]",x[0]))

def StartsWith(prefix):
    return (lambda x: x.startswith(prefix))

def EndsWith(suffix):
    return (lambda x: x.endswith(suffix))

def Contains(span):
    return lambda x: bool(re.search(span,x))

def WithLength(length):
    return (lambda x: len(x) == length)

