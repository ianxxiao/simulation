
import streamlit as st
import helpers
from show_pages import show_ad_budget, show_welcome_page, show_starbucks_operation, show_corporate_valuation, \
    show_product_allocation


def main():

    sim_selection = st.sidebar.selectbox('Go To ...', helpers.OPTIONS)

    if sim_selection == 'Welcome Page':
        show_welcome_page()

    elif sim_selection == 'CMO Lab: Nike Marketing':
        show_ad_budget()

    elif sim_selection == 'COO Lab: Starbucks Operation':
        show_starbucks_operation()

    elif sim_selection == 'CFO Lab: Corporate Valuation':
        show_corporate_valuation()

    elif sim_selection == 'CPO Lab: Product Portfolio':
        show_product_allocation()

    else:
        st.markdown("Something went wrong. We are looking into it.")


if __name__ == '__main__':
    main()
