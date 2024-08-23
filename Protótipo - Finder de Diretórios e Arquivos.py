import requests

#url = input("Insira o diretório desejado")
url = "https://www.alura.com.br"

diretorios = open("diretorios.txt", "r")


for diretorio in diretorios:    
    urlcompleta = url+"/"+diretorio.strip()

    try:
       response = requests.get(urlcompleta)

       if response.status_code != 200:
           print(f"Status: {response.status_code} - diretório {urlcompleta} não encontrado ")
       else:
            print(f"Status: {response.status_code} - diretório {urlcompleta} encontrado ")
            arquivos = open("arquivos.txt", "r")

            for arquivo in arquivos:                
                urlcompleta2 = urlcompleta+"/"+arquivo                

                try:  
                    response2 = requests.get(urlcompleta2)
                    if response2.status_code != 200:
                        print(f"    Status: {response2.status_code} não foi possível acessar o arquivo {urlcompleta2}")
                    else:
                        print(f"    Status: {response2.status_code} foi encontrado o arquivo {urlcompleta2} !!!!!!!!!!!!!!")
                except:
                    print(f"    Status: {response2.status_code} não foi possível acessar o arquivo {urlcompleta2}")
                
    except:
        print(f"diretório {urlcompleta} não encontrado")