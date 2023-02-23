from github import Github
import pandas as pd

project_list=['Eyaeljery/projet2','Eyaeljery/projet ']
token="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"
def project_info():
    df_projects=pd.DataFrame()
    for projects in project_list:
        g=Github(token)
        repo=g.get_repo(projects)
        df_projects=df_projects.append({'project_id':repo.id,
                                        'name':repo.full_name })
        print(df_projects)                 







