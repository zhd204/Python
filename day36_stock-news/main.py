import requests
import os
from utils import response_data, select_day
import html
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
FUNCTION = "TIME_SERIES_DAILY"
STK_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stk_api_key = os.environ.get("STK_API_KEY")
stk_parameters = {
    "function": FUNCTION,
    "symbol": STOCK,
    "interval": "30min",
    "adjusted": True,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": stk_api_key
}

stk_data = response_data(url=STK_URL, params=stk_parameters)
yesterday = select_day(stk_data["Time Series (Daily)"], 1)  # yyyy-mm-dd as string
day_before_yesterday = select_day(stk_data["Time Series (Daily)"], 2, date=yesterday)  # yyyy-mm-dd as string
print(yesterday, day_before_yesterday)
yesterday_close_price = float(stk_data["Time Series (Daily)"][yesterday]["4. close"])
day_before_yesterday_close_price = float(stk_data["Time Series (Daily)"][day_before_yesterday]["4. close"])

change_per = (yesterday_close_price - day_before_yesterday_close_price) / day_before_yesterday_close_price

if abs(change_per) >= 0.05:

    # Get the first 3 news pieces for the COMPANY_NAME.
    news_api_key = os.environ.get("NEWS_API_KEY")
    news_parameter = {
        "q": "tesla",
        "sortBy": "publishedAt",
        "apiKey": news_api_key
    }

    news_data = response_data(url=NEWS_URL, params=news_parameter)

    if change_per >= 0:
        news_string = f"{STOCK}: 🔺{abs(change_per) * 100:.2f}%\n\n"
    else:
        news_string = f"{STOCK}: 🔻{abs(change_per) * 100:.2f}%\n\n"

    for i in range(3):
        news_string += f"Headline: {news_data['articles'][i]['title']}. ({STOCK})?." \
                       f"\nBrief: {html.unescape(news_data['articles'][i]['description'])}\n\n"

    # STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    # Twilio account info
    account_sid = os.environ["ACCT_SID"]
    auth_token = os.environ["AUTH_TOKEN"]

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=news_string,
        from_="+16674010418",  # purchased/trial phone number from Twilio
        to="+17178142546"  # verified number with Twilio, in this case it is the phone number used via the registration.
    )
    print(message.status)
else:
    print(change_per)
# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
