from cx_Freeze import setup, Executable
import sys

# Adiciona o caminho do Python
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Configurações do cx_Freeze
options = {
    'build_exe': {
        'packages': ['selenium', 'openpyxl', 'psycopg2', 'datetime'],
        'excludes': ['tkinter'],
        'include_files': []  # Você pode incluir outros arquivos aqui se necessário
    }
}

executables = [
    Executable('cotacao.py', base=base)
]

setup(
    name='CotacaoDolar',
    version='0.1',
    description='Script para capturar a cotação do dólar e inserir no PostgreSQL',
    options=options,
    executables=executables
)
