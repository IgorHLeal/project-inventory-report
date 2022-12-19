from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, product):
        simple_report = super().generate(product)

        products = Counter(
            value["nome_da_empresa"] for value in product
        )

        result = ""

        for company in products:
            result += f"- {company}: {products[company]}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{result}"
        )
