import requests


response = requests.get(
    "https://terjetheteacher.github.io/some-jokes/justJokes.json"
)
print(response.status_code)
jokes = response.json()   


print("vits 1 = " + jokes["1"])



print("alle vitser")
for nummer, vits in jokes.items():
    print(f"{nummer}: {vits}")

#Jeg brukte en API for å hente vitser direkte fra https://terjetheteacher.github.io/some-jokes/justJokes.json i stedet for å lage en egen json fil til.
#Jeg brukte koden fra oppgave 6 for å importere vitsene