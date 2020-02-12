
import streamlit as st
import helpers
from show_pages import show_ad_budget, show_welcome_page, show_starbucks_operation, show_corporate_valuation


def main():

    sim_selection = st.sidebar.selectbox('Go To ...', helpers.OPTIONS)

    if sim_selection == 'Welcome Page':
        show_welcome_page()

    elif sim_selection == 'Example 1: Advertising Budget':
        show_ad_budget()

    elif sim_selection == 'Example 2: Starbucks Operation':
        show_starbucks_operation()

    elif sim_selection == 'Example 3: Corporate Valuation':
        show_corporate_valuation()


if __name__ == '__main__':
    main()
