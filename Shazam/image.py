from PIL import Image
import requests
from io import BytesIO

response = requests.get('https://is2-ssl.mzstatic.com/image/thumb/Music124/v4/16/d1/73/16d17379-1386-7faf-a3f3-abab20b9dbbd/195497602445.jpg/400x400cc.jpg')
img = Image.open(BytesIO(response.content))
img.resize((128,128)).show()