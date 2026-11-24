def cadastrar_produto(produtos: list, contador_produtos: int) -> tuple:
    """
    Função para cadastrar um novo produto na lista de produtos.

    Args:
        produtos (list): Lista de produtos cadastrados.
        contador_produtos (int): Contador de produtos cadastrados.

    Returns:
        tuple: Uma tupla contendo a lista atualizada de produtos e o contador atualizado.
    """
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))

    contador_produtos += 1
    produto = {
        "id": contador_produtos,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    produtos.append(produto)

    print("Produto cadastrado com sucesso!\n")
    return produtos, contador_produtos


def consultar_produtos(produtos: list, contador_produtos: int) -> None:
    """
    Função para listar os produtos cadastrados.

    Args:
        produtos (list): Lista de produtos cadastrados.
        contador_produtos (int): Contador de produtos cadastrados.

    Returns:
        None: Esta função apenas imprime os dados na tela.
    """
    print("\n--- 📦 PRODUTOS CADASTRADOS ---")
    if contador_produtos == 0:
        print("Nenhum produto cadastrado ainda.")
    else:
        for indice, item in enumerate(produtos, start=1):
            print(f"{indice}. {item['nome']} - R$ {item['preco']:.2f} (Qtd: {item['quantidade']})")
        print(f"Total de produtos: {contador_produtos}")
    print("-------------------------------\n")


# --- PROGRAMA PRINCIPAL (MENU DO ERP) ---
lista_produtos = []
total_cadastrados = 0

while True:
    print("=== MENU DO ERP ===")
    print("1 - Cadastrar produto")
    print("2 - Consultar produtos")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        lista_produtos, total_cadastrados = cadastrar_produto(lista_produtos, total_cadastrados)
    elif opcao == "2":
        consultar_produtos(lista_produtos, total_cadastrados)
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.\n")









