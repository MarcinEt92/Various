# https://www.youtube.com/watch?v=PXMJ6FS7llk

from BaseMethods import BaseMethods


def print_options():
    print("1. Get simpson html data with pandas")
    print("2. Get football csv data with pandas")
    print("3. Get tables from pdf with camelot")
    print("4. Web automation and web scraping: html tags - XPath")
    print("5. Web automation and web scraping: headless mode")
    print("6. Pivot tables with pandas")
    print("7. Excel Add a bar chart")
    print("8. Automate Whatsapp")
    print("")


def get_and_execute():

    options = {
        1: BaseMethods.get_simpson_html_data_with_pandas,
        2: BaseMethods.get_csv_data_from_website,
        3: BaseMethods.extract_table_from_pdf,
        4: BaseMethods.web_automation,
        5: BaseMethods.web_automation_headless_mode,
        6: BaseMethods.pivot_tables_excel,
        7: BaseMethods.excel_add_bar_chart,
        8: BaseMethods.automate_whatsapp,
    }
    option_number = int(input("Choose: "))
    option = options.get(option_number)
    option()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_options()
    get_and_execute()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
