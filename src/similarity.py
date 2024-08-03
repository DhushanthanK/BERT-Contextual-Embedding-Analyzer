import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(embedding1, embedding2):
    return cosine_similarity([embedding1], [embedding2])[0][0]
