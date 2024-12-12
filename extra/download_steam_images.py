import requests

BASE_URL = "https://steamcdn-a.akamaihd.net/steam/apps/"
FNAME = "/header.jpg"
APP_ID = 440
OUTPUT_FILE = "team_fortress.jpg"

"""
Send a request to the Steam API to download an image 
for a game based on its app ID
"""
def retrieve_image(id):
    request_url = f"{BASE_URL}{id}{FNAME}"
    response = requests.get(request_url)

    if response.status_code == 200:
        return response.content

    return None

"""
Store an image to memory from the API data

@param  image_data
@param  fname       Filename to store the new file
"""
def save_img(image_data, fname):
    # Write the byte data to a file
    with open(fname, "wb") as file:
        file.write(image_data)

if __name__ == "__main__":
    img = retrieve_image(APP_ID)
    save_img(img, OUTPUT_FILE)