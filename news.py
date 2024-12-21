import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=YOUR API KEY')
json_data = requests.get(url).json()

ar=[]

def news():
    for i in range(5):
        ar.append("Number " + str(i+1)+ ", "+ json_data["articles"][i]["title"]+".")

    return ar
arr=news()
# print(arr)



