import requests


def listar_nombre_paises(url):
    paises = requests.get(url)
    paises = paises.json()

    for pais in paises:
        #print(f"Nombre Comun:{pais['name']['common']}")
        #print(f"Nombre Oficial:{pais['name']['official']}")
        #print(f"Nombre Oficial:{pais['oficial']}")

        # Nombre oficial, capital, moneda, codigo telefonico
        print(f"Nombre Oficial en Español: {pais['translations']['spa']['official']}")
        print(f"La capital es: {pais['capital'][0]}")
        Moneda= pais ['currencies']
        for monedas in Moneda.values():
           print(f"La moneda es: {monedas['name']}, simbolo: {monedas['symbol']}")
        print(f"El codigo telefonico es: {pais['idd']['root']+pais['idd']['suffixes'][0]}")
        #print(pais)

url = 'https://restcountries.com/v3.1/independent?status=true&fields=translations,capital,currencies,idd'
listar_nombre_paises(url)