import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


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
columns = st.columns(2)  

# Dados das habilidades
habilidades = {
    'Python': 90,
    'Streamlit': 80,
    'Git': 75,
    'Django': 85,
    'RPA': 70,
}

# Cria a figura e o eixo do matplotlib
fig, ax = plt.subplots()

# Cria as barras horizontais
ax.barh(range(len(habilidades)), list(habilidades.values()), color='skyblue')

# Define os rótulos y como os nomes das habilidades
ax.set_yticks(range(len(habilidades)))
ax.set_yticklabels(list(habilidades.keys()))

# Define os limites x entre 0 e 100
ax.set_xlim([0, 100])

# Remove os contornos do gráfico
for spine in ax.spines.values():
    spine.set_visible(False)

# Remove os ticks do eixo x
ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

# Adiciona as etiquetas de valor em cada barra
for i, v in enumerate(habilidades.values()):
    ax.text(v, i, f' {v}', color='black', va='center')

# Título do gráfico
#ax.set_title('Minhas Habilidades')

# Mostra o gráfico no Streamlit
columns[1].pyplot(fig)


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
