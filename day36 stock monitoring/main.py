import requests
import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_api_key = '27ESG5ACE1W0V905'

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api_key = "354cc38a6ffe4ddea05fce0c70c18405"

account_sid = "AC4b2125af66e06da78324e3c107b726b2"
auth_token = "d6fcf9661e6055c01d47cd1aa9f7f3d7"

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
today = datetime.datetime.today() #2024-08-17
base_date = today - datetime.timedelta(days=1)
before_base_date = base_date - datetime.timedelta(days=1) # What about weekends??
latter_day = base_date.strftime('%Y-%m-%d')
former_day = before_base_date.strftime('%Y-%m-%d')
print(latter_day, former_day)

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
latter_close = stock_data[latter_day]["4. close"]
former_close = stock_data[former_day]["4. close"]
print(latter_close, former_close)
fluc_rate = abs(float(latter_close) - float(former_close))/float(latter_close)
fluc_rate = round(fluc_rate, 4)
# fluc_rate = 2
# former_close = 98
# latter_close = 100
print(f"fluctuation rate: {fluc_rate}")

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
if fluc_rate >= 0:
    news_params = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
    formatted_articles = [(f"Headline: {article['title']}.\nBrief: {article['description']}") for article in three_articles]
    print(formatted_articles)

    try:
        fluc = ""
        if former_close < latter_close:
            fluc = "🔺"
        else:
            fluc = "🔻"

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{COMPANY_NAME}: {fluc}{fluc_rate}%\n"
                 f"First article:\n{formatted_articles[0]}\n"
                 f"Second article:\n{formatted_articles[1]}\n"
                 f"Third article:\n{formatted_articles[2]}",
            from_='whatsapp:+14155238886',
            to = 'whatsapp:+491739708177'
        )
        print("Message successfully sent")
    except Exception as e:
        print(f"Failed to send message: {e}")

else:
    print("Nothing to send.")


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the
  coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
"""

