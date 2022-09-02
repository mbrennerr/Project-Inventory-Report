class SimpleReport:
    @classmethod
    def filter_by_oldest_fabrication(cls, inventory: list) -> str:
        return min(
            [fabrication["data_de_fabricacao"] for fabrication in inventory]
        )

    @classmethod
    def filter_by_expiration_date(cls, inventory: list) -> str:
        return min(
            [fabrication["data_de_validade"] for fabrication in inventory]
        )

    @classmethod
    def filter_manufacturer_by_max_product(cls, inventory: list) -> str:
        result = cls.get_all_manufactures(inventory)
        return max(result, key=result.get)

    @classmethod
    def get_all_manufactures(cls, inventory: list) -> dict:
        COMPANIES_NAMES = [
            fabrication["nome_da_empresa"] for fabrication in inventory
        ]

        result = {}
        for company in COMPANIES_NAMES:
            if company not in result:
                result[company] = 1
            else:
                result[company] += 1
        return result

    @classmethod
    def generate(cls, inventory: list) -> str:
        oldest_fabrication = cls.filter_by_oldest_fabrication(inventory)
        expiration_date = cls.filter_by_expiration_date(inventory)
        companies_name = cls.filter_manufacturer_by_max_product(inventory)

        return (
            f"Data de fabricação mais antiga: {oldest_fabrication}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com mais produtos: {companies_name}"
        )
