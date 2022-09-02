import xmltodict
import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def csv_reader(cls, path: str) -> list:
        with open(path, "r", encoding="utf-8") as file:
            file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(file_reader)

    @classmethod
    def json_reader(cls, path: str) -> list:
        with open(path, "r", encoding="utf-8") as file:
            file_reader = json.load(file)
            return file_reader

    @classmethod
    def xml_reader(cls, path: str) -> dict:
        with open(path, "r", encoding="utf-8") as file:
            # my_xml = file.read()
            file_reader = xmltodict.parse(file.read())
            return file_reader["dataset"]["record"]
        # xmltodict refenrence:https://www.askpython.com/python-modules/
        # xmltodict-module

    @classmethod
    def select_reader(cls, path: str) -> list:
        if path.endswith(".csv"):
            return cls.csv_reader(path)
        elif path.endswith(".json"):
            return cls.json_reader(path)
        elif path.endswith(".xml"):
            return cls.xml_reader(path)
        else:
            raise Exception("File type not supported")

    @classmethod
    def import_data(cls, path, report_type):
        simple_report = SimpleReport
        complete_report = CompleteReport
        data = cls.select_reader(path)
        if report_type == "simples":
            return simple_report.generate(data)
        elif report_type == "completo":
            return complete_report.generate(data)

        else:
            raise Exception("Report type not supported")
