# Author: Marco Ma
# Date: Feb 24, 2021
# Project: toy python package

import pandas as pd

def catbind(a, b):
    concatenated = pd.concat([pd.Series(a.astype("str")),
                              pd.Series(b.astype("str"))])
    return pd.Categorical(concatenated)

# print("Sup Im a toy")