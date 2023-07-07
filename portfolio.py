import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuração da página
#st.set_page_config(layout="wide")

# Título do portfólio
st.divider()

st.image("imagem/IMG_20230703_120107.png")

st.markdown("""
    <a href="https://github.com/Maurynn" target="_blank" style="margin-right: 15px; text-decoration: none">
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="Github logo" width="25" height="25">
    </a>
    <a href="https://linkedin.com/in/maurosp" target="_blank" style="margin-right: 15px; text-decoration: none">
        <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" alt="LinkedIn logo" width="25" height="25">
    </a>
    <a href="https://instagram.com/maurinn?igshid=ZDc4ODBmNjlmNQ==" target="_blank" style="margin-right: 15px; text-decoration: none">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram logo" width="25" height="25">
    </a>
    <a href="https://wa.me/5511952483074" target="_blank" style="margin-right: 15px; text-decoration: none">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp logo" width="25" height="25">
    </a>
""", unsafe_allow_html=True)

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
    'Ano': ['2020 - 2023'],
    font_size=12
})

# Criando a figura com a visualização
fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='#3f7f93',
                font_color='white',
                align='center'),
    cells=dict(values=[df.Instituição, df.Grau, df.Curso, df.Ano],
               fill_color='lightcyan',
               align='center',
               font_size=14))
])

# Configurando o layout da figura
fig.update_layout(
    width=650,
    height=150,
    margin=dict(l=0, r=0, t=20, b=20),
)

# Renderizando a figura
st.plotly_chart(fig, use_container_width=True)

st.divider()

# Projetos
st.header("Projetos Principais")
with st.expander('Video Converter Online'):
    st.write("Descrição do projeto")
    st.write("Acesse o [App](https://videoconvert.streamlit.app/)")
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
    st.write("Acesse o [App](https://searchajob.streamlit.app/)")
    st.divider()
    st.write("""
    Buscador de Vagas para Desenvolvedores (Streamlit)

    Esta aplicação web, criada com Python e Streamlit, permite que desenvolvedores pesquisem vagas de emprego em tempo real. 
    Utilizando a API do Adzuna, a aplicação retorna uma lista de vagas baseadas nas habilidades e localização inseridas pelo usuário. 
    Além disso, a aplicação analisa as descrições das vagas e gera uma nuvem de palavras com as habilidades mais requisitadas, 
    fornecendo um vislumbre das tendências do mercado. Também utiliza a biblioteca Pygments para realçar trechos de código nas descrições das vagas, melhorando a legibilidade.""")
    st.image("imagem/IMG_20230630_155903.jpg")
    
    st.divider()

    st.markdown("Developed by: Mauro Alves")

# Realizações
#st.header("Realizações")
#with st.expander('Nome da Realização'):
    #st.write("Descrição da realização")
            
