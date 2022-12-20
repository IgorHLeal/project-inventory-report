from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        if 'csv' not in path:
            raise ValueError("Arquivo inválido")
        with open(path, encoding="utf-8") as file:
            inventory_file = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(inventory_file)
