import openpyxl


class TestData():
    CHROME_EXECUTABLE_PATH = r"C:\Users\rfnsh\PycharmProjects\WhatsappWebUiAutomation\utilites\chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = r"C:\Users\rfnsh\PycharmProjects\WhatsappWebUiAutomation\utilites\geckodriver.exe"
    EXCEL_EXECUTABLE_PATH = r"C:\Users\rfnsh\PycharmProjects\WhatsappWebUiAutomation\assets\test.xlsx"
    BASE_URL = "https://web.whatsapp.com/"
    SEARCH_TERM = "Sample"
    _404 = "Check your connection"
    HOME_PAGE_TITLE = "Whatsapp"
    NO_RESULTS_TEXT = "No results found."
    data_load = openpyxl.load_workbook(EXCEL_EXECUTABLE_PATH)
    sheet = data_load['Sheet1']
    SAMPLE_DATA = sheet['A2'].value
