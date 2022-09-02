from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Copo_carao",
        "RTLD_GLOBAL",
        "24/12/2022",
        "25/12/2023",
        "696969696969",
        "Armazenar na geladeira",
    )
    string1 = f"O produto {product.nome_do_produto} "
    string2 = f"fabricado em {product.data_de_fabricacao} "
    string3 = f"por {product.nome_da_empresa} com validade "
    string4 = f"até {product.data_de_validade} "
    string5 = f"precisa ser armazenado {product.instrucoes_de_armazenamento}."
    text = string1 + string2 + string3 + string4 + string5
    assert product.__repr__() == text
