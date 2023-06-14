#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0 or not isinstance(a_dictionary, dict):
        return None

    best = list(a_dictionary.keys())[0]
    for student in a_dictionary:
        if a_dictionary[student] > a_dictionary[best]:
            best = student

    return best
