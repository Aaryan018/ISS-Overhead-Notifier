# ISS-Overhead-Notifier

Technologies/Concepts Used: Python, API Endpoints, API Parameters, smtplib (sending mails)

1. This program sends a notification email to the user when the International Space Station is overhead during the night sky.
2. It makes use of API endpoints to find the geographical coordinates of ISS and compare it with the current location.
3. Once it is dark (after sunset and before sunrise) and the ISS is within +-5 degrees of current location, it sends an email notifying to look up in the sky.


![International Space Station](https://user-images.githubusercontent.com/88761228/211168409-217c00da-0767-4c47-a0f1-74aed61e9aab.jpg)
