import re

data = {
    "chat_id": "@testingBot47",
    "text": "Hello, Structured!",
}

command_regex = "/trabajoLOL"

x = re.findall("^/trabajo*", command_regex)

print(x)

if x == ["/trabajo"]:
    print("Existe")

#get_chat(-1001747799058)

#send_static_message(-1001747799058, "LOL! Como agrandar tu pene al cuadrado de forma totalmente privada con un bug reloco ekisde y ademas con otro id LOL")

## old code

for _ in range(2):
    print("Hola, Mundo!")