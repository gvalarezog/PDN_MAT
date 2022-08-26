import requests


def listar_paises(ruta):
    paises = requests.get(ruta)
    paises = paises.json()
    for pais in paises:
        print(pais['name']['official'])

def detalle_pais(pais):
    ruta_pais = 'https://restcountries.com/v3.1/name/' + pais
    pais = requests.get(ruta_pais)
    pais = pais.json()
    # print(pais)
    # print(pais[0]['name'])
    # print(pais[0]['name']['common'])
    nombre = pais[0]['name']['common']
    # print(pais[0]['tld'][0])
    sub_dominio = pais[0]['tld'][0]
    # print(pais[0]['idd']['root'])
    # print(pais[0]['idd']['suffixes'][0])
    # print(pais[0]['idd']['root'] + pais[0]['idd']['suffixes'][0])
    codigo_telefonico = pais[0]['idd']['root'] + pais[0]['idd']['suffixes'][0]
    # print(pais[0]['capital'][0])
    capital = pais[0]['capital'][0]
    texto =  f'El pais {nombre} tiene como capital {capital}, su codigo telfonico es: {codigo_telefonico} ' \
             f'y el sub dominio es {sub_dominio}'

    print(texto)

if __name__=='__main__':
    ruta = 'https://restcountries.com/v3.1/all'
    listar_paises(ruta)
    print('*'.center(10, '*'))
    detalle_pais('Ecuador')
