from http.client import responses

import requests


usl = 'https://www.youtube.com/watch?v=0BcNGMvf80E&list=PLuEo4W0EBxtWLw8glAHArx1JybLl81LI3&index=9'

responses = requests.get(usl)
pass