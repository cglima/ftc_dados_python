import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="🍲"
)

# image_path = "/home/ciana/repositorios/ftc_dados_python/"
image = Image.open('indian-curry.png')
st.sidebar.image(image, width=120)

st.sidebar.markdown('# Curry Company')
st.sidebar.markdown('## Fastest Delivery in Town')
st.sidebar.markdown("""---""")

st.write(' # Curry Company Growth Dashboard')

st.markdown(
    """
    Grwth Dashboard foi construído para acompanhar as métricas de crescimento dos Entregadores e Restaurantes.
    ### Como utilizar esse Growth Dashboard?
    - Visão Empresa:
        - Visão Gerencial: Métricas gerais de comportamento
        - Visão Tática: Indicadores semanais de crescimento
        - Visão Gepgráfica: Insights de geolocalização
    - Visão Entregador:
        - Acompanhamento dos indicadores semanais de crescimento
    - Visão Restaurantes:
        - Indicadores semanais de crescimento dos restaurantes
    """
)

st.sidebar.markdown("### Powered by Comunidade DS")