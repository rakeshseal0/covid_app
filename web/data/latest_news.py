import requests
from bs4 import BeautifulSoup 


class news:
    def __init__(self):
        dat = requests.get('https://www.thehindu.com/topic/coronavirus/')
        self.soup = BeautifulSoup(dat.content, 'html5lib') 
        self.data = {}

    def heading(self):
        paragraphs = self.soup.find_all('p')
        # print()
        self.data['heading'] = paragraphs[1].get_text()

    def top_news(self):
        links = self.soup.find_all(class_='story-card')
        links = links[0:10]
        for elem in links:
            anchors = elem.find("h3").find('a')
            self.data[str(anchors.contents[0]).strip()] = anchors["href"]
            # self.data[anchors["href"]] = str(anchors.contents[0]).strip()

    def get_data(self):
            self.heading()
            self.top_news()
            return self.data



if __name__ == "__main__":
    n = news()
    jsn = n.get_json()
    print(jsn)
