from anime_muip import AnimeMUIP

client = AnimeMUIP('YOUR_TOKEN', ip='10.242.1.1')
response = client.muip_client("7", "mcoin 1")
print(response)