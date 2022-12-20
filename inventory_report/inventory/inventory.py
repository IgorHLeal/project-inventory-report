from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(self, path, tipo):
        if 'csv' in path:
            return Inventory.open_csv(path, tipo)
        elif 'json' in path:
            return Inventory.open_json(path, tipo)
        elif 'xml' in path:
            return Inventory.open_xml(path, tipo)
        else:
            raise ValueError("Arquivo inválido")

    # Conteúdo do dia 1.2
    @classmethod
    def open_csv(self, path, tipo):
        with open(path, encoding="utf-8") as file:
            inventory_file = csv.DictReader(file, delimiter=",", quotechar='"')
            if tipo == "simples":
                return SimpleReport.generate(list(inventory_file))
            elif tipo == "completo":
                return CompleteReport.generate(list(inventory_file))
            else:
                raise ValueError("Tipo inválido")

    @classmethod
    def open_json(self, path, tipo):
        with open(path) as file:
            inventory_file = json.load(file)
            if tipo == "simples":
                return SimpleReport.generate(list(inventory_file))
            elif tipo == "completo":
                return CompleteReport.generate(list(inventory_file))
            else:
                raise ValueError("Tipo inválido")

    @classmethod
    def open_xml(self, path, tipo):
        with open(path) as file:
            inventory_file = xmltodict.parse(file.read())["dataset"]["record"]
            if tipo == "simples":
                return SimpleReport.generate(list(inventory_file))
            elif tipo == "completo":
                return CompleteReport.generate(list(inventory_file))
            else:
                raise ValueError("Tipo inválido")


# Install xmltodict: https://pypi.org/project/xmltodict/
# Using xmltodict: https://docs.python-guide.org/scenarios/xml/
# https://docs.python-guide.org/scenarios/xml/
# https://acervolima.com/ler-e-escrever-arquivos-xml-em-python/
