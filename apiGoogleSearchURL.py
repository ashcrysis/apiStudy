from googlesearch import search

def buscar_no_google(query, num_results=10, lang='pt-br'):
    resultados = []

    # Itera pelos resultados da busca
    for i, resultado in enumerate(search(query, lang=lang), start=1):
        resultados.append(resultado)
        if i == num_results:
            break

    return resultados

# String que você deseja pesquisar
minha_busca = "Como ensinar um cão a rolar no chão"

# Número de resultados que você deseja obter (até 10)
numero_resultados = 10

# Realiza a busca
resultados = buscar_no_google(minha_busca, num_results=numero_resultados)

# Exibe os resultados
for i, resultado in enumerate(resultados, start=1):
    print(f"Resultado #{i}: {resultado}")
