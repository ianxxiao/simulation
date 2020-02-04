import simpy
from sims import AdSim
import streamlit as st

def main():

    # set up layout
    st.title("Simulator")
    ad_budget = st.slider(label='Pick an Advertising Budget',
                          max_value=50000,
                          min_value=20000,
                          step=5000)

    ad = AdSim(ad_budget)
    sales = ad.run_sim()

    st.text(f'expected sales ${sales:.2f}')


if __name__ == '__main__':
    main()
