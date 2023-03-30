from sklearn.cluster import AffinityPropagation


def get_clusters(encodings, random_state: int = 0):
    """
    Returns the cluster identity for the input encodings and the total number of clusters.

    Parameters
    ----------
    encodings : np.array
        Output from get_encodings function
    random_state : int, default: 0
        Seed for random number

    Returns
    -------
    clusters : np.array
        Cluster identity for each encoding
    n_clusters : int
        Number of identified clusters
    """
    clustering = AffinityPropagation(random_state=random_state).fit(encodings)
    clusters = clustering.labels_
    n_clusters = len(set(clusters))
    return (clusters, n_clusters)
