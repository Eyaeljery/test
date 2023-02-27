from github import Github
import pandas as pd
import numpy as np

token="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"
g=Github(token)
current_user=g.get_user()
print(current_user.name)

                    







