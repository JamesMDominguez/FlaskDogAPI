from webbrowser import get
from flask import Flask , render_template
import requests
import json
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def hello_world():
    breeds_list = requests.get('https://dog.ceo/api/breeds/list/all')
    dog_IMG = requests.get('https://dog.ceo/api/breeds/image/random/50')
    breed_list_data = json.loads(breeds_list.text)
    img_links = json.loads(dog_IMG.text)
    return render_template("index.html",data=img_links,list=breed_list_data)

@app.route('/<breed>')
def hello_world2(breed):
    breeds_list = requests.get('https://dog.ceo/api/breeds/list/all')
    breed_list_data = json.loads(breeds_list.text)
    
    breed_pics = requests.get(f'https://dog.ceo/api/breed/{breed}/images')
    breeds = json.loads(breed_pics.text)
    return render_template("index.html",data=breeds,list=breed_list_data)

if __name__ == "__main__":
    app.run()
