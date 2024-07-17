import requests
from bs4 import BeautifulSoup


class AgentFinder:
    
    # def main(self, names):

    #     for name in names:
    #         result = self.search_agent(name)
    #         if result is not None:
    #             url = self.construct_url(result)
    #             self.get_agent_data(url)
    #             return self.state, self.phoneNumber
    
    def search_agent(self, name):

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'referer': 'https://www.remax.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }
        json_data = {
            'name': name,
            'country': 'USA',
            'cardType': 'autoComplete',
        }
        response = requests.post(
            'https://agents-offices-middleware.prod.udc-shared-prod.eng.remax.tech/v1/agent/search',
            headers=headers,
            json=json_data,
        )
        
        if response.status_code == 200:
            if response.json()['totalHits'] == 0:
                print(f"No agents matched this name {name} !")
                return None
            elif response.json()['totalHits'] > 1:
                print(f"Warning: more than one agent matched '{name}', most relevant agent was fetched")
            else:
                print(f'fetching {name}...')
            return response.json()['results'][0]
        else:
            print(f'Network Error {response.status_code}')
            return None

    def construct_url(self, result):
        
        masterCard = result['masterCustomerId']
        self.firstName = result['firstName']
        self.lastName = result['lastName']
        city = result['city']
        self.state = result['state']
        return f"https://www.remax.com/real-estate-agents/{self.firstName}-{self.lastName}-{city}-{self.state}/{masterCard}".lower()

    def get_agent_data(self, url):
        
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            self.phoneNumber = soup.select_one('div.d-information-container p').find_all(string=True)[-1]
            return self.phoneNumber


# print(search_agent('Jacob Taylor'))
# result = {'masterCustomerId': '102183855', 'firstName': 'Chance', 'lastName': 'Toon', 'city': 'Shelbyville', 'detailUrl': None, 'officeName': 'RE/MAX Celebration', 'state': 'TN', 'primaryOffice': {'masterCustomerId': '102292468', 'name': 'RE/MAX Celebration', 'address': {'city': 'Shelbyville', 'state': 'TN'}}}
# print(agent.construct_url(result))
url = 'https://www.remax.com/real-estate-agents/chance-toon-shelbyville-tn/102183855'
url = 'https://www.remax.com/real-estate-agents/tyler-secundy-colorado-springs-co/102228481'

agent = AgentFinder()
print(agent.get_agent_data(url))