import decimal
import logging
from pywebio.input import slider, FLOAT, NUMBER, input as pw_input

from pywebio.output import put_html, put_success
from tornado.log import app_log

logging.basicConfig(level= logging.INFO, format="%(asctime)s - %(lewelname)s - %(massage)s",
                    handlers=[logging.FileHandler("shop.log"), logging.StreamHandler()],)


APPLE_PRICE = decimal.Decimal(52.75)
BANANA_PRICE = decimal.Decimal(81.40)

logging.debug("debug")
logging.info("info")

put_html("<h1>Welcome to our Fruit Shop</h1>"
         "<h1>Введіть кількість кілограмів за товар!</h1>")

apple_weight = slider(
    "Вага яблук. (Від 0 до 5 кг)", type=FLOAT, min_value=0, max_value=5, value=0.15, required=True)

apple_weight = decimal.Decimal(apple_weight).quantize(
    decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP)

banana_weight = pw_input("Вага бананів. (від 0 до 10 кг)", type=NUMBER, required=True, min=0, max=10, value=3)
banana_weight = decimal.Decimal(banana_weight).quantize(
    decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP)

logging.info(f"{banana_weight=}")

apple_cost = (APPLE_PRICE * apple_weight).quantize(
    decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
)
banana_cost = (BANANA_PRICE * banana_weight).quantize(
    decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
)
total_cost = apple_cost + banana_cost
put_success(
    f"Total cost: \nЯ'блука:\t{apple_cost}\t грн \nБанани:\t{banana_cost}\t грн \nЗагальна сума:\t{total_cost}\t грн"
)
