import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# mostrar todas as colunas da tabela completa
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

# pasta onde o main.py esta
BASE_DIR = Path(__file__).resolve().parent
# caminho completo ate o dataset
arquivo = BASE_DIR / "dataset.csv"

df = pd.read_csv(arquivo)