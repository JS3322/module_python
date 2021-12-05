import requests
from bs4 import BeautifulSoup
import torch
import cv2

x = torch.rand(5, 3)
print(x)


indeed_resul = requests.get("https://www.indeed.com/jobs?as_and=python&limit=50")
indeed_soup = BeautifulSoup(indeed_resul.text, "html.parser")


pagination = indeed_soup.find("div", {"class":"pagination"})

pages = pagination('a')
spans = []

for page in pages:
    spans.append(page.find("span"))

print(spans)