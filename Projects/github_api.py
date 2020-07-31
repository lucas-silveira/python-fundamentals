from urllib import request
import json


def read(url):
    with request.urlopen(url) as response:
        data = json.loads(response.read())
        print(data)


if __name__ == '__main__':
    read(r'https://api.github.com/users/lucas-silveira')  # The "r" prefix
    # prevents Python from handling special characters.
