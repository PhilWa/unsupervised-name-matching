import numpy as np
from dirty_cat import SimilarityEncoder


def get_encodings(names: list[str]) -> np.array:
    """
    Returns n-gram similarities from list of names.

    Parameters
    ----------
    names : list[str]
        A list of names to compute n-gram similarities for

    Returns
    -------
    transformed_values : np.array
        An array of n-gram similarities
    """
    sorted_values = np.unique(np.array(names))
    similarity_encoder = SimilarityEncoder(similarity="ngram")
    transformed_values = similarity_encoder.fit_transform(sorted_values.reshape(-1, 1))
    return transformed_values
