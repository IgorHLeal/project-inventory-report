from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        2,
        "Tagima Dallas Mahogany",
        "Tagima",
        "15/10/2020",
        "20/12/2030",
        "TAGIMA1234567",
        "Armazenar sempre no case"
    )

    assert product.id == 2
    assert product.nome_do_produto == "Tagima Dallas Mahogany"
    assert product.nome_da_empresa == "Tagima"
    assert product.data_de_fabricacao == "15/10/2020"
    assert product.data_de_validade == "20/12/2030"
    assert product.numero_de_serie == "TAGIMA1234567"
    assert product.instrucoes_de_armazenamento == "Armazenar sempre no case"
