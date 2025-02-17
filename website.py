

import streamlit as st

def home():
    st.title("Home Page")
    st.write("Welcome to Home Page")

def about_us():
    st.title("About Us Page")  
    st.write("Welcome to About Us Page")
 
def contact_us():
    st.title("Contact Us Page")
    st.write("Welcome to Contact Us Page")
    st.write("Email: umemakhan@gmail.com") 

def main():
    st.set_page_config(page_title="Online Store")
    st.sidebar.title("Navbar")

    page = st.sidebar.radio("Navigation:", ("HOME", "About Us", "Contact Us"))

    if page == "HOME":
        home()
    elif page == "About Us":
        about_us()
    elif page == "Contact Us":
        contact_us()

main()
