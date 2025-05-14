# nlp_utils.py
from rapidfuzz import fuzz

def find_best_path_match(user_input, tree, threshold=70):
    """
    Recursively search all levels of the tree and return the best partial path match.
    Matches to any intermediate or leaf node path.
    """
    best_match = None
    best_score = 0

    def recurse(subtree, path=[]):
        nonlocal best_match, best_score
        if isinstance(subtree, dict):
            for key, value in subtree.items():
                full_path = " ".join(path + [key]).lower()
                score = fuzz.partial_ratio(user_input.lower(), full_path)
                if score > best_score and score >= threshold:
                    best_match = path + [key]
                    best_score = score
                recurse(value, path + [key])

    recurse(tree)
    return best_match
