# Teste de Carga HTTP

Script Python para simular requisicoes HTTP simultaneas e testar a resiliencia de um servidor sob carga.

## O que faz

Cria um pool controlado de threads que disparam requisicoes GET em paralelo para uma URL alvo. Ao final exibe estatisticas completas: tempo total, sucessos, falhas, tempo medio/minimo/maximo e distribuicao de status codes HTTP.

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

Execute o script e responda as perguntas no terminal:

```bash
python iniciar.py
```

Sera solicitado:

1. **URL para teste** — endereco completo (ex: `https://seusite.com`)
2. **Total de requisicoes** — quantidade total de requisicoes (padrao: 100)
3. **Conexoes simultaneas** — numero de threads em paralelo (padrao: 10)
4. **Timeout por requisicao** — tempo maximo de espera em segundos (padrao: 10)

Ao final, o script pergunta se deseja executar outro teste.

## Exemplo de saida

```
==================================================
     TESTE DE CARGA HTTP
==================================================

URL para teste: https://httpbin.org/get
Total de requisicoes (padrao 100): 50
Conexoes simultaneas (padrao 10): 5
Timeout por requisicao (s) (padrao 10):

Iniciando teste de carga em https://httpbin.org/get
Total: 50 | Concorrentes: 5 | Timeout: 10s

[1/50] HTTP 200 em 0.234s
[2/50] HTTP 200 em 0.189s
...

==================================================
RESULTADOS
==================================================
Tempo total:     2.45s
Requisicoes:     50
Sucessos:        50
Falhas:          0
Tempo medio:     0.234s
Tempo minimo:    0.189s
Tempo maximo:    0.312s

Status codes:
  HTTP 200: 50
==================================================

Executar outro teste? (s/n):
```

## Aviso

Use este script apenas em servidores **de sua propriedade** ou com **autorizacao explicita** do responsavel. Testes de carga nao autorizados podem ser considerados ataques DDoS.

---

Code by Jhonny.
