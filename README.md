# Teste de Carga HTTP

Script Python simples para simular requisicoes HTTP simultaneas e testar a resiliencia de um servidor sob carga.

## O que faz

Cria N threads que disparam requisicoes GET em paralelo para uma URL alvo. Cada thread executa uma requisicao independente e imprime o status code da resposta (ou erro, se houver).

Ideal para:
- Verificar como um servidor se comporta com trafego concorrente
- Testar limites de conexoes simultaneas
- Validar estabilidade de endpoints simples

## Requisitos

- Python 3.x
- Biblioteca `requests`

```bash
pip install requests
```

## Como usar

1. Abra o arquivo `iniciar.py`
2. Altere as variaveis no final do script:

```python
url_do_site = "https://seu-site-aqui.com"  # URL alvo
num_requisicoes = 1000                       # Quantidade de requisicoes simultaneas
```

3. Execute:

```bash
python iniciar.py
```

## Parametros

| Variavel | Descricao | Padrao |
|----------|-----------|--------|
| `url_do_site` | Endereco a ser testado | `"URL PARA TESTE"` |
| `num_requisicoes` | Numero de threads/requisicoes | `10000` |

## Aviso

Use este script apenas em servidores **de sua propriedade** ou com **autorizacao explicita** do responsavel. Testes de carga nao autorizados podem ser considerados ataques DDoS.

---

Code by Jhonny.
