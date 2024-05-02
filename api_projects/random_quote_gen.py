import requests

def get_random_quote(category=None, author=None):
    params = {"method": "getQuote", "format": "json", "lang": "en"}
    if category:
        params["category"] = category
    if author:
        params["filter"] = f"from:{author}"
    response = requests.get("https://api.forismatic.com/api/1.0/", params=params)
    quote_data = response.json()
    quote = quote_data["quoteText"]
    author = quote_data["quoteAuthor"]
    return quote, author

def display_quote(quote, author, category=None, show_filter_options=True):
    print("\n" + "-" * 80)
    print(" " * 38 + "Quote of the Day")
    print("-" * 80)
    if category or show_filter_options:
        print("Filter options:")
        print(f"- Category: {category or 'Random'}")
        print(f"- Author: {author or 'Random'}")
        print("-" * 80)
    print(f"{quote}\n")
    print(f"- {author}")
    print("-" * 80 + "\n")

category = input("Enter a category (or leave blank for random): ")
author = input("Enter an author (or leave blank for random): ")
quote, author = get_random_quote(category, author)
display_quote(quote, author, category, show_filter_options=False)