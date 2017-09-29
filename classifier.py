import requests

data = {
	"images_file": open("testbild2.jpg", "rb"),
	"classifier_ids": ["puddlesweeper_1847970994", "default"]
}

def parse_request(r, *args, **kwargs):
	json = r.json()
	print(json)

hooks = {
	"response": parse_request
}

r = requests.post("https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify?api_key=b398984f4477e89ce8a52a91c831fac5b407cebe&version=2016-05-20", data=data, hooks=hooks)

print(r.request.url)

