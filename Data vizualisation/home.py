import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from pyvis.network import Network
from IPython.display import display,HTML
import pandas as pd
import streamlit.components.v1 as components
import random
import matplotlib.colors as mcolors

st.set_page_config(page_title="Data_Viz_ola",layout="wide")
# style
#with open('style.css')as f:
    #st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
theme_plotly = None 

def unique_list(oldlist):
    new_list = []

    for component in oldlist:
        if component not in new_list:
            new_list.append(component)

    return new_list

def merge(list1,list2):
    merged_list = [(list1[i],list2[i]) for i in range(0,len(list1))]
    return merged_list

def generate_colors(list1):
    colors_list = []
    for i in range(0,len(list1)):
        color = random.choice(list(mcolors.CSS4_COLORS.keys()))
        colors_list.append(color)

    return colors_list

def network_gen_3edges(node1,color1,node2,node3,edge1,edge2,edge3):
    net = Network(
        bgcolor="black",
        font_color="yellow",
        directed=True,
        cdn_resources='remote',
        
    )
    net.add_nodes(node1, color=color1)
    net.add_nodes(node2)
    net.add_nodes(node3)
    net.add_edges(edge1)
    net.add_edges(edge2)
    net.add_edges(edge3)
    net.save_graph("node.html")
    Html_file = open("node.html", 'r', encoding='utf-8')
    source_code= Html_file.read()
    return components.html(source_code,height=1000,width=1400)

def network_gen_2edges(node1,color1,node2,edge1):
    net = Network(
        bgcolor="black",
        font_color="yellow",
        directed=True,
        cdn_resources='remote',
        
    )
    net.add_nodes(node1, color = color1)
    net.add_nodes(node2)
    net.add_edges(edge1)
    net.save_graph("node.html")
    Html_file = open("node.html", 'r', encoding='utf-8')
    source_code= Html_file.read()
    return components.html(source_code,height=1000,width=1400)

def network_gen_2nodes_2edges(node1,node2,edge1,edge2):
    net = Network(
        bgcolor="black",
        font_color="yellow",
        directed=True,
        cdn_resources='remote',
        
    )
    net.add_nodes(node1)
    net.add_nodes(node2)
    net.add_edges(edge1)
    net.add_edges(edge2)
    net.save_graph("node.html")
    Html_file = open("node.html", 'r', encoding='utf-8')
    source_code= Html_file.read()
    return components.html(source_code,height=1000,width=1400)

st.header("Ola Data Visualisation")
data= pd.read_csv("ola_data.csv")
cat = (data['category'])
gen = (data['gender'])
booking_id = (data['booking_id'])
Trip_cost = (data['total_trip_cost'])
distance_tra = (data['distance_travelled'])

new_distance=[]
for x in distance_tra:
    if x>20:
        new_distance.append(20)
    if x>20 and x<40:
        new_distance.append(40)
    if x>40 and x<60:
        new_distance.append(60)
    if x>60 and x<100:
        new_distance.append(80)

unique_new_dist = unique_list(new_distance)
dist_color = generate_colors(unique_new_dist)

tuple_cat_dist = merge(unique_new_dist,cat)


rounded_trip_cost = []
for x in Trip_cost:
        rounded_trip_cost.append(round(x))



new_cat = unique_list(cat)
new_gen = unique_list(gen)
new_booking = unique_list(booking_id)

gen_color = generate_colors(new_gen)
cat_color = generate_colors(new_cat)

tuple_cat_gen = merge(cat,gen)
tuple_cat_cost = merge(rounded_trip_cost,cat)

tab1,tab2,tab3= st.tabs(["Category-Gender correlation","Category-Trip Cost correlation","Category-Distance travelled Correlation"])
with tab1:
    st.markdown("##")
    network_gen_2edges(new_cat,cat_color,new_gen,tuple_cat_gen)

with tab2:
    st.markdown("##")
    network_gen_2edges(new_cat,cat_color,rounded_trip_cost,tuple_cat_cost)

with tab3:
    st.markdown("##")
    network_gen_2edges(new_cat,cat_color,unique_new_dist,tuple_cat_dist)


hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer{visibility: hidden;}
        </style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
