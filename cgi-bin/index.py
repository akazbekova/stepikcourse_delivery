import json
from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"


alive_state = True

@app.route("/alive")
def alive():
    if alive_state:
        return '{"alive":true}'
    else:
        return '{"alive":true}'


workhours_open = "08:00"
workhours_closes = "20:00"
schedule = {"opens": workhours_open, "closes": workhours_closes}
@app.route("/workhours")
def workhours():
    return json.dumps(schedule)

promocode = "stepik"
promo_discount = "15%"
promotion_text = {"promotion":"Сегодня скидка "+ promo_discount +" по промокоду " + promocode}
@app.route("/promotion")
def promotion():
    return json.dumps(promotion_text, ensure_ascii=False)


@app.route("/promo")
def promotion_text():
    all_promotions = [
        "Сегодня скидка 15% по промокоду stepik",
        "Сегодня скидка 10% по промокоду summer",
        "Удваиваем все пиццы по промокоду udodopizza"
    ]
    promotion_number = random.randint(0,2)
    return json.dumps({"promotion": all_promotions[promotion_number]}, ensure_ascii=False)


@app.route("/promo/<code>")
def checkpromo(code):
    if code == "Stepik":
        return '{"valid":true, "discount":15}'
    elif code == "summer":
        return '{"valid":true, "discount":10}'
    elif code == "pleaseplease":
        return '{"valid":true, "discount":5}'
    else:
        return '{"valid":false, "discount":0}'


app.run("localhost",8000)

