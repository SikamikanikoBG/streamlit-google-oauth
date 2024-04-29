import streamlit as st
import streamlit_google_oauth as oauth

client_id = st.secrets["GOOGLE_CLIENT_ID"]
client_secret = st.secrets["GOOGLE_CLIENT_SECRET"]
redirect_uri = st.secrets["GOOGLE_REDIRECT_URI"]


if __name__ == "__main__":
    app_name = '''
    Streamlit Google Authentication Demo
    '''
    app_desc = '''
    A streamlit application that authenticates users by <strong>Google Oauth</strong>.
    The user must have a google account to log in into the application.
    '''
    login_info = oauth.login(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        app_name=app_name,
        app_desc=app_desc,
        logout_button_text="Logout",
    )
    if login_info:
        user_id, user_email = login_info
        st.write(f"Welcome {user_email}")

# streamlit run app.py --server.port 8080
