import streamlit as st

def render(auth, base_url):
    """Render the login page and handle authentication."""
    st.title("Please Log In")
    with st.form(key='login_form'):
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        submit_button = st.form_submit_button(label='Log In')

        if submit_button:
            token = auth.get_token(username, password)
            if token and auth.verify_token(token):
                st.session_state['token'] = token  # Store the token in session state
                st.success("Logged in successfully!")
                st.experimental_rerun()  # Reload the page to show the main content
            else:
                st.error('Access denied. Please check your credentials and try again.')

    # Add a link to the WordPress sign-up page
    if st.button('Sign Up'):
        sign_up_url = f"{base_url}/signup"  # Adjust this URL to your actual sign-up page
        st.markdown(f"[Sign Up Here]({sign_up_url})", unsafe_allow_html=True)
