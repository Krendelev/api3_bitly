# Bitly Helper

Helps you shorten links with [Bitly](https://bitly.com) or get click counts for a specified Bitlink.

## How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

## Usage

Register with [Bitly](https://bitly.com) and follow the instructions to get a `GENERIC ACCESS TOKEN`. Place it in the `.env` file in the same directory with `helper.py` like this:
```
BITLY_TOKEN='b123456d78b9e0befe123456bb00789a123cca45'
```
Then run `helper.py` with an URL as an argument:
```bash
$ python helper.py https://dvmn.org
http://bit.ly/31NxaHn

$ python helper.py bit.ly/31HvSha
3
```



## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org)
