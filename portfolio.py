import streamlit as st
import pandas as pd

# Título do portfólio
st.divider()
st.image("imagem/IMG_20230630_151247.png")

st.divider()

# Sobre você 
st.header("Sobre mim")
st.write("""
👨🏻‍🎓 Sou formado em Análise e Desenvolvimento de Sistemas e tenho um forte compromisso em me manter atualizado e aprimorar minhas habilidades constantemente. 

📕Além da minha formação acadêmica, busco constantemente cursos e treinamentos complementares para me aprofundar em áreas específicas. Também aplico meus conhecimentos em exercícios e projetos pessoais para testar minhas habilidades práticas.

Estou entusiasmado em encontrar oportunidades para aplicar meu conhecimento e experiência no campo do desenvolvimento de software. Meu objetivo é contribuir com soluções inovadoras e fazer parte de equipes dinâmicas que impulsionem o crescimento e a excelência tecnológica. Estou aberto a desafios estimulantes e estou sempre pronto para aprender e me adaptar às demandas do setor em constante evolução.
""")

st.divider()

# Habilidades
st.header("Habilidades")
columns = st.columns(5)  
columns[0].button("Python")  
columns[1].button("Streamlit")  
columns[2].button("Git")
columns[3].button("Django")
columns[4].button("RPA")

st.divider()

# Educação
st.header("Educação")
df = pd.DataFrame({
    'Instituição': ['Universidade Paulista'],
    'Grau': ['Superior Completo'],
    'Curso':['Análise e Desenvolvimento de Sistemas'],
    'Ano': ['2020 - 2023']
})
st.table(df)

st.divider()

# Projetos
st.header("Projetos")
with st.expander('Video Converter Online'):
    st.write("Descrição do projeto")
    st.write("[App](https://videoconvert.streamlit.app/)")
    st.divider()
    st.write("""
    Este projeto consiste em uma aplicação web desenvolvida com a biblioteca Streamlit em Python,
    projetada para converter arquivos de vídeo em áudio. A ferramenta aceita tanto uploads de arquivos locais em múltiplos formatos, como MP4, MOV, AVI, FLV, WMV, quanto a inserção de links do  YouTube.
    O usuário, após realizar o upload ou fornecer o link, pode iniciar a conversão com um simples clique.
    A aplicação fornece feedback durante o processo de conversão e, ao término, disponibiliza o arquivo de áudio resultante para audição e download. 
    Ademais, tooltips informativos estão integrados para auxiliar na compreensão das funcionalidades da aplicação.""")
    st.divider()
    st.image("imagem/IMG_20230630_114522.jpg")

with st.expander('search Jobs'):
    st.write("Descrição do projeto")
    st.write("[App](https://searchajob.streamlit.app/)")
    st.image("imagem/IMG_20230630_155903.jpg")

st.divider()

# Realizações
#st.header("Realizações")
#with st.expander('Nome da Realização'):
    #st.write("Descrição da realização")
