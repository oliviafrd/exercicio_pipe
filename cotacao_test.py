# RPA cotação dólar
from selenium import webdriver
from datetime import datetime
from time import sleep
from selenium.webdriver.edge.options import Options 
from selenium.webdriver.common.by import By
import psycopg2

edge_options = Options()
edge_options.add_argument("--headless")

driver = webdriver.Edge(options=edge_options)

driver.get(r'https://www.bing.com/search?pglt=41&q=dolar+hoje&cvid=09d5f7d3b3af475c8d1ca428200bc31f&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgYICBAAGEAyBwgJEEUY_FXSAQgxODY4ajBqMagCALACAA&FORM=ANNAB1&PC=HCTS')
sleep(5)

#pegando cotação
findDolar = driver.find_element(By.ID, 'cc_tv')
getDolar = findDolar.get_attribute('value')
cotacao_dolar = float(getDolar.replace(",", "."))
data = datetime.now()
print("\33[32mCotação achada com sucesso!\33[m")

# Conexão com o postgres
db_config = {
    'dbname': 'dbCotacoes',
    'user': 'avnadmin',
    'password': 'AVNS_W0DLm7wJjB9lcgsIoPF',
    'host': 'postgresaiven-project-first.e.aivencloud.com',
    'port': '23957'  
}

#criar conexão
conn = psycopg2.connect(**db_config)
print("\33[32mConexão bem sucedida!\33[m")

#criando um cursor
cur = conn.cursor()

# executando a query
cur.execute("CALL inserir_cotacao(%s, %s, %s)", (data.date(), data.time(), cotacao_dolar))
# Commit da transação 
conn.commit()
print("\33[32mProcedimento inserir_cotacao chamado com sucesso!\33[m")

# Fechar a conexão
conn.close()
print("\33[31mConexão encerrada!\33[m")
