from github import Github
import pandas as pd

project_list=['apache/any23','apache/dubbo']
token="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"
def project_info():
    df_projects=pd.DataFrame()
    for projects in project_list:
        g=Github(token)
        repo=g.get_repo(projects)
        df_projects=df_projects.append({'project_id':repo.id,
                                        'name':repo.full_name })
    df=df_projects.to_csv('projects.csv', sep =',')
    newdf=pd.read_csv('projects.csv')
    print(newdf)
                    







