# ISS-Overhead-Notifier

Technologies/Concepts Used: Python, API Endpoints, API Parameters, smtplib (sending mails)

1. This program sends a notification email to the user when the International Space Station is overhead during the night sky.
2. It makes use of API endpoints to find the geographical coordinates of ISS and compare it with the current location.
3. Once it is dark (after sunset and before sunrise) and the ISS is within +-5 degrees of current location, it sends an email notifying to look up in the sky.
4. Open source API from the following website has been used to determine the live location of the International Space Station:
http://api.open-notify.org/

Note: The best way to execute this program is to host and run it on cloud that supports Python. This ensures that the scripts are running and whenever the ISS is overhead, it notifies the user.
 

Use the following steps to run this project: Download the zip file and make following changes to the main.py

1. Variable **MY_LAT**: Latitude of your current location.
2. Variable **MY_LONG**: Longitude of your current location.
3. Variable **FROM_EMAIL**: Enter Email you want to send the email from.
4. Variable **MY_PASSWORD**: Enter the app password for that email.
5. Variable **TO_EMAIL**: Email of user whom you'd like to notify.

![International Space Station](https://user-images.githubusercontent.com/88761228/211168534-58848c48-affe-421d-8d7e-68b088fd5dae.jpg)
