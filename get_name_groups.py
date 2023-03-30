from dirty_cat import GapEncoder
import numpy as np


def get_name_groups(
    names: list[str], n_labels: int, n_name_parts: int = 2, random_state: int = 0
) -> ([str], np.array):
    """
    Returns the name-groups and activations.

    Parameters
    ----------
    names : list[str]
        A list of names to generate name-groups for
    n_labels : int
        Number of wanted name-groups, output of get_clusters can be used
    n_name_parts : int, default: 2
        Number of wanted name-group parts, 2 as default as people typically have a first and a last name
    random_state : int, default: 0
        Seed for random numbers

    Returns
    -------
    name_groups : list[str]
        name-groups consisting of n_name_parts
    name_activations : np.array
        Activations for each name
    """
    enc = GapEncoder(n_components=n_labels, random_state=42)
    name_activations = enc.fit_transform(np.array(names).reshape(-1, 1))
    name_groups = enc.get_feature_names_out(n_labels=n_name_parts)
    return (name_groups, name_activations)
