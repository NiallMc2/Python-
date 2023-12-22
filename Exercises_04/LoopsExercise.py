scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
print (scan)
keys = scan.keys()
items = scan.items()


  #Iterating keys

print("IP Address:", keys)

 #Iterating items

print("Port Number:", items)
	
print(f"Found a service on {keys} at {items}")


