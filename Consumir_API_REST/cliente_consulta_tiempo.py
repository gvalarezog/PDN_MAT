import requests


def consulta_tiempo(url, api_key, ciudad, pais_ISO2):
    parametros = {'key':api_key, 'city':ciudad, 'country':pais_ISO2}
    tiempo = requests.get(url=url,params=parametros)
    tiempo = tiempo.json()

    print(tiempo)

if __name__=='__main__':
    url_api = 'http://api.weatherbit.io/v2.0/current'
    consulta_tiempo(url=url_api, pais_ISO2='EC', ciudad='Quito', api_key='f2abe4042e454ccc80b7353a6f5ef495')