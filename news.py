import requests

api_key = "pub_45042470cf3f6ec7c593e1c968b34bdbccf9d"
base_url = "https://newsdata.io/api/1/news"

def get_news():
    params = {
        "apikey": api_key,
        "country": "hr",
        "category": "technology",
        "language": "hr",
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        news=""
        for article in data["results"]:
            news+=f"Naslov: {article["title"]}\n"
            news+=f"Opis: {article["description"]}\n"
            news+=f"Link: {article["link"]}\n"
            news+="\n"
        return news 
    else:
        return f"Neuspješno dohvaćanje vijesti. Statusni kod: {response.status_code}"
