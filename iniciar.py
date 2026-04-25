#!/usr/bin/env python3
"""Teste de carga HTTP com interface interativa no terminal."""

import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests


def fazer_requisicao(url, timeout):
    inicio = time.perf_counter()
    try:
        response = requests.get(url, timeout=timeout)
        duracao = time.perf_counter() - inicio
        return {
            "status": response.status_code,
            "duracao": duracao,
            "erro": None,
        }
    except requests.exceptions.Timeout:
        return {"status": None, "duracao": timeout, "erro": "Timeout"}
    except requests.exceptions.RequestException as e:
        return {"status": None, "duracao": 0, "erro": str(e)}


def perguntar_url():
    while True:
        url = input("URL para teste: ").strip()
        if url.startswith(("http://", "https://")):
            return url
        print("Erro: URL deve comecar com http:// ou https://")


def perguntar_numero(mensagem, padrao, minimo=1):
    while True:
        entrada = input(f"{mensagem} (padrao {padrao}): ").strip()
        if not entrada:
            return padrao
        try:
            valor = int(entrada)
            if valor < minimo:
                print(f"Erro: valor minimo e {minimo}")
                continue
            return valor
        except ValueError:
            print("Erro: digite um numero valido")


def iniciar_teste(url, total, concorrentes, timeout):
    sucessos = 0
    falhas = 0
    tempos = []
    codigos = {}

    print(f"\nIniciando teste de carga em {url}")
    print(f"Total: {total} | Concorrentes: {concorrentes} | Timeout: {timeout}s\n")

    inicio_total = time.perf_counter()

    with ThreadPoolExecutor(max_workers=concorrentes) as executor:
        futuros = {
            executor.submit(fazer_requisicao, url, timeout): i
            for i in range(total)
        }
        for futuro in as_completed(futuros):
            resultado = futuro.result()
            idx = futuros[futuro]

            if resultado["erro"]:
                falhas += 1
                print(f"[{idx + 1}/{total}] ERRO: {resultado['erro']}")
            else:
                sucessos += 1
                tempos.append(resultado["duracao"])
                codigo = resultado["status"]
                codigos[codigo] = codigos.get(codigo, 0) + 1
                print(
                    f"[{idx + 1}/{total}] HTTP {codigo} em {resultado['duracao']:.3f}s"
                )

    duracao_total = time.perf_counter() - inicio_total

    print("\n" + "=" * 50)
    print("RESULTADOS")
    print("=" * 50)
    print(f"Tempo total:     {duracao_total:.2f}s")
    print(f"Requisicoes:     {total}")
    print(f"Sucessos:        {sucessos}")
    print(f"Falhas:          {falhas}")
    if tempos:
        print(f"Tempo medio:     {sum(tempos) / len(tempos):.3f}s")
        print(f"Tempo minimo:    {min(tempos):.3f}s")
        print(f"Tempo maximo:    {max(tempos):.3f}s")
    print("\nStatus codes:")
    for codigo, qtd in sorted(codigos.items()):
        print(f"  HTTP {codigo}: {qtd}")
    print("=" * 50)


def main():
    print("=" * 50)
    print("     TESTE DE CARGA HTTP")
    print("=" * 50)
    print()

    url = perguntar_url()
    total = perguntar_numero("Total de requisicoes", 100)
    concorrentes = perguntar_numero("Conexoes simultaneas", 10)
    timeout = perguntar_numero("Timeout por requisicao (s)", 10)

    print()
    iniciar_teste(url, total, concorrentes, timeout)

    print()
    again = input("Executar outro teste? (s/n): ").strip().lower()
    if again == "s":
        print()
        main()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTeste interrompido.")
        sys.exit(0)
