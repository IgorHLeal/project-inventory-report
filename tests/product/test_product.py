from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Takamine Jumbo GJ72 CE NT",
        "Takamine",
        "15/10/2010",
        "20/12/2030",
        "TKMNE24122019",
        "Armazenar sempre no case"
    )

    assert product.id == 1
    assert product.nome_do_produto == "Takamine Jumbo GJ72 CE NT"
    assert product.nome_da_empresa == "Takamine"
    assert product.data_de_fabricacao == "15/10/2010"
    assert product.data_de_validade == "20/12/2030"
    assert product.numero_de_serie == "TKMNE24122019"
    assert product.instrucoes_de_armazenamento == "Armazenar sempre no case"
