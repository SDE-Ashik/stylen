import streamlit as st
from homepage.MainPage import MainPage
from stylegen.main import Main


class MainProgram:

    def __init__(self):
        pass

    # Create a function to show the homepage
    def show_homepage(self):
        mp = MainPage()
        mp.mainpage_display()

    # Create a function to show the StyleGen page
    def show_stylegen(self):
        main = Main()
        main.main_display()

    def mainprogram_display(self):

        # Define the options for the side menu
        options = ["Homepage", "Try StyleGen"]

        # Set the default option to "Homepage"
        selected_option = options.index("Homepage")

        # Create the side menu
        selected_option = st.sidebar.selectbox("Select an option", options)

        # Show the appropriate page based on the selected option
        if selected_option == "Homepage":
            self.show_homepage()
        elif selected_option == "Try StyleGen":
            self.show_stylegen()


mp = MainProgram()
mp.mainprogram_display()