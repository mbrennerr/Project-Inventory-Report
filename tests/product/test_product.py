from inventory_report.inventory.product import Product


def test_cria_produto():

    product = Product(
        1,
        "Copo_carao",
        "RTLD_GLOBAL",
        "24/12/2022",
        "25/12/2023",
        "696969696969",
        "Armazenar na geladeira",
    )
    assert product.id == 1
    assert product.nome_do_produto == "Copo_carao"
    assert product.nome_da_empresa == "RTLD_GLOBAL"
    assert product.data_de_fabricacao == "24/12/2022"
    assert product.data_de_validade == "25/12/2023"
    assert product.numero_de_serie == "696969696969"
    assert product.instrucoes_de_armazenamento == "Armazenar na geladeira"
