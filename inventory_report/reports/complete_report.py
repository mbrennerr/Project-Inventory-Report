from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def list_all_manufactures(cls, inventory):
        result = super().get_all_manufactures(inventory)

        return "".join(
            [(f"- {company}: {result[company]}\n") for company in result]
        )

    @classmethod
    def generate(cls, inventory, option=None) -> str:
        oldest_fabrication_date = cls.filter_by_oldest_fabrication(inventory)
        expiration_date = cls.filter_by_expiration_date(inventory)
        companies_name = cls.filter_manufacturer_by_max_product(inventory)
        companies_products = cls.list_all_manufactures(inventory)

        return (
            f"Data de fabricação mais antiga: {oldest_fabrication_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com mais produtos: {companies_name}\n"
            f"Produtos estocados por empresa:\n{companies_products}"
        )
