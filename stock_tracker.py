import requests
import datetime as dt
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "KZHZLOXKHG08PGYF"
NEWS_API_KEY = "e8e5f04272b14218ac8302d52ee34591"

TWILIO_ACCOUNT_SID = "AC6b77186dc8771b944ade3ec50e65dfb6"
TWILIO_AUTH_TOKEN = "79691a6a96738c24bcc51eee295784c7"


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY,
    "outputsize":"compact"
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data_stock = response.json()

#Obtener la fecha de ayer
now = dt.date.today()
yesterday = now - dt.timedelta(days=1)
before_yesterday = now - dt.timedelta(days=2)


yesterday, before_yesterday = str(yesterday), str(before_yesterday)

price_yesterday = data_stock["Time Series (Daily)"][yesterday]["4. close"]


#TODO 2. - Get the day before yesterday's closing stock price
price_before_yesterday = data_stock["Time Series (Daily)"][before_yesterday]["4. close"]
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
price_yesterday = float(price_yesterday)
price_before_yesterday = float(price_before_yesterday)

diff = price_yesterday - price_before_yesterday
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percentage = (diff*100)/price_yesterday
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percentage >= 5:
    print("Hello")


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_params = {
    "apiKey":"e8e5f04272b14218ac8302d52ee34591",
    "q":COMPANY_NAME,
    "sortBy": "publishedAt"
}
response = requests.get(NEWS_ENDPOINT, params=news_params)
response.raise_for_status()
news_data = response.json()
print(response.url)
three_articles = news_data["articles"][0:3]
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
articles_send = [[article["title"],article["description"]] for article in three_articles]
#TODO 9. - Send each article as a separate message via Twilio. 
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
for article in articles_send:
    if price_yesterday < price_before_yesterday:
        message = client.messages \
                        .create(
                            body=f"TSLA: 🔻{round(diff_percentage,2)} \n Headline: {article[0]} \n Brief: {article[1]} \n \
                            Precio ayer: {price_yesterday} \n precio Anteayer: {price_before_yesterday}",
                            from_='+12565949273',
                            to='+573006129875'
                        )
    elif price_yesterday > price_before_yesterday:
         message = client.messages \
                        .create(
                            body=f"TSLA: 🔺{round(diff_percentage,2)} \n Headline: {article[0]} \n Brief: {article[1]} \
                                \n Precio ayer: {price_yesterday} \n precio Anteayer: {price_before_yesterday}",
                            from_='+12565949273',
                            to='+573006129875'
                        )

print(message.status)


#Optional TODO: Format the message like this: 


