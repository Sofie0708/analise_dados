import streamlit as st
import pandas as pd

# Título e cabeçalho da aplicação
st.title("Padaria Pão Quentinho")
st.header("Faça seu pedido online")
st.subheader("Seja bem-vindo!")


cliente = st.text_input("Qual o seu nome?")
if cliente:
    st.write(f"Olá, **{cliente}**! Monte o seu pedido abaixo:")

st.subheader("Cardápio do dia")
cardapio_df = pd.DataFrame({
    "Item": ["Pão Francês (unid)", "Pão de Queijo (unid)", "Café com Leite", "Bolo de Cenoura (fatia)", "Suco Natural"],
    "Preço (R$)": [1.00, 3.50, 4.50, 6.00, 7.00]
})
st.dataframe(cardapio_df)


precos = {
    "Pão Francês (unid)": 1.00,
    "Pão de Queijo (unid)": 3.50,
    "Café com Leite": 4.50,
    "Bolo de Cenoura (fatia)": 6.00,
    "Suco Natural": 7.00
}

st.subheader("🛒 Monte o seu Pedido")

with st.form("form_pedidos"):
    itens_selecionados = st.multiselect(
        "Escolha os produtos que deseja comprar:",
        list(precos.keys())
    )
    
    opcao_entrega = st.selectbox("Forma de consumo/retirada:", ["Comer no local", "Retirar na loja", "Entrega"])
    submit = st.form_submit_button("Calcular Total")


if submit:
    if not itens_selecionados:
        st.warning("Por favor, selecione pelo menos um item para calcular!")
    else:
        st.success("Pedido gerado com sucesso!")
        
        col_res1, col_res2 = st.columns([2, 1])
        
        total = sum([precos[item] for item in itens_selecionados])
        
        with col_res1:
            st.write("### Itens Selecionados:")
            for item in itens_selecionados:
                st.write(f"- {item}: R$ {precos[item]:.2f}")
            st.write(f"**Opção escolhida:** {opcao_entrega}")
            
        with col_res2:
            st.subheader("Total:")
            st.title(f"R$ {total:.2f}")

