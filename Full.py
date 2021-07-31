import bs4
import re
import requests
import wikipedia

URL_radix = "https://en.wikipedia.org"

def input_loop():
    exiting = ""
    while exiting != "y":
        from_string = input("Starting article : ")
        to_string = input("Ending article : ")
        depth = int(input("Depth (1-6): "))
        from_URL = URL_radix + "/wiki/" + wikipedia.search(from_string)[0].replace(" ", "_")
        to_URL = URL_radix + "/wiki/" + wikipedia.search(to_string)[0].replace(" ", "_")
        print("[URL] From: {}\n[URL] To: {}".format(from_URL, to_URL))
        search(from_URL, to_URL, depth, wikipedia.search(from_string)[0].replace(" ", "_"))
        exiting = input("Exit ? (y/n) : ")
def search(input_URL, output_URL, depth, path):
    if input_URL == output_URL:
        print(path)
    if depth == 0:
        return None
    response = requests.get(input_URL)
    content = response.content
    pattern = re.compile("/wiki/[\w\-:]+")
    links = pattern.findall(content.__str__())
    unique_links = []
    for link in links:
        if ":" not in link and "Main_Page" not in link and link not in unique_links:
            unique_links.append(link)
            current_URL = URL_radix + link
            search(current_URL, output_URL, depth-1, path+"->{}".format(link[6:]))

input_loop()