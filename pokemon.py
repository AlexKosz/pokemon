import random
import requests
import json
from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def ma():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/")
    pokemonList=response.json()
    nextUrl = pokemonList['next']
    prevUrl = pokemonList['previous']
    print(nextUrl, prevUrl)
    pokemonList=pokemonList['results']
    print(pokemonList[0])
    def getInfo(pokemonURL):
        response = requests.get(pokemonURL)
        pokemonInfo=response.json()
        print(pokemonInfo)
        return(pokemonInfo)
    return render_template("index.html", pokemonList = pokemonList, len=len(pokemonList), getInfo=getInfo)


    

#@app.route('/result', methods=['POST'])
#def guess():
 #       return render_template("info.html", pokemonInfo)




if __name__=="__main__":    
    app.run(debug=True)    

