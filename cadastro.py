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


#interface

image = open('iclogo.png', 'rb').read()
width = 100

st.image(image,
        caption='',
        width=width,
)

nome = st.text_input("Nome:")
curso = st.selectbox("Curso:", options = ['---', 'Agronomia', 'Administração e Gestão', 'Antropologia', 'Arquitetura', 'Artes Cênicas', 'Artes Plásticas', 'Astronomia', 'Biologia', 'Bioquímica', 'Ciência de Dados e IA', 'Ciência Política', 'Ciências Ambientais', 'Ciências Sociais', 'Comunicação Social', 'Contabilidade', 'Design de Interiores', 'Design de Moda', 'Desenvolvimento de Software', 'Desenvolvimento Web', 'Direito', 'Economia', 'Educação Física', 'Enfermagem', 'Engenharia Aeroespacial', 'Engenharia Civil', 'Engenharia Elétrica', 'Engenharia Mecânica', 'Engenharia Química', 'Farmácia', 'Filosofia', 'Finanças', 'Fisioterapia', 'Física', 'Geografia', 'Geologia', 'Gestão de Recursos Humanos', 'História', 'Jornalismo', 'Letras', 'Línguas', 'Marketing', 'Marketing Digital', 'Matemática', 'Medicina', 'Medicina Veterinária', 'Música', 'Nutrição', 'Odontologia', 'Pedagogia', 'Psicologia', 'Publicidade e Propaganda', 'Química', 'Relações Internacionais', 'Segurança da Informação', 'Serviço Social', 'Sociologia', 'Teologia', 'Turismo'])
hrs_curso = st.number_input("Horas do Curso:", format="%d", step=1)
valor_curso = st.selectbox("Valor do Curso:", options = ['Nada', 'de 0 a 100 R$', '100 a 250 R$', '250 a 500 R$', 'mais de 500 R$'])
