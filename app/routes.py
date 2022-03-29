from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', title = 'Home')

@app.route('/top5')
def top5():
    topdigis = [
        {
            'id':1,
            'img': "https://digimon.shadowsmith.com/img/agumon.jpg",
            'name': "Agumon",
            'tamer': "Tai",
            'text': 'Agumon is the original digipal, and Wargreymon is awesome.'
        },
        {
            'id':2,
            'img': "https://digimon.shadowsmith.com/img/gabumon.jpg",
            'name': "Gabumon",
            'tamer': "Matt", 
            'text': "He'll give you his fur coat if you're cold."
        },
        {
            'id':3,
            'img': "https://digimon.shadowsmith.com/img/biyomon.jpg",
            'name': "Biyomon",
            'tamer': "Sora",
            'text': "The VA behind Sora is still doing voice acting! Including Tales in the new Sonic movies."
        },
        {
            'id':4,
            'img': "https://digimon.shadowsmith.com/img/tentomon.jpg",
            'name': "Tentomon",
            'tamer': "Izzy",
            'text': 'I never liked bugs but Tentomon always amused me.'
        },
        {
            'id':5,
            'img': "https://digimon.shadowsmith.com/img/palmon.jpg",
            'name': "Palmon",
            'tamer': "Mimi",
            'text': 'In the game "Digimon World" Palmon ran the farm that gave you tons of meat for your digipals.'
        }
        # {
        #     'id':6,
        #     'img': "https://digimon.shadowsmith.com/img/gomamon.jpg",
        #     'name': "Gomamon",
        #     'tamer': "Joe"
        # },
        # {
        #     'id':7,
        #     'img': "https://digimon.shadowsmith.com/img/patamon.jpg",
        #     'name': "Patamon",
        #     'tamer': "T.K."
        # },
        # {
        #     'id':8,
        #     'img': "https://digimon.shadowsmith.com/img/gatomon.jpg",
        #     'name': "Gatomon",
        #     'tamer': "Kari"
        # }
    ]
    return render_template('top5.html', digis = topdigis)