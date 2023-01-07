import requests
from datetime import datetime
import smtplib
import time

MY_LAT =  000 # Your latitude
MY_LONG =  000 # Your longitude

MY_EMAIL = "" # Enter Email you want to send the email from.
MY_PASSWORD = "" #Enter the app password for that email.

TO_EMAIL = "" #Email of user whom you'd like to notify.

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(MY_LAT - iss_latitude) < 5 and abs(MY_LONG - iss_longitude) < 5:
        return True

#Your position is within +5 or -5 degrees of the ISS position.

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now.hour > sunset and time_now.hour < sunrise:
        return True


while True:
    if is_overhead() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg="Subject:ISS Notification\n\nLook Up!!"
            )
    time.sleep(60)
