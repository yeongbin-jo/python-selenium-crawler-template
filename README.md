# Selenium Crawler Template
Boilerplate for developing crawler with Selenium.

## Installation

```bash
pip install selenium-crawler-template
```

## Usage
```python
from selenium_crawler_template import Crawler

class MyCrawler(Crawler):
    @Crawler.open_url_in_new_tab
    def _get_email_from_profile(self, _):
        return self.find_element('a#email').get_attribute('href')

    def crawl(self, **kwargs):
        self.driver.get(kwargs['url'])
        
        for profile in self.find_elements('ul > .profile'):
            _ = self._get_email_from_profile(profile.get_attribute('href'))
           
        self._scroll_to_bottom()
```
