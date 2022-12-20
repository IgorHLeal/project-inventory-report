from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, productsList):
        simple_report = SimpleReport.generate(productsList)

        company_stock = {}

        for value in productsList:
            if value["nome_da_empresa"] in company_stock:
                company_stock[value["nome_da_empresa"]] += 1
            else:
                company_stock[value["nome_da_empresa"]] = 1

        result = ""

        for key, value in company_stock.items():
            result += f"- {key}: {value}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{result}"
        )


# Referencias:
# https://stackoverflow.com/questions/10756427/loop-through-all-nested-dictionary-values
