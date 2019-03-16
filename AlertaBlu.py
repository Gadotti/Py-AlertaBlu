from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path='D:\Sistemas\Python\geckodriver.exe')
driver.get("http://alertablu.cob.sc.gov.br/p/detalhada")
#print('Iniciado...')
for row in driver.find_elements_by_xpath("html/body/div[2]/div/div[2]/div/table/thead"):
    cell = row.find_elements_by_tag_name("th")[1]
    print(cell.text)
    text_file = open("NivelRio.txt", "w")
    text_file.write("Nivel do rio atual: %s" % cell.text)
    text_file.close()
driver.close()
#print('Finalizado...')