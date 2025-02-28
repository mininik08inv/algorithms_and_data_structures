import requests

r = requests.get("http://127.0.0.1:8000/hotels/12345", params={"date_from": "todayyyy", "date_to": "tomorrowww"})


print(r.text)