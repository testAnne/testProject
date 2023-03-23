import requests

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

#研究下第一个仓库
repo_dict = repo_dicts[29]  #获取仓库列表中的第一个仓库的信息，返回是一个字典对象
# print(f"\nKeys:{len(repo_dict)}")   #第一个仓库字典对象中，打印包含多少个键.目前80个
   #打印这个字典中包含的所有键，看看其中对应的信息是什么
# for key in sorted(repo_dict.keys()):
#     print(key)
print("\nSelected information about first repo:")
print(f"Name:{repo_dict['name']}")
print(f"Owner:{repo_dict['owner']['login']}")
print(f"Stars:{repo_dict['stargazers_count']}")
print(f"Created:{repo_dict['created_at']}")


