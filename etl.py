import pandas as pd
import os
import glob
from utils_log import log_decorator

@log_decorator
# funcao de extract que le e consolida json
def extrair_dados_consolida(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

@log_decorator
# fucao que transforma
def calculo_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"]*df["Venda"]
    return df

@log_decorator
# funcao que da load em csv ou parquet
def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    parametro que vai sair ou csv ou parquet ou os dois
    """
    if "csv" in format_saida:
        df.to_csv("dados.csv")
    if "parquet" in format_saida:
        df.to_parquet("dados.parquet")

@log_decorator
def pipeline_calcular_kpi_vendas_consolidado(pasta: str, format_saida: list):
    dataframe = extrair_dados_consolida(pasta=pasta)
    dataframe_calculado = calculo_total_vendas(dataframe)
    carregar_dados(dataframe_calculado, format_saida)
