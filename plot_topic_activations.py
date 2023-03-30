import seaborn as sns
import matplotlib.pyplot as plt


def plot_topic_activations(
    name_activations: np.array, name_groups: list[str], names: list[str]
) -> sns.heatmap:
    """
    Visualize mapping of name-groups to names

    Parameters
    - - - - -
    name_activations : array
    Array of name activations from get_name_groups


    name_groups : list of strings
    List of name-groups from get_name_groups

    names : list of strings
    Number of wanted name-group parts, 2 as default as people typically have a first and a last name
    Returns
    - - - -
    out : sns.heatmap
    Heatmap showing the activations for each name, name group pair

    """


data = pd.DataFrame(name_activations, columns=name_groups, index=names)
sns.heatmap(data)
plt.title("Activations for each name / name-group pair")
plt.xlabel("Name-groups")
plt.ylabel("Extracted names")
plt.show()
