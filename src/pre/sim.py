"""
    This is to calculate and write a similarity file for the given data.
    It considers each item as a set of its features and calculate their jaccard similarity.

    Input file format(.csv):
    item_id, feature_id1, feature_id2, feature_id3. . . .

    Output file format(.data - binary file: nested dictionary)
    {item_id1:{item_id2:sim_val12, item_id3: sim_val13, . . . }, item_id2:{. . .}, . . .}

    Similarity value can be accessed as: sim[item_id1][item_id2]
    Neighbours can be accessed as: sim[item_id].keys()

    Here sim is a nested dictionary name in which the generated similarity file is loaded with pickle.
"""

