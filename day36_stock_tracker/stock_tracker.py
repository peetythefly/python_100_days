import finnhub, auth#, requests
import datetime as dt

# We'll get the stocks for FAANG and Microsoft.
# ISINS = ("US0378331005", "US0231351067", "US38259P5089", "US30303M1027", "US64110L1061", "US5949181045")
# SYMBOLS = ("AAPL","AMZN","GOOG","META","NFLX", "MSFT")
STOCKS = {
    "AAPL" : "US0378331005",
    "AMZN" : "US0231351067",
    "GOOG" : "US02079K3059",
    "META" : "US30303M1027",
    "NFLX" : "US64110L1061",
    "MSFT" : "US5949181045",
}

# We will use finnhub's python-specific library.
finnhub_client = finnhub.Client(api_key=auth.finnhub_api_key)
for stock in STOCKS:
    lookup = finnhub_client.symbol_lookup(STOCKS[stock])["result"][0]
    name = lookup["description"]
    quote = finnhub_client.quote(stock)
    price = quote["c"]
    prev_price = quote["pc"]
    delta = (price - prev_price) / prev_price
    percent = round (delta * 100, 2)
    now = dt.datetime.now()
    # Replace the space(s) in the name with the proper html character for the url.
    news_url = f"https://news.google.com/search?q={name.replace(" ", "&nbsp;")}&hl=en-US&gl=US&ceid=US%3Aen"
    report = f"""{name} Statistics on {now.month}/{now.day}:
Percent change from yesterday is {percent}%
Current price is ${price}.
Day change is ${quote["d"]}.
Percent change is ${quote["dp"]}.
High price of the day is ${quote["h"]}.
Low price of the day is ${quote["l"]}.
Open price of the day is ${quote["o"]}.
Previous close price was ${prev_price}.\n"""
    print(report)
    # If there is a change in the previous close price by more than 5%, build a report and dump it to the desktop.
    if abs(percent) >= 1:
        with open(file=f"{auth.my_desktop}/StockAlert.txt", mode="a") as stock_file:
            stock_file.write(f"\n{report}\nLink to news:\n{news_url}")
        
# Another option is to use the requests library.
# parameters = {
#     "token" : auth.finnhub_api_key,
#     "q" : "US5949181045"
# }
# search_url = "https://finnhub.io/api/v1/search"
# search_response = requests.get(url=search_url, params=parameters)
# quote_url = "https://finnhub.io/api/v1/quote"
# quote_response = requests.get(url=quote_url, params=parameters)
# print(quote_response.json())
# print(response.json())

