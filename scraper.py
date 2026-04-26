import requests
from bs4 import BeautifulSoup

def buscar_google(dork):
    url = f"https://www.google.com/search?q={dork}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    return response.text

def extraer_enlaces(html):
    soup = BeautifulSoup(html, "html.parser")
    enlaces = []

    for link in soup.find_all("a"):
        href = link.get("href")
        if href and "url?q=" in href:
            enlace = href.split("url?q=")[1].split("&")[0]
            enlaces.append(enlace)

    return enlaces
