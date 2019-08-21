import argparse
import os
import requests
from dotenv import load_dotenv


def shorten_link(token, url):
    bitly_url = "https://api-ssl.bitly.com/v4/bitlinks"
    headers = {"Authorization": "Bearer {}".format(token)}
    payload = {"long_url": url}
    response = requests.post(bitly_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["link"]


def count_clicks(token, url):
    bitly_url = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary".format(url)
    headers = {"Authorization": "Bearer {}".format(token)}
    payload = {"unit": "day", "units": -1}
    response = requests.get(bitly_url, headers=headers, params=payload)
    response.raise_for_status()
    return response.json()["total_clicks"]


def link(parsed_arg):
    message = "{} is not valid URL".format(parsed_arg)
    if not (parsed_arg.startswith("http") or parsed_arg.startswith("bit")):
        raise argparse.ArgumentTypeError(message)
    return parsed_arg


def get_link():
    parser = argparse.ArgumentParser(
        description="Shorten URL with Bitly or get click counts for a specified Bitlink."
    )
    parser.add_argument(
        "URL", type=link, help="URL to shorten or to get click counts for"
    )
    return parser.parse_args()


if __name__ == "__main__":
    link = get_link()
    load_dotenv()
    token = os.getenv("BITLY_TOKEN")
    functions = [count_clicks, shorten_link]
    requested_function = functions[link.URL.startswith("http")]
    try:
        requested_answer = requested_function(token, link.URL)
    except requests.exceptions.HTTPError:
        exit("URL is incorrect")
    print(requested_answer)
