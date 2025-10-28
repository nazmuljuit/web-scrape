import requests
import selectorlib

URL = ""

def scrape(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    data = extractor.extract(source)
    
    # Check if "question" exists and handle the data
    if "question" in data and data["question"]:
        return data["question"]
    else:
        return []

def store(extracted):
    with open("data.txt", "w", encoding="utf-8") as file:  # Added encoding="utf-8"
        if isinstance(extracted, list):
            for item in extracted:
                file.write(item + "\n")
        else:
            file.write(str(extracted))

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print("Extracted tags:", len(extracted))
    store(extracted)