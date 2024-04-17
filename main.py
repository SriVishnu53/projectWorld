import streamlit as st

from streamlit_option_menu import option_menu


import home, account, analaysis, About
st.set_page_config(
        page_title="Analaysis",
)



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Menus',
                options=['Home','Account','Text_Analaysis','About'],
                icons=['house-fill','person-circle','bar-chart-line-fill','chat-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "Account":
            account.app()    
        if app == "Text_Analaysis":
            analaysis.app()        
        if app == 'About':
            About.app()
            
             
          
             
    run()            
         
