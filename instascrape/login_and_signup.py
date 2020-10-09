from __future__ import annotations

import insta_scraper
import jsontools

class LoginAndSignupPage(insta_scraper.StaticInstaScraper):
    """
    Representation of an Instagram profile page.

    Attribues
    ---------
    url : str
        Full URL to an existing Instagram profile

    Methods
    -------
    static_load(session=requests.Session())
        Makes request to URL, instantiates BeautifulSoup, finds JSON data,
        then parses JSON data.
    """

    def _scrape_json(self, json_data: dict):
        """Scrape JSON data and load into instances namespace"""
        self.data = LoginAndSignupJSON(json_data)
        self._load_json_into_namespace(self.data)


class LoginAndSignupJSON(jsontools.JSONScraper):
    def parse_json(self):
        super().parse_json()


if __name__ == "__main__":
    url = r"https://www.instagram.com/accounts/login"
    login = LoginAndSignupPage(url)
    login.static_load()
