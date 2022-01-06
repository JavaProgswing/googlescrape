# googlescrape

## Installation

Installation is simple!

```python
# Stable version

pip install googlescrape
```

## Examples

```python

from GoogleScrape import Client
scrapeClient=Client()
scrapeClient.imagesearch("Oracle","capture.png")
#saves the screenshot in capture.png
```

```python

from GoogleScrape import Client
scrapeClient=Client()
scrapeClient.googlescrape("Oracle")
#outputs a json
```
