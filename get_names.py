import spacy


def get_names(text: str) -> list[str]:
    """
    Returns a unique, sorted list of named entities from a string of text.

    Parameters
    ----------
    text : str
        The input text to extract names from

    Returns
    -------
    out : list[str]
        Sorted list of unique names extracted from text
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    names.sort()
    return list(set(names))
