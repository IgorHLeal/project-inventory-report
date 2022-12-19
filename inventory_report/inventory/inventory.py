from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(self, path, type):
        if 'csv' in path:
            return Inventory().open_csv(path, type)
        elif 'json' in path:
            return Inventory().open_json(path, type)
        elif 'xml' in path:
            return Inventory().open_xml(path, type)
        raise ValueError()

    # Conteúdo do dia 1.2
    @classmethod
    def open_csv(self, path, type):
        with open(path, encoding="utf-8") as file:
            inventory_file = csv.DictReader(file, delimiter=",", quotechar='"')
            if type == "simples":
                return SimpleReport().generate(list(inventory_file))
            elif type == "completo":
                return CompleteReport().generate(list(inventory_file))
            else:
                raise ValueError

    @classmethod
    def open_json(self, path, type):
        with open(path, 'r') as file:
            inventory_file = json.load(file)
            if type == "simples":
                return SimpleReport().generate(list(inventory_file))
            elif type == "completo":
                return CompleteReport().generate(list(inventory_file))
            else:
                raise ValueError

    # Install xmltodict: https://pypi.org/project/xmltodict/
    # Using xmltodict: https://docs.python-guide.org/scenarios/xml/
    # https://docs.python-guide.org/scenarios/xml/
    # https://acervolima.com/ler-e-escrever-arquivos-xml-em-python/
    @classmethod
    def open_xml(self, path, type):
        with open(path) as file:
            inventory_file = xmltodict.parse(file.read())["dataset"]["record"]
            if type == "simples":
                return SimpleReport().generate(list(inventory_file))
            elif type == "completo":
                return CompleteReport().generate(list(inventory_file))
            else:
                raise ValueError
