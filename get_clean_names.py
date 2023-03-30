import pandas as pd


def get_clean_names(
    name_activations: np.array, name_groups: list[str], names: list[str]
) -> pd.DataFrame:
    """
    Returns mapping of name-groups to names

    Parameters
    ----------
    name_activations : array
                    Array of name activations from get_name_groups


    name_groups : list of strings
               List of name-groups from get_name_groups

    names : list of strings
                Number of wanted name-group parts, 2 as default as people typically have a first and a last name

    Returns
    --------
    out : pd.DataFrame
       Dataframe contains mapping of name-groups to names

    """
    return (
        pd.DataFrame(name_activations, columns=name_groups, index=names)
        .idxmax(axis=1)
        .reset_index()
        .rename({"index": "extracted_names", 0: "name_group"}, axis=1)
    )
