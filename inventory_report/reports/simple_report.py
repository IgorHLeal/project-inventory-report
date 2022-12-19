from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, lista):
        oldest_date = min(
            [product["data_de_fabricacao"] for product in lista]
        )

        closest_date = min(
            [product["data_de_validade"] for product in lista]
        )

        company_bigger_stock = Counter(
            [product["nome_da_empresa"] for product in lista]
        ).most_common(1)[0][0]

        # Forma alternativa de encontrar a empresa com mais produtos:
        """ company_bigger_stock = max(
            Counter(product["nome_da_empresa"] for product in lista)
        ) """

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company_bigger_stock}"
        )

# Referências
# most_common()[][]:
    # https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list
