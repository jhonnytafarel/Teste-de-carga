#Quer saber mais do codigo? acesse o arquivo Leia-me dentro da pasta.
import requests
import threading

def fazer_requisicao(url):
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
    except Exception as e:
        print(f"Erro: {e}")

def iniciar_teste(url, num_requisicoes):
    threads = []
    for _ in range(num_requisicoes):
        thread = threading.Thread(target=fazer_requisicao, args=(url,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

url_do_site = "URL PARA TESTE" # Url
num_requisicoes = 10000 # Número de requisições simultâneas

iniciar_teste(url_do_site, num_requisicoes) #Code BY:Jhonny.


