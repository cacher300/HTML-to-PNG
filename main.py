import requests

HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
HCTI_API_USER_ID = '5af2103a-065a-4c26-ab9e-53d995c87217'
HCTI_API_KEY = '603c48ed-4e59-45e4-a85c-05820041e8ef'

with open("map.html", "r") as f:
    html_code = f.read()

data = { 'html': html_code,
         'css': ".box { color: white; background-color: #0f79b9; padding: 10px; font-family: Roboto }",
         'google_fonts': "Roboto" }

image = requests.post(url=HCTI_API_ENDPOINT, data=data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))

image_url = image.json()['url']

# Download the image and save it as a binary file
response = requests.get(image_url)
with open("image.png", "wb") as f:
    f.write(response.content)

print("Image saved as image.png")
