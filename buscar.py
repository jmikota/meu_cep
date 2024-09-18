import streamlit as st
import requests
def busca_cep(cep):
    resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    return resposta

st.set_page_config(
    "Sistema de busca de CEP"
)

st.title('Sistema de Busca de CEP')
st.divider()

menu = st.sidebar
cep = menu.text_input("Digite o CEP:")
botao = menu.button("Pesquisar")

if botao:
    resposta = busca_cep(cep)
    if resposta.status_code == 200:
        st.success("CEP encontrado com sucesso!")
        dados = resposta.json()
        st.write(f"CEP: {dados['cep']}")
        st.write(f"ENDEREÇO: {dados['logradouro']}")
        st.write(f"BAIRRO: {dados['bairro']}")
        st.write(f"CIDADE: {dados['localidade']}")
        st.write(f"ESTADO: {dados['estado']}")
        

    else:
        st.error("O CEP informado é invalido!")



#{
#"cep":"84020-120"
#"logradouro":"Rua Professora Alzira Braga Ribas"
#"complemento":""
#"unidade":""
#"bairro":"Neves"
#"localidade":"Ponta Grossa"
#"uf":"PR"
#"estado":"Paraná"
#"regiao":"Sul"
#"ibge":"4119905"
#"gia":""
#"ddd":"42"
#"siafi":"7777"
#}