# ISS-Overhead-Notifier

Technologies/Concepts Used: Python, API Endpoints, API Parameters, smtplib (sending mails)

1. This program sends a notification email to the user when the International Space Station is overhead during the night sky.
2. It makes use of API endpoints to find the geographical coordinates of ISS and compare it with the current location.
3. Once it is dark (after sunset and before sunrise) and the ISS is within +-5 degrees of current location, it sends an email notifying to look up in the sky.


![International Space Station](https://user-images.githubusercontent.com/88761228/211168492-7c26a611-7eed-4dae-986d-2535c35c4aba.jpg)
