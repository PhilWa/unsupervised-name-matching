# Unsupervised Name-Matching — Introducing John to Dr. Watson

This repository showcases an unsupervised workflow to determine the underlying name-groups of different name variants. The goal is to explain to the computer that both ‘John’ and ‘Dr. Watson’ both refer to the name-group ‘Dr. John H. Watson’. More info you can find in this  [blogpost](https://medium.com/d-one/unsupervised-name-matching-made-easy-introducing-john-to-dr-watson-d543cbdc26e5)

The workflow consists of 4 steps:

1. Extracting the names from the text
2. Based on the name similarities, determine the number of name clusters
3. Using the number of clusters to determine meaningful name-groups
4. Assign each name to a name-group

## Requirements

Make sure you have the following libraries and the respective spaCy language model installed:
```bash
dirty-cat==0.2.0
en-core-web-sm==3.2.0
matplotlib==3.5.1
numpy==1.22.3
pandas==1.4.2
scikit-learn==1.0.2
seaborn==0.11.2
spacy==3.2.4
```

After installing spaCy, the language model can be downloaded like this:

```bash
python -m spacy download en_core_web_sm
```

# Description


1. Use `get_names.py` to extract names from a given text.
2. Determine the similarity of names using `get_encodings.py` and `get_clusters.py`.
3. Determine the name-groups using `get_name_groups.py`.
4. Map each name to a name-group using `plot_topic_activations.py` and `get_clean_names.py`.

**tl;dr**:

run:
> python tutorial.py


## Limitations and improvements
This workflow runs smoothly for the provided test cases but may require adjustments for real-world natural language processing tasks. Some possible improvements include:

1. Improving unsupervised
determination of name clusters by using consensus of multiple orthogonal approaches, such as word2vec or the transformed based universal sentence encoder.
2. Generating name-groups using more advanced techniques like convolutional variational autoencoders or generative adversarial networks.
Contact
If you have any questions or input, please feel free to get in touch.

# Example 1: Disambiguating Names in Biomedical Publications and Clinical Trials

A life science knowledge graph may include information on research publications, authors, clinical trials, and investigators. This repo helps disambiguate names in datasets of biomedical publications and clinical trials. For instance, consider these author and investigator lists:

- Dr. John H. Watson, J. Watson, Watson, J., Prof. John Watson, John Watson, MD
- Dr. Sherlock Holmes, PhD, S. Holmes, Prof. S. Holmes, Sherlock H. Holmes, PhD, Dr. S. H. Holmes

Using this workflow, we can map different name variants to a single name-group for each person ('watson, john' and 'sherlock, holmes'), simplifying the process of creating a knowledge graph that accurately represents relationships between publications, authors, clinical trials, and investigators.

# Example 2: Mapping Gene Symbols to Gene Names

In a life science knowledge graph, it is essential to accurately represent the relationships between genes, their functions, and associated diseases. Gene symbols, which are used as shorthand for gene names, can be ambiguous. This repo can help disambiguate gene symbols and map them to their respective gene names. Consider the following list of gene symbols and names in a dataset:

- TP53
- Tumor Protein p53
- p53
- TP53 (Tumor Protein p53)
- p53 tumor suppressor

By using this workflow, we can map these different name variants to a single name-group 'tp53, tumor protein p53', thus enabling accurate representation of gene relationships in the knowledge graph.


## Contact
philipp.warmer@gmail.com
https://www.linkedin.com/in/philippwarmer/

