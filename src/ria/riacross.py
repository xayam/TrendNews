import re
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from tensorflow_text import SentencepieceTokenizer
import sklearn.metrics.pairwise
# from transformers import pipeline, set_seed
import pprint

# tokenizer = T5Tokenizer.from_pretrained("t5-base")
# generator = pipeline(task='text-generation',
#                      # tokenizer=tokenizer,
#                      model='ai-forever/rugpt3medium_based_on_gpt2')
# deepset/deberta-v3-large-squad2')
# set_seed(42)
pp = pprint.PrettyPrinter(width=80, compact=True)

module_url = 'https://tfhub.dev/google/universal-sentence-encoder-multilingual/3'
print("Loading multilingual model...")
model = hub.load(module_url)


# generator = pipeline(model='deepset/deberta-v3-large-squad2')
# set_seed(42)
# print(generator(
#     [{"question": "Какое слово из списка " + \
#     "наиболее трендовое и популярное для общества?", "context": "биометалл, спецоперация, конфликт, бифидобактерии"}],
#     max_new_tokens=100, num_beams=30))

def embed_text(inp):
    return model(inp)


def get_sim(embeddings_1, embeddings_2=None):
    # sim = [[0 for _ in range(len(labels_1))] for _ in range(len(labels_1))]
    # embeddings_1 = embed_text(labels_1)
    sim = 1 - np.arccos(
        sklearn.metrics.pairwise.cosine_similarity(embeddings_1,
                                                   embeddings_2)) / np.pi
    return sim


def split_text(text):
    result = re.findall(r"\b[\-цукенгшщзхъфывапролджэячсмитьбю]+\b", text)
    return result


# def get_keyword_1(question, data):
#     context = str(data)
#     prompt = [{"question": "отсортируй список ключевых слов по релевантности. список: " + str(data),
#                "context": '"' + context + '"'}]
#     generate = generator(prompt, max_length=len(str(data)), num_return_sequences=1)
#     print(generate)
#     result = split_text(generate["answer"])
#     if result[question] in data:
#         return result[question]
#     else:
#         raise "ERROR. GPT model not found keyword"


# def get_keyword(question, data):
#     words = ""
#     for word in data:
#         words += f"'{word}', "
#     prompt = "Какое слово из списка " + words[:-2] + \
#              [" меньше", " больше"][question + 1] + \
#              " всего актуально для новостного тренда?"
#     generate = generator(prompt, max_length=len(prompt) + 50, num_return_sequences=1)
#     pp.pprint(generate)
#     result = split_text(generate["generated_text"])
#     if result[-1] in data:
#         return result[-1]
#     else:
#         raise "ERROR. GPT model not found keyword"
