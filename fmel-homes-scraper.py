import requests

url_15_may = "https://accommodation.fmel.ch/StarRezPortal/56e48bc61c4c34f8b425d3fe61ad580e8879b7c9037a4a5828b7ed6416c26bdeb84fb80e6efe782b7c0a21a2d2838cc2e055e2ada347919b29a526bde39ac056/71/929/Book_now-House_selection?UrlToken=89C4714B&TermID=1433&ClassificationID=1&DateStart=16%20May%202022&DateEnd=15%20May%202027"
url_1_june = "https://accommodation.fmel.ch/StarRezPortal/bec3eba564523df9ae23a9df8b7171880f4710ed8703b2d06c35af607ef60f768d17d7467028b9f7ce58e6fe652f0ed2186ff4c817ef6c825da7e448e3f15594/71/929/Book_now-House_selection?UrlToken=89C4714B&TermID=1433&ClassificationID=1&DateStart=01%20June%202022&DateEnd=31%20May%202027"

payload={}
headers = {
  'Cookie': '<Add your Cookie here>'
}

response_15_may = requests.request("GET", url_15_may, headers=headers, data=payload)
response_1_june = requests.request("GET", url_1_june, headers=headers, data=payload)

print("15th May Request:", response_15_may.status_code)
print("1st June Request:", response_1_june.status_code)