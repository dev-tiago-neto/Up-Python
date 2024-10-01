import random
from os import system as sys

quiz = [
    {
        "pergunta": "Qual é a principal fonte de energia utilizada pela Fórmula E?",
        "alternativas": ["Combustível fóssil", "Eletricidade", "Biocombustível"],
        "resposta_idx": 1,
    },
    {
        "pergunta": "Como a Fórmula E contribui para a redução da emissão de gases de efeito estufa?",
        "alternativas": [
            "Usando carros híbridos",
            "Utilizando motores elétricos",
            "Diminuindo o número de corridas",
        ],
        "resposta_idx": 1,
    },
    {
        "pergunta": "Em que tipo de local geralmente acontecem as corridas da Fórmula E?",
        "alternativas": ["Autódromos permanentes", "Circuitos de rua", "Pistas de aeroportos"],
        "resposta_idx": 1,
    },
    {
        "pergunta": "Qual é uma vantagem ambiental direta das baterias usadas na Fórmula E?",
        "alternativas": ["Produzem mais ruído", "Geram menos emissões", "São mais baratas"],
        "resposta_idx": 1,
    },
    {
        "pergunta": "Como a Fórmula E promove a sustentabilidade nas cidades onde realiza corridas?",
        "alternativas": [
            "Através de campanhas de sensibilização ambiental",
            "Dando ingressos gratuitos",
            "Construindo novas pistas permanentes",
        ],
        "resposta_idx": 0,
    },
    {
        "pergunta": "O que acontece com as baterias usadas pelos carros da Fórmula E após o uso?",
        "alternativas": ["São descartadas em aterros", "São recicladas", "São vendidas como sucata"],
        "resposta_idx": 1,
    },
    {
        "pergunta": "Qual é o impacto do menor nível de ruído dos carros da Fórmula E nas cidades?",
        "alternativas": ["Reduz a poluição sonora", "Aumenta a poluição sonora", "Não tem impacto"],
        "resposta_idx": 0,
    },
    {
        "pergunta": "Como a Fórmula E ajuda a promover a inovação em veículos elétricos?",
        "alternativas": [
            "Mantendo a tecnologia em segredo",
            "Testando e desenvolvendo novas tecnologias",
            "Limitando o uso de novas tecnologias",
        ],
        "resposta_idx": 1,
    },
    {
        "pergunta": "Qual é uma diferença chave entre os pneus usados na Fórmula E e na Fórmula 1?",
        "alternativas": [
            "Os pneus da Fórmula E são recicláveis",
            "Os pneus da Fórmula E são maiores",
            "Os pneus da Fórmula E são menos duráveis",
        ],
        "resposta_idx": 0,
    },
    {
        "pergunta": "Como a Fórmula E influencia o mercado de veículos elétricos de consumo?",
        "alternativas": [
            "Diminui o interesse em veículos elétricos",
            "Promove a aceitação e o desenvolvimento de veículos elétricos",
            "Não tem impacto no mercado de veículos elétricos",
        ],
        "resposta_idx": 1,
    },
]

pontos = 0


def input_int(prompt: str, somar_ao_input: int = 0):
    valor = input(prompt)
    while not valor.isnumeric():
        limpar_console()
        print("\033[31m(x) Digite um inteiro válido\033[0m")
        valor = input(prompt)

    return int(valor) + somar_ao_input


def forcar_indice_resposta_na_lista(input_fn, input_prompt, lista):
    resposta = input_fn(input_prompt)

    while resposta not in lista:
        limpar_console()
        print("\033[31m(x) Digite uma alternativa que esteja na lista\033[0m")
        resposta = input_fn(input_prompt)
    return resposta


def exibir_pergunta_e_pegar_indice_resposta(pergunta, alternativas, resposta):
    prompt = f"(?) {pergunta}\n"

    for i, alt in enumerate(alternativas, 1):
        prompt += f"    {i} - {alt}\n"
    prompt += "> "
    idx_resposta_usuario = (
        forcar_indice_resposta_na_lista(
            input_int, prompt, range(1, len(alternativas) + 1)
        )
        - 1
    )

    return idx_resposta_usuario


def limpar_console():
    sys("cls||clear")


def embaralhar_lista(lista):
    # Utiliza o algoritmo Fisher–Yates para embaralhar a lista
    n = len(lista)

    for i in range(n):
        j = random.randint(i, n - 1)
        lista[i], lista[j] = lista[j], lista[i]
    return lista


embaralhar_lista(quiz)

for pergunta in quiz:
    idx_resposta_usuario = exibir_pergunta_e_pegar_indice_resposta(
        pergunta["pergunta"], pergunta["alternativas"], pergunta["resposta_idx"]
    )
    limpar_console()

    if idx_resposta_usuario == pergunta["resposta_idx"]:
        pontos += 1
        print("\033[32m[+] Você acertou a pergunta anterior :)\033[0m")
    else:
        print("\033[31m[=] Você errou a pergunta anterior :(\033[0m")

print(
    f"[!] Parabéns por concluir o Quiz! Você fez {pontos} pontos de {len(quiz)} possíveis"
)
