import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Título do portfólio
st.title("Portfólio de Seu Nome")

# Informações de contato
st.write("Entre em contato:")
st.write("📧: seuemail@gmail.com")

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

# Dados de exemplo para a visualização
df = pd.DataFrame({
    'Instituição': ['Universidade Paulista'],
    'Grau': ['Superior Completo'],
    'Curso':['Análise e Desenvolvimento de Sistemas'],
    'Ano': ['2020 - 2023']
})

# Criando a figura com a visualização
fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='#3f7f93',
                font_color='white',
                align='center'),
    cells=dict(values=[df.Instituição, df.Grau, df.Curso, df.Ano],
               fill_color='lightcyan',
               align='center'))
])

# Configurando o layout da figura
fig.update_layout(
    width=600,
    height=200,
    margin=dict(l=20, r=20, t=20, b=20),
)

# Renderizando a figura
st.plotly_chart(fig, use_container_width=True)

st.divider()

# Projetos
st.header("Projetos Principais")
with st.expander('Video Converter Online'):
    st.write("Descrição do projeto")
    st.write("Acesse o [App](https://videoconvert.streamlit.app/)")
    st.image("imagem/IMG_20230630_114522.jpg")

with st.expander('search Jobs'):
    st.write("Descrição do projeto")
    st.write("Acesse o [App](https://searchajob.streamlit.app/)")
    st.image("imagem/IMG_20230630_155903.jpg")

st.divider()

st.markdown("Developed by: Mauro Alves")
