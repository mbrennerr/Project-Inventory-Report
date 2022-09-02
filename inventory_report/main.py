import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():

    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")
    else:
        path = sys.argv[1]
        type = sys.argv[2]

        importer = ""
        if path.endswith(".csv"):
            importer = CsvImporter
        elif path.endswith(".json"):
            importer = JsonImporter
        elif path.endswith(".xml"):
            importer = XmlImporter

        relatory = InventoryRefactor(importer)
        print(relatory.import_data(path, type), end="")
        return relatory.import_data(path, type)
