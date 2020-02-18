# TERRY A. DAVIS RANDOM VIDEO GENERATOR!
import webbrowser
import json
import random

links = json.loads(open("links.json").read())
choice = random.choice(links)
webbrowser.open(choice, new=2)
print("# SOME VIDEOS ARE AGE RESTRICTED!\n# BE SIGNED INTO YOUTUBE FOR BEST RESULTS!")
print(f"Opening: {choice}")
