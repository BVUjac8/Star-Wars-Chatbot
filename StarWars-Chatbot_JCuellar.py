# Julia Cuellar
# DSC 680
# Star Wars Chatbot

import numpy as np
import pandas as pd
import requests
import json
import sqlite3
import openpyxl
import functools
from functools import reduce
import urllib.request as urllib2
from pprint import pprint
from pip._vendor.distlib.compat import raw_input
import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


# Read Star Wars character data
def read_file():
    char = pd.read_csv('characters.csv')
    print('Character data:\n', char)


# Read Star Wars planet data
def read_file2():
    plan = pd.read_csv('planets.csv')
    print('Planet data:\n', plan)


# Read Star Wars species data
def read_file3():
    spec = pd.read_csv('species.csv')
    print('Species data:\n', spec)


# Read Star Wars starship data
def read_file4():
    ship = pd.read_csv('starships.csv')
    print('Starship data:\n', ship)


# Read Star Wars vehicle data
def read_file5():
    veh = pd.read_csv('vehicles.csv')
    print('Vehicle data:\n', veh)


# Read Star Wars database data
def read_db():
    conn = sqlite3.connect("Star Wars")
    cur = conn.cursor()
    cur.execute("SELECT * FROM character")
    table = cur.fetchall()

    for i in table:
        print(i)

    cur.execute("SELECT * FROM planets")
    table2 = cur.fetchall()

    for i in table2:
        print(i)

    cur.execute("SELECT * FROM species")
    table3 = cur.fetchall()

    for i in table3:
        print(i)

    cur.execute("SELECT * FROM starships")
    table4 = cur.fetchall()

    for i in table4:
        print(i)

    cur.execute("SELECT * FROM vehicles")
    table5 = cur.fetchall()

    for i in table5:
        print(i)


# Merge Star Wars database data
def db_merge():
    conn = sqlite3.connect("Star Wars")
    cur = conn.cursor()
    cur.execute("SELECT * FROM character")
    table = cur.fetchall()
    char = pd.read_csv('characters.csv')
    print(char)
    cur.execute("SELECT * FROM planets")
    table2 = cur.fetchall()
    plan = pd.read_csv('planets.csv')
    print(plan)
    cur.execute("SELECT * FROM species")
    table3 = cur.fetchall()
    spec = pd.read_csv('species.csv')
    print(spec)
    cur.execute("SELECT * FROM starships")
    table4 = cur.fetchall()
    ship = pd.read_csv('starships.csv')
    print(ship)
    cur.execute("SELECT * FROM vehicles")
    table5 = cur.fetchall()
    veh = pd.read_csv('vehicles.csv')
    print(veh)
    db = [char, plan, spec, ship, veh]
    db_final = reduce(lambda left, right: pd.merge(left, right, on=['name'], how='outer'), db).fillna('NA')
    print("Database shape:\n", db_final.shape)
    print("Database data:\n", db_final)
    db_final.to_excel('Star Wars Data.xlsx')

    with open("Star Wars Data.json", "r") as f:
        data = json.load(f)


# Create Star Wars chatbot
def chatbot():
    api = 'https://swapi.py4e.com/api/'
    data = json.load(urllib2.urlopen(api))
    print(data)
    print("--Star Wars Chatbot--")
    character = input("What character from Star Wars do you want to know about?\n")
    char = data['people']
    print("Data about " + str(character) + ": ", char)
    planet = input("What planet from Star Wars do you want to know about?\n")
    plan = data['planets']
    print("Data about " + str(planet) + ": ", plan)
    species = input("What species from Star Wars do you want to know about?\n")
    spec = data['species']
    print("Data about " + str(species) + ": ", spec)
    starship = input("What starship from Star Wars do you want to know about?\n")
    ship = data['starships']
    print("Data about " + str(starship) + ": ", ship)
    vehicle = input("What vehicle from Star Wars do you want to know about?\n")
    veh = data['vehicles']
    print("Data about " + str(vehicle) + ": ", veh)


if __name__ == "__main__":
    read_file()
    read_file2()
    read_file3()
    read_file4()
    read_file5()
    read_db()
    db_merge()
    chatbot()