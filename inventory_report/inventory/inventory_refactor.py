from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def report_type_selector(cls, report, report_type):
        simple_report = SimpleReport
        complete_report = CompleteReport
        if report_type == "simples":
            return simple_report.generate(report)
        elif report_type == "completo":
            return complete_report.generate(report)
        else:
            raise ValueError()

    def import_data(self, file, report_type):
        self.data += self.importer.import_data(file)
        report = self.report_type_selector(self.data, report_type)
        return report

    def __iter__(self):
        return InventoryIterator(self.data)
