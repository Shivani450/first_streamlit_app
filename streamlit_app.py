import streamlit 
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🍧Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show=my_fruit_list.loc[fruits_selected] 


streamlit.dataframe(fruits_to_show)

##import requests 
##fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + "watermelon") 
##streamlit.text(fruityvice_response)

#streamlit.header("Fruityvice Fruit Advice!")
#import requests
#fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json())


##fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
##streamlit.dataframe(fruityvice_normalized)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','apple')
streamlit.write('The user entered ', fruit_choice)

import requests 
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) 
streamlit.text(fruityvice_response)
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

#fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_normalized)
#fruit_choice=streamlit.text_input('What fruit would you like information about?','apple') 
#streamlit.write('The user entered',fruit_choice) 
#import requests
####fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())

#streamlit.dataframe(fruityvice_normalized)


import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)



fruit_choice = streamlit.text_input('What fruit would you like to add?','apple')
streamlit.write('Thanks for adding', fruit_choice)

#import requests 
#fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) 
#streamlit.text(fruityvice_response)
#fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_normalized)
