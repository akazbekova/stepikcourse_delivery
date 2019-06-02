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



@app.route("/promo")
def promotion_text():
    all_promotions = [
        "Сегодня скидка 15% по промокоду stepik",
        "Сегодня скидка 10% по промокоду summer",
        "Удваиваем все пиццы по промокоду udodopizza"
    ]
    promotion_number = random.randint(0,2)
    return json.dumps({"promotion": all_promotions[promotion_number]}, ensure_ascii=False)



promocodes_list = [
      {"code":"doubletrouble", "discount":"50%"},
      {"code":"illbeback", "discount":"25%"},
      {"code":"stepik", "discount":"25%"},
      {"code":"libertyordeath", "discount":"100%"},
      {"code":"summer", "discount":"10%"},
      {"code":"pleaseplease", "discount":"5%"}]

@app.route("/promo/<code>")
def checkpromo(code):
  for n in promocodes_list:
       if code.lower() == n["code"]:
           return json.dumps({"valid":True,"discount": n["discount"]})
  return json.dumps({"valid":False, "discount":0})



meals = [{
 "title": "Chinken",
 "id": 1,
 "available": True,
 "picture": "",
 "price": 20.0,
 "category": 1
}, {
 "title": "Milk",
 "id": 2,
 "available": True,
 "picture": "",
 "price": 10.0,
 "category": 1
}]

@app.route("/meals")
def meal():
    return json.dumps(meals, ensure_ascii=False)


app.run("localhost",8000)

