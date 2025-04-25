# Exercicio‑de‑Programacao‑2‑Python 

Segundo Exercício‑Programa (EP2) da disciplina **MAC2166 – Introdução à Computação** (USP/Poli). O objetivo é praticar manipulação de listas e aritmética de polinômios em Python, desenvolvendo rotinas para:
* Verificar se um número é raiz de um polinômio;
* Dividir polinômios por (x − b) ou (ax − b);
* Listar raízes inteiras ou racionais de um polinômio;
* Representar raízes racionais como inteiros ou frações simplificadas;
* Exibir polinômios em forma legível.

## Índice 📑
- Descrição 📝  
- Pré‑requisitos ⚙️  
- Estrutura do Projeto 🗂️  
- Instalação 🔧  
- Uso 🚀  
- Exemplo de Execução 💻  
- Funções Disponíveis 🔍  
- Licença 📜  

## Descrição 📝
O arquivo **ep02.py** contém:
| Função | Propósito |
| --- | --- |
| `polinomioComRaiz(p, b)` | retorna `True` se *b* é raiz de *p(x)* |
| `polinomioQuociente(p, b)` | devolve *p(x)/(x − b)* |
| `listaCanonicaDeRaizes(p)` | lista raízes inteiras em ordem canônica |
| `polinomioQuocienteRacional(p, b, a)` | devolve quociente e resto de *p(x)/(ax − b)* |
| `listaRaizesRacionais(p)` | lista raízes racionais p/q |
| `racionalToString(p_n, r)` | formata raiz como inteiro ou fração reduzida |
Funções auxiliares **`polinomioToString`** e **`sig`** geram strings de polinômios; a função **`main()`** lê dados do usuário e imprime as raízes.

## Pré‑requisitos ⚙️
- Python ≥ 3.6 (sem dependências externas)

## Estrutura do Projeto 🗂️
```
├── ep02.py          # Código‑fonte completo (339 linhas)
├── LICENSE          # MIT
└── README.md        # (substituir por este 🙂)
```

## Instalação 🔧
```bash
git clone https://github.com/rafael-agra/Exercicio-de-Programacao-2-Python.git
cd Exercicio-de-Programacao-2-Python
python ep02.py  # ou abra em seu IDE favorito
```

## Uso 🚀
Ao executar **ep02.py**, o programa:
1. Pede o grau `n` do polinômio;
2. Solicita `n + 1` coeficientes (`p[0] … p[n]`), do termo independente ao dominante;
3. Calcula e imprime a lista canônica de raízes inteiras (se `p[n] = 1`) ou racionais.

### Exemplo de Execução 💻
```
Digite o grau: 3
Digite p[0]: -6
Digite p[1]: 11
Digite p[2]: -6
Digite p[3]: 1
A lista canonica das raizes inteiras de p(x) = x^3-6x^2+11x-6 eh:
1 2 3
```

## Funções Disponíveis 🔍
- `polinomioComRaiz(p, b)`  
- `polinomioQuociente(p, b)`  
- `listaCanonicaDeRaizes(p)`  
- `polinomioQuocienteRacional(p, b, a)`  
- `listaRaizesRacionais(p)`  
- `racionalToString(pn, r)`  

Todas incluem docstrings explicativas.

## Licença 📜
Distribuído sob a licença **MIT** — consulte `LICENSE` para detalhes.

