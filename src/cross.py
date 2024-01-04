import re
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from tensorflow_text import SentencepieceTokenizer
import sklearn.metrics.pairwise
# from PIL import Image


module_url = 'https://tfhub.dev/google/universal-sentence-encoder-multilingual/3'
print("Loading multilingual model...")
model = hub.load(module_url)


def embed_text(inp):
    return model(inp)


def get_sim(embeddings_1):
    # sim = [[0 for _ in range(len(labels_1))] for _ in range(len(labels_1))]
    # embeddings_1 = embed_text(labels_1)
    sim = 1 - np.arccos(
        sklearn.metrics.pairwise.cosine_similarity(embeddings_1,
                                                   embeddings_1)) / np.pi
    return sim
