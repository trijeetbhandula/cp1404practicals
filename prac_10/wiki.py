"""
CP1404 - Practical 10
Wikipedia Python API
"""

import wikipedia
from wikipedia import DisambiguationError, PageError

query = input("Enter page title or query phrase in quotation marks: ")
while query != "":
    try:
        search = wikipedia.page(query)
        print(f"Title: {search.title}")
        print(f"URL: {search.url}")
        print(f"Summary: {wikipedia.summary(str(query))}")
    except DisambiguationError as e:
        print("Disambiguation page")
        print(e.options)
    except PageError:
        print("The page doesnt exist")
    query = input("Enter page title or query phrase: ")
