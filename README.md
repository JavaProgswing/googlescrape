# googlescrape

What is `googlescrape?`

`googlescrape` is a simple Python Package that can google anything and get it's results by scraping. 

## Installation

Installation is simple!

```
pip install googlescrape
```

## Examples

```python
from googlescrape import Client

scrape_client = Client()
scrape_client.image_search("Oracle", "capture.png")

# Searches, and saves the screenshot as `capture.png`.
```

```python
from googlescrape import Client

scrapeClient = Client()
scrapeClient.json_search("Oracle")

# Searches, and outputs the result as JSON
```
