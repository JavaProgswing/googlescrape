# googlescrape

## Installation

Installation is simple!

```python
# Stable version

pip install googlescrape
```

## Examples

```python

from googlescrape import client
scrapeClient=client()
scrapeClient.imagesearch("Oracle","capture.png")
#saves the screenshot in capture.png
```

```python

from googlescrape import client
scrapeClient=client()
scrapeClient.googlescrape("Oracle")
#outputs a json
```
