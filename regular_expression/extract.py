import re


def extract():
    url = input("Twitter URL: ").strip()
    #  (?:...) non-capturing
    #  (...) capturing

    if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE):
        print(matches.group(1))

    # name = re.sub(r".*(https?://)?(www\.)?twitter\.com/", "", url)


extract()

