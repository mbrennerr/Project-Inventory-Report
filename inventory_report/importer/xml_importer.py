import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(path, "r", encoding="utf-8") as file:
            my_xml = xmltodict.parse(file.read())
            return my_xml["dataset"]["record"]
