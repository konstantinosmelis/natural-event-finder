import spacy
from spacy.lang.en import English
import os
import sys
import nltk
import json
import tweetsearch

def read_file(filename):
    file = open(filename, 'r')
    data = json.load(file)
    return data


def push_event(event, data):
    nlp = spacy.load("en_core_web_md")
    locations = []
    for e in data:
        e['text'] = e['text'].replace('#', '')
        doc = nlp(e['text'])
        for ent in doc.ents:
            if ent.label_ == "GPE":
                locations.append(ent.text)
    return locations


def get_full_data(events):
    tweetsearch.get_data(events)
    data = {}
    for e in events:
        event = e[1:len(e)]
        json_data = read_file(f'{event}.json')
        locations = push_event(event, json_data['data'])
        data[event] = locations
    return data


def main():
    events = ['#earthquake', '#forestfire', '#storm']
    get_full_data()


if __name__ == "__main__":
    main()
