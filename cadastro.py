import streamlit as st
import pyodbc

#conexao banco de dados
def conectar_bd():
    dados_conexao = (
        "Driver={SQL Server};"
        "Server=Bauer;"
        "Database=IC;"
    )
    conexao = pyodbc.connect(dados_conexao)
    return conexao

#inserir os dados na tabela de cursos
def inserir_dados(nome, curso, hrs_curso, valor_curso):
    conexao = conectar_bd()
    cursor = conexao.cursor()
    comando = f"""
    INSERT INTO cadastro (nome, curso, hrs_curso, valor_curso)
    VALUES ('{nome}', '{curso}', '{hrs_curso}', '{valor_curso}')
    """
    cursor.execute(comando)
    cursor.commit()
    cursor.close()
    conexao.close()