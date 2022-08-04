import requests

url = "http://127.0.0.1:5000/"

data = [{"name": "rohan", "views": 30, "likes": 1000},
        {"name": "rajesh", "views": 50, "likes": 2000},
        {"name": "rishabh", "views": 300, "likes": 3000}]

for i in range(len(data)):    
    response = requests.put(url + "video/" + str(i), data[i])
    print(response.json())

input()

response = requests.get(url + "video/2")
print(response.json())