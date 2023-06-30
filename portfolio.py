import streamlit as st
import pandas as pd

# Título do portfólio
st.title("Portfólio de Mauro Alves")
st.divider()
# Informações de contato
st.write("Entre em contato:")
st.write("📩: mauro.mn@hotmail.com")

# Sobre você
st.header("Sobre mim")
st.write("""
Sou um desenvolvedor Python apaixonado por aprendizado de máquina e ciência de dados.
Tenho experiência em várias bibliotecas e ferramentas, incluindo Streamlit, Pandas, 
Scikit-Learn e TensorFlow.
""")

# Habilidades
st.header("Habilidades")
columns = st.columns(3)  
columns[0].button("Python")  
columns[1].button("Streamlit")  
columns[2].button("Machine Learning")

# Educação
st.header("Educação")
df = pd.DataFrame({
    'Instituição': ['Universidade Paulista'],
    'Grau': ['Superior Completo'],
    'Anos': ['2020 - 2023']
})
st.table(df)

# Projetos
st.header("Projetos")
with st.expander('Video Converter Online'):
    st.write("Descrição do projeto")
    sr.write("Este projeto consiste em uma aplicação web desenvolvida com a biblioteca Streamlit em Python, projetada para converter arquivos de vídeo em áudio. A ferramenta aceita tanto uploads de arquivos locais em múltiplos formatos, como MP4, MOV, AVI, FLV, WMV, quanto a inserção de links do YouTube. O usuário, após realizar o upload ou fornecer o link, pode iniciar a conversão com um simples clique. A aplicação fornece feedback durante o processo de conversão e, ao término, disponibiliza o arquivo de áudio resultante para audição e download. Ademais, tooltips informativos estão integrados para auxiliar na compreensão das funcionalidades da aplicação.")
    st.write("[GitHub](https://videoconvert.streamlit.app/)")
    st.image("imagem/1688093912734.jpg")

with st.expander('search Jobs'):
    st.write("Descrição do projeto")
    st.write("[GitHub](https://searchajob.streamlit.app/)")
    st.image("imagem/1688094033319.jpg")

# Realizações
st.header("Realizações")
with st.expander('Nome da Realização'):
    st.write("Descrição da realização")
