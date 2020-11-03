import streamlit as st
import plotly.figure_factory as ff
from PIL import Image
import pandas as pd
import numpy as np

showImageFormat = "False"



def ad_calc_profit(price_item, cost_item,unit_sold):
    profit_item = []
    break_even_cnt = 0
    # Calculate profit for each case
    for i in range(len(price_item)):
        # Get all key factors
        unit_price = price_item[i]
        unit_cost = cost_item[i]
        #unit_sold = ad_budget*conversion_rate
        # Calculate total profit
        profit = unit_sold * (unit_price - unit_cost)
        #print("------")
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
    st.title("Advertising Analytics")
    image = Image.open('./image/silvi2.jpg')
    st.image(image,use_column_width=True)

    #% VENDITE LINEA1
    var1=st.number_input('% vendite linea1',value=40,max_value=100,step=1)
    #st.write('il numero selezionato è: ', var1)
    
    var2=st.number_input('% vendite linea2',value=100-var1,max_value=100,step=1)
    #st.write('il numero selezionato è: ', var2)
    
    var3=st.number_input('% vendite linea3',value=100-var1-var2,max_value=100,step=1)
    #st.write('il numero selezionato è: ', var3)
    
    N =5000
    price_item1=[]
    price_item2=[]
    price_item3=[]
    
    
    if var1+var2+var3 ==100:
        st.markdown("La somma delle percentuali è corretta")
    else:
        st.markdown("I numeri corretti non sono corretti, cambiare le proporzioni!!")
    

    if var1 !=0:
        unit_price1 = st.slider(label="Scegliere il prezzo medio unitario linea 1",
                              max_value=50,
                              min_value=10,
                              value=35,
                              step=1)

        unit_cost1 = st.slider(label="Scegliere il costo medio unitario linea 1",
                              max_value=50,
                              min_value=10,
                              value=20,
                              step=1)
        price_item1, cost_item1 = get_items_ad_triangular(unit_price1, unit_cost1, N)
        #hist line1
        hist_data = [price_item1, cost_item1]
        group_label = ['Unit Price line1', 'Unit Cost line1']
        fig = ff.create_distplot(hist_data, group_label, bin_size=[0.5, 0.5], curve_type='normal')
        st.plotly_chart(fig, use_container_width=True)

    if var2 !=0:
        unit_price2 = st.slider(label="Scegliere il prezzo medio unitario linea 2",
                              max_value=50,
                              min_value=10,
                              value=46,
                              step=1)

        unit_cost2 = st.slider(label="Scegliere il costo medio unitario linea 2",
                              max_value=50,
                              min_value=10,
                              value=39,
                              step=1)
        price_item2, cost_item2 = get_items_ad_triangular(unit_price2, unit_cost2, N)
        #hist line2
        hist_data = [price_item2, cost_item2]
        group_label = ['Unit Price line2', 'Unit Cost line2']
        colors = ['rgb(0, 0, 100)', 'rgb(0, 200, 200)']
        fig = ff.create_distplot(hist_data, group_label, bin_size=[0.5, 0.5], curve_type='normal',colors=colors)
        st.plotly_chart(fig, use_container_width=True)

                     
    if var3 !=0:
        unit_price3 = st.slider(label="Scegliere il prezzo medio unitario linea 3",
                              max_value=50,
                              min_value=10,
                              value=35,
                              step=1)

        unit_cost3 = st.slider(label="Scegliere il costo medio unitario linea 3",
                              max_value=50,
                              min_value=10,
                              value=20,
                              step=1)
        price_item3, cost_item3 = get_items_ad_triangular(unit_price3, unit_cost3, N) 
        #hist line3
        hist_data = [price_item3, cost_item3]
        group_label = ['Unit Price line3', 'Unit Cost line3']
        fig = ff.create_distplot(hist_data, group_label, bin_size=[0.5, 0.5], curve_type='normal')
        st.plotly_chart(fig, use_container_width=True)        

    st.markdown("**BUDGET CAMPAGNE MARKETING**")
    st.markdown("Infine, scegliamo il **budget di advertising** per le nostre campagne. Trattasi di un fattore deterministico, poichè dipende esclusivamente da noi")
    ad_budget = st.slider(label="Scegliere l'Advertising Budget",
                          max_value=40000,
                          min_value=1000,
                          value=20000,
                          step=1)

    st.markdown("** CANALI DI MARKETING: **")
    st.markdown("- TV")
    st.markdown("- SEO")
    st.markdown("- ADWORDS")
    st.markdown("- PAPER")
    
    #% LINEAR OPTIMIZATION ADVERTISING BUDGET
    chan1=st.number_input('% BUDGET ON TV',value=15,max_value=100,step=1) 
    chan1_rate = st.slider(label="Impostare la conversion rate TV",
                          max_value=1.00,
                          min_value=0.00,
                          value=0.12,
                          step=0.01)
    chan2=st.number_input('% BUDGET ON SEO',value=100-chan1,max_value=100,step=1)
    chan2_rate = st.slider(label="Impostare la conversion rate SEO",
                          max_value=1.00,
                          min_value=0.00,
                          value=0.09,
                          step=0.01)
    chan3=st.number_input('% BUDGET ON ADWORDS',value=100-chan1-chan2,max_value=100,step=1)
    chan3_rate = st.slider(label="Impostare la conversion rate ADWORDS",
                          max_value=1.00,
                          min_value=0.00,
                          value=0.12,
                          step=0.01)
    chan4=st.number_input('% BUDGET ON PAPER',value=100-chan1-chan2-chan3,max_value=100,step=1)
    chan4_rate = st.slider(label="Impostare la conversion rate PAPER",
                          max_value=1.00,
                          min_value=0.00,
                          value=0.11,
                          step=0.01)
    ## ON TOTAL
    unit_sold_SEO = int(ad_budget*chan1/100*chan1_rate)
    unit_sold_TV  = int(ad_budget*chan2/100*chan2_rate)
    unit_sold_ADWORDS = int(ad_budget/100*chan3*chan3_rate)
    unit_sold_PAPER = int(ad_budget/100*chan4*chan4_rate)
    
    ## ON PROD1
    unit_sold_SEO1 = unit_sold_SEO*var1/100
    unit_sold_TV1  = unit_sold_TV*var1/100
    unit_sold_ADWORDS1 = unit_sold_ADWORDS*var1/100
    unit_sold_PAPER1 = unit_sold_PAPER*var1/100
    unit_sold1 = int(unit_sold_SEO1+unit_sold_TV1+unit_sold_ADWORDS1+unit_sold_PAPER1)
    
    ## ON PROD2
    unit_sold_SEO2 = unit_sold_SEO*var2/100
    unit_sold_TV2  = unit_sold_TV*var2/100
    unit_sold_ADWORDS2 = unit_sold_ADWORDS*var2/100
    unit_sold_PAPER2 = unit_sold_PAPER*var2/100
    unit_sold2 = int(unit_sold_SEO2+unit_sold_TV2+unit_sold_ADWORDS2+unit_sold_PAPER2)
    
    ## ON PROD2
    unit_sold_SEO3 = unit_sold_SEO*var3/100
    unit_sold_TV3  = unit_sold_TV*var3/100
    unit_sold_ADWORDS3 = unit_sold_ADWORDS*var3/100
    unit_sold_PAPER3 = unit_sold_PAPER*var3/100
    unit_sold3 = int(unit_sold_SEO3+unit_sold_TV3+unit_sold_ADWORDS3+unit_sold_PAPER3)  
    
    
    # unit_sold = unit_sold1+unit_sold2+unit_sold3
       
    # profit_item1, prob_profit1 = ad_calc_profit(price_item1, cost_item1,unit_sold1)
    # if var2!=0:
    #     profit_item2, prob_profit2 = ad_calc_profit(price_item2, cost_item1,unit_sold2)
    # if var3!=0:
    #      profit_item3, prob_profit1 = ad_calc_profit(price_item3, cost_item1,unit_sold3)
    ## Image 2
    st.markdown("**Costi dovuti all'aumento della produzione**")

    image = Image.open('./image/Silvi1.jpeg')
    st.image(image,use_column_width=True)

    sales_expense = st.slider(label="Impostare costi extra dovuti alle vendite",
                        max_value=20000,
                        min_value=1000,
                        value=2500,
                        step=100)
    
    marketing_expense = st.slider(label="Costi gestione campagne marketing (h attività, etc)",
                        max_value=20000,
                        min_value=1000,
                        value=1500,
                        step=100)

    if var1!=0 & var2==0 & var3==0:
        profit_item = unit_sold1*(sum(price_item1)/len(price_item1))-sales_expense-marketing_expense
    elif var3!=0 & var2!=0:
        profit_item = unit_sold1*(sum(price_item1)/len(price_item1))+unit_sold2*(sum(price_item2)/len(price_item2))-sales_expense-marketing_expense
    
    #profit_itemz = int(sum(profit_item1) / len(profit_item1))+int(sum(profit_item2)/ len(profit_item2))-sales_expense-marketing_expense
    print(profit_item)
    ROI = (profit_item-ad_budget)/ad_budget*100
    print(ROI)

    #Result
    if st.checkbox(' Mostra i Risultati'):
        #st.markdown(f"Probabilità di break-even (ovvero per generare profitto positivo): **{prob_profit*100: .2f}%**")
        st.markdown(f"La redditività media dell'investimento (ROI) del Marketing Budget: "
                f"**{(profit_item- ad_budget) / (ad_budget)*100: .2f}%**")
                #f"**{(sum(profit_item) / len(profit_item) - ad_budget) *100 / (ad_budget): .2f}%**")
        #st.markdown(f"Utile medio: **€{sum(profit_item1) / len(profit_item1): .2f}**")
        #st.markdown(f"ROI: **{((sum(profit_item1) / len(profit_item1)+sum(profit_item2)/ len(profit_item2))- ad_budget-sales_expense-marketing_expense) *100 / (ad_budget): .2f}**")


if __name__ == "__main__":
    main()