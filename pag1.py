import streamlit as st
import plotly.figure_factory as ff
from PIL import Image
import pandas as pd
import numpy as np

def ad_calc_profit(price_item, cost_item, ad_budget,sales_expense,conversion_rate):
    profit_item = []
    break_even_cnt = 0
    # Calculate profit for each case
    for i in range(len(price_item)):
        # Get all key factors
        unit_price = price_item[i]
        unit_cost = cost_item[i]
        unit_sold = ad_budget*conversion_rate
        # Calculate total profit
        profit = unit_sold * (unit_price - unit_cost) - sales_expense
        ##print("------")
        #print(f"unit sold: {unit_sold}")
        #print(unit_price, unit_cost, profit)

        profit_item.append(profit)

        if profit >= 0.0:
            break_even_cnt += 1
    # Calculate probability of break-even
    prob_profit = break_even_cnt / len(profit_item)
    return profit_item, prob_profit

def get_items_ad_triangular(unit_price, unit_cost, N):
    price_item = np.random.triangular(size=N, left=unit_price-10.0, right=unit_price+10.0, mode=unit_price)
    cost_item = np.random.triangular(size=N, left=unit_cost-5.0, right=unit_cost+10.0, mode=unit_cost)
    return price_item, cost_item


def main():
    # Get the data from url and request it as json file
    st.button("Re-run")
    #st.title("Welcome pagexx")#
    image = Image.open('./image/silvi.jpg')
    st.image(image,use_column_width=True)

    # # #% VENDITE LINEA1
    # var1=st.number_input('% vendite linea1',value=40,max_value=100,step=1)
    # #st.write('il numero selezionato è: ', var1)
    
    # var2=st.number_input('% vendite linea2',value=100-var1,max_value=100,step=1)
    # #st.write('il numero selezionato è: ', var2)
    
    # var3=st.number_input('% vendite linea3',value=100-var1-var2,max_value=100,step=1)
    # #st.write('il numero selezionato è: ', var3)
    
    # if var1+var2+var3 ==100:
        # st.markdown("La somma delle percentuali è corretta")
    # else:
        # st.markdown("I numeri corretti non sono corretti, cambiare le proporzioni!!")
    
    unit_price = st.slider(label="Scegliere il prezzo medio unitario linea 1",
                          max_value=50,
                          min_value=10,
                          value=35,
                          step=1)

    unit_cost = st.slider(label="Scegliere il costo medio unitario linea 1",
                          max_value=40,
                          min_value=10,
                          value=20,
                          step=1)
    N =5000
    conversion_rate1 = 0.23

    price_item, cost_item = get_items_ad_triangular(unit_price, unit_cost, N)
    hist_data = [price_item, cost_item]
    group_label = ['Unit Price1', 'Unit Cost1']
    fig = ff.create_distplot(hist_data, group_label, bin_size=[0.5, 0.5], curve_type='normal')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("Infine, scegliamo il **budget di advertising** per le nostre campagne. Trattasi di un fattore deterministico, poichè dipende esclusivamente da noi")
    ad_budget = st.slider(label="Scegliere l'Advertising Budget",
                          max_value=40000,
                          min_value=1000,
                          value=10000,
                          step=1)

    sales_expense = st.slider(label="Impostare costi extra dovuti alle vendite",
                        max_value=60000,
                        min_value=10000,
                        value=37000,
                        step=1000)

    profit_item, prob_profit = ad_calc_profit(price_item, cost_item, ad_budget,sales_expense,conversion_rate1)

    #Result
    if st.checkbox(' Mostra i Risultati'):
        st.markdown(f"Utile medio: **€{sum(profit_item) / len(profit_item): .2f}**")
        st.markdown(f"Probabilità di break-even (ovvero per generare profitto positivo): **{prob_profit*100: .2f}%**")

        st.markdown(f"La redditività media dell'investimento (ROI) del Marketing Budget: "
                f"**{(sum(profit_item) / len(profit_item) - ad_budget) *100 / (ad_budget): .2f}%**")
        
        hist_data = [profit_item]
        group_label = ['estimated profit']
        fig = ff.create_distplot(hist_data, group_label, bin_size=[3000], curve_type='normal')
        st.plotly_chart(fig, use_container_width=True)  


if __name__ == "__main__":
    main()