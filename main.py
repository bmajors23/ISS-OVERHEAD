import requests
from datetime import datetime
import smtplib

MY_LAT = -39.9444 # Your latitude
MY_LONG = 149.1653 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


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

time_now = datetime.now()
hour = time_now.hour


if iss_latitude > MY_LAT - 5 and iss_latitude < MY_LAT + 5 and iss_longitude > MY_LONG - 5 and iss_longitude < MY_LONG + 5:
    if sunset < hour < sunrise:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login("billyjoe17667@gmail.com", "12345!")
            connection.sendmail(
                from_addr="billyjoe17667@gmail.com",
                to_addrs="billyjoe17667@gmail.com",
                msg=f"Subject:Look up!\n\nThe iss satellite is above you now!"
            )



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



