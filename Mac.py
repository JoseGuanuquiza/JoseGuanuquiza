import network

# Inicializamos el objeto de la red
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Obtenemos la dirección MAC
mac = wlan.config('mac')

# Convertimos la dirección MAC a un formato legible
mac_address = ':'.join(f'{b:02x}' for b in mac)

print("Dirección MAC:", mac_address)
