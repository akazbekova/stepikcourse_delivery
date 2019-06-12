import json
from flask import Flask
import random

datafile_encoding = 'utf8'
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"


alive_state = True

@app.route("/alive")
def alive():
    config_file = open('C:/Users/user/PycharmProjects/stepikcourse_delivery/config.json', "r")
    config_content = config_file.read()
    data = json.loads(config_content)
    config_file.close()
    return json.dumps({"alive":data["alive"]})


@app.route("/workhours")
def workhours():
    config_file = open('C:/Users/user/PycharmProjects/stepikcourse_delivery/config.json', "r")
    config_content = config_file.read()
    data = json.loads(config_content)
    config_file.close()
    return json.dumps(data["workhours"])



@app.route("/promotion")
def promotion_text():
    promotion_number = random.randint(0,2)
    promotion_file = open('C:/Users/user/PycharmProjects/stepikcourse_delivery/promotions.json', "r")
    promotions = json.loads(promotion_file.read())
    return json.dumps(promotions[promotion_number], ensure_ascii=False)


@app.route("/promo")
def promo_text():
    all_promotions = [
        "Сегодня скидка 15% по промокоду stepik",
        "Сегодня скидка 10% по промокоду summer",
        "Удваиваем все пиццы по промокоду udodopizza"
    ]
    promo_random = random.randint(0,2)
    return json.dumps({"promotion": all_promotions[promo_random]}, ensure_ascii=False)


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

