import requests
import time

website = 'https://www.manishjha.in/'

interval = 5
while True:
    try:
        info = requests.get(website)
        print(info)
    except:
        print(f"Could not connect to: {website}")
        print({
                "code" : 404,
                "status" : "FAILURE"
        })

    print(f"Will do again in {interval} seconds ...")
    time.sleep(5)