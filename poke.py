import requests
import fastapi
from fastapi.responses import FileResponse, RedirectResponse

url = "https://pokeapi.co/api/v2/pokemon/"
app = fastapi.FastAPI()

@app.get("/")
def root():
    return RedirectResponse("http://127.0.0.1:8000/25")

@app.get("/{num}")
def poke(num: str):
    img = requests.get(url + num).json()["sprites"]["front_default"]
    img2 = requests.get(img).content

    name = requests.get(url + num).json()["name"]

    with open("img.jpg", "wb") as f:
        f.write(img2)
    return FileResponse("img.jpg")