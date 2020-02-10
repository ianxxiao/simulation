import streamlit as st
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from PIL import Image
from sims import AdSim
import helpers

def show_welcome_page():

    st.title("Welcome.")
    st.markdown("You will learn the following concepts:")
    st.markdown("1. History of Monte Carlo Method \n "
                "2. High Level Montel Carlo Process \n"
                "3. Interactive Example")

    # HISTORY
    st.markdown("***")
    st.video("https://youtu.be/ioVccVC_Smg")

    # SIMULATION ARCHITECTURE
    st.markdown("***")
    st.markdown("Monte Carlo Simulation can be represented in terms of input, transformation, and outcome.")
    image = Image.open('./asset/monte-carlo-process.png')
    st.image(image, caption='Monte Carlo Simulation Process', format='PNG',
             use_column_width=True)

    # ILLUSTRATION OF PROBABILITY DISTRIBUTION
    st.markdown("***")
    st.markdown("**Step 1: DEFINE an INPUT assume if we draw from a normal distribution ...**")
    center = st.slider("Pick the Center of the Distribution", min_value=40,
                       max_value=50, value=45, step=1)
    N = st.slider("Decide how many samples (N): ", min_value=100, max_value=5000, value=500, step=100)
    st.markdown(f"We draw {N} samples from a [normal distribution]"
                f"(https://en.wikipedia.org/wiki/Normal_distribution) "
                f"with the densest population around {center}.")

    input_items = helpers.get_items(center, N)
    hist_data = [input_items]
    group_label = ['your choice']
    fig = ff.create_distplot(hist_data, group_label, bin_size=[0.5])
    st.plotly_chart(fig)

    st.markdown("**Step 2: Apply Some Transformation to Each Sample ...**")
    distribution = st.selectbox("Pick a Distribution to Represent Uncertainty",
                                ("Uniform", "Poisson", "Triangular"))
    st.markdown(f"We apply a transformation to the population with "
                f"numbers drawn from a _{distribution}_ distribution.")

    output_items = helpers.apply_function(input_items, distribution)
    hist_data = [output_items]
    group_label = ['output']
    fig = ff.create_distplot(hist_data, group_label, bin_size=[0.1])
    st.plotly_chart(fig)

    # ANALYZE RESULTS
    st.markdown("**Step 3: Analyze the Outcome ...**")
    st.markdown("In this case, the results are not very sensible since it's a dummy example. "
                "Typically, we should ask the following quesitons: ")
    st.markdown("1. what is the probability of achieving the acceptable outcomes? Is it good enough to proceed? \n"
                "2. what is the probability of achieving sub-optimal outcomes? And how do we hedge against that? \n"
                "3. what factor has the largest impact on the outcome? How can we influence it? \n")
    st.markdown("Common Analysis: ")
    st.markdown("1. Sensitivity Analysis \n"
                "2. Cumulative Probability")
    st.markdown(
        "**Next Step:** Use the panel on the left to choose an example and see how we these analysis to the outcomes "
        "from various real-world examples.")


def show_ad_budget():

    # set up layout
    st.title("Welcome to the CMO Lab")
    st.markdown(" As a leader in Marketing, you might wonder how "
                "to best allocate your advertising budget get the most sales return.")

    ad_budget = st.slider(label="Pick an Advertising Budget ($'000)",
                          max_value=50,
                          min_value=20,
                          step=5)

    ad = AdSim(ad_budget)
    sales = ad.run_sim()

    st.text(f"expected sales ${sales:.2f}")


def show_starbucks_operation():

    # set up layout
    st.title("Welcome to the COO Lab")
    st.markdown(" As a leader in Operation, you might wonder how "
                "to best allocate your advertising budget get the most sales return.")

    ad_budget = st.slider(label="Pick an Advertising Budget ($'000)",
                          max_value=50,
                          min_value=20,
                          step=5)

    ad = AdSim(ad_budget)
    sales = ad.run_sim()

    st.text(f"expected sales ${sales:.2f}")


def show_corporate_valuation():
    st.title("Welcome to the CFO Lab")
    st.markdown("Coming soon ...")