![vagabond](https://raw.githubusercontent.com/cburmeister/vagabond/master/image.jpg)

vagabond
===========

Search https://www.airbnb.com/ without leaving the prompt.

---

## Install

```bash
$ python setup.py install
```

## Usage

Want to get away?

```bash
$ vagabond --query vanuatu 
[
    {
        "instant": true,
        "lat": "-17.77155394774955",
        "lng": "168.31360175045555",
        "name": "The Makordel Lodge ",
        "price": 69.0,
        "summary": "\n  Entire home/apt \u00b7 3 reviews \u00b7 Port-Vila\n\n",
        "url": "/rooms/3410639?s=pdDG"
    },
    {
        "instant": false,
        "lat": "-17.75696070408711",
        "lng": "168.28999982598978",
        "name": "Waterfront, 7 mins from town",
        "price": 80.0,
        "summary": "\n  Private room \u00b7 4 reviews \u00b7 Port Vila\n\n",
        "url": "/rooms/1508188?s=pdDG"
    }
]
```

Check out the help for all available arguments:

```bash
$ vagabond --help
```
