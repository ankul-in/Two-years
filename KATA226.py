#kata
#https://www.codewars.com/kata/643869cb0e7a563b722d50ad/train/python

#scrapper good wikipedia scrapper
import requests

headers = {
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "AnkulBot/1.0 (https://w.wiki/4wJS)"
}

def wikidata_scraper(url):
    entity_id = url.rstrip('/').split('/')[-1].replace('.json', '')


    api_url = f"https://www.wikidata.org/wiki/Special:EntityData/{entity_id}.json"

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        entity_data = data['entities'][entity_id]
        label = entity_data['labels'].get('en', {}).get('value')
        description = entity_data['descriptions'].get('en', {}).get('value')

        return {
            "ID": entity_id,
            "LABEL": label if label is not None else "No Label",
            "DESCRIPTION": description if description is not None else "No Description",
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            "ID": "NO ID",
            "LABEL": "No Label",
            "DESCRIPTION": "NO Description",
        }
    

print(wikidata_scraper(f"https://www.wikidata.org/wiki/Special:EntityData/Q42.json"))