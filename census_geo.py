import requests
from bs4 import BeautifulSoup

CENSUS_URL = "https://www2.census.gov/geo/tiger/GENZ2018/shp/"

def main():
    shp_html = requests.get(CENSUS_URL).text
    bs = BeautifulSoup(shp_html)
    all_links = [link.get("href") for link in bs.body.table.find_all("a")]
    all_zip_links = [link for link in all_links if "zip" in link]

    for link in all_zip_links:
        r = requests.get(
            CENSUS_URL + link,
        )
        open(link, "wb").write(r.content)

if __name__ == "__main__":
    main()
