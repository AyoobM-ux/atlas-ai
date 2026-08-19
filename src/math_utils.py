import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    dot_product = np.dot(a, b)

    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    if norm_a == 0 or norm_b == 0:
        raise ValueError("Cosine similarity is undefined for zero vectors.")

    similarity = dot_product / (norm_a * norm_b)

    return float(similarity)






def normalize_vector(vector: np.ndarray) -> np.ndarray:
    norm = np.linalg.norm(vector)

    if norm == 0:
        raise ValueError("Cannot normalize a zero vector.")

    return vector / norm






def cosine_similarity_batch(
    query: np.ndarray,
    vectors: np.ndarray
) -> np.ndarray:

    query_norm = np.linalg.norm(query)

    if query_norm == 0:
        raise ValueError("Query cannot be a zero vector.")

    vector_norms = np.linalg.norm(
        vectors,
        axis=1,
        keepdims=True
    )

    if np.any(vector_norms == 0):
        raise ValueError("Vectors cannot contain zero vectors.")

    normalized_query = query / query_norm
    normalized_vectors = vectors / vector_norms

    return normalized_vectors @ normalized_query