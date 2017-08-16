"""
    This is to split the given data in 3 - way (training - validation - test) form.
    User just need to provide ratio (e.g. .6, .2, .2). Given example values are default split.
    This is to be noted that the generated splits are non-overlapped and cover the whole data as follows:

    tr | tr | tr | vl | ts
    tr | tr | vl | ts | tr
    tr | vl | ts | tr | tr
    vl | ts | tr | tr | tr
    ts | tr | tr | tr | vl

    here tr: training, vl: validation, ts: test

    Coded by: Arpit Rana
    Date: August 16th, 2017
"""

