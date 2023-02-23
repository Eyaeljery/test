from github import Github
import pandas as pd

project_list=['Eyaeljery/projet2','Eyaeljery/projet ']
token="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"
def project_info():
    proects=pd.DataFrame()
    for projects in project_list:
        g=Github(token)







