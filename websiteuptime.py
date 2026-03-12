import requests as req

requrl = input("Enter target URL (make sure to add the HTTP): ").strip()

try:
    response = req.get(requrl, timeout=5)
    if response.status_code == 200:
        print("Website is up and running :)")
    elif response.status_code == 404:
        print("That website doesn't seem to exist")
    elif response.status_code == 301:
        print("The website redirected the request")
    elif response.status_code == 500:
        print("The server encountered an internal error")
    else:
        print(f"Website returned unexpected status: {response.status_code}")

except req.exceptions.RequestException as e:
    print("Could not reach the website:", e)