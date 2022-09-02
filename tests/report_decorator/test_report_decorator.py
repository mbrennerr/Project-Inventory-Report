from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.inventory.product import Product

BLUE = "\033[36m"
BLEACH = "\033[0m "
GREEN = "\033[32m"
RED = "\033[31m"


def get_products():
    product = Product(
        "3",
        "NITROUS OXIDE",
        "Galena Biopharma",
        "2020-12-22",
        "2024-11-07",
        "CZ09 8588 0858 8435 9140 2695",
        "instrucao 3",
    ).__dict__
    return [product]


def test_decorar_relatorio():
    products = get_products()
    color_report = ColoredReport(SimpleReport).generate(products)
    line_break = color_report.split("\n")

    assert line_break[0].startswith(f"{GREEN}")
    space = line_break[0].split(f"{BLEACH}")
    assert space[1].startswith(f"{BLUE}")

    assert line_break[1].startswith(f"{GREEN}")
    space = line_break[0].split(f"{BLEACH}")
    assert space[1].startswith(f"{BLUE}")

    assert line_break[2].startswith(f"{GREEN}")
    space = line_break[2].split(f"{BLEACH}")
    assert space[1].startswith(f"{RED}")
