import requests
from plotly import offline
from plotly.graph_objs import bar


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers = headers)
print(f"status code:{r.status_code}")

#将相应赋值为一个变量
response_dict = r.json()

print(response_dict.keys())
print(f"Total repos:{response_dict['total_count']}")

#仓库的先关信息
repo_dicts = response_dict['items']
print(f"Repos return info:{len(repo_dicts)}")  #获得了多少个仓库的信息

print("\nSelected information about each repo:")
repo_names, starts = [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    starts.append(repo_dict['stargazers_count'])
    #print(f"\nName:{repo_dict['name']}")
    #print(f"\nOwner:{repo_dict['owner']['login']}")

#可视化
data = [{
    'type': 'bar',
    'x': 'repo_names',
    'y':  'starts'
}]
#布局规范的字典，指定图表名称和坐标轴标签
my_layout = {
    'title': 'Github上最受欢迎的python项目',
    'xaxis': {'title': 'Repos'},
    'yaxis': {'title': 'stars'},
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')