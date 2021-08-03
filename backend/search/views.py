from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


url = "https://search.musinsa.com/search/musinsa/goods?q=카고바지"
res = requests.get(url)
res.raise_for_status

soup = BeautifulSoup(res.text, "lxml")
title = soup.find_all("a", attrs={"name": "goods_link"})
print(title[0]["href"])


def size_search(request):
    if request.method == "GET":
        return
    elif request.method == "POST":
        return

