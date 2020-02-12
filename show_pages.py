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
    st.markdown("**Step 1: Define input(s) of uncertainty ... **")
    center = st.slider("Pick the average value of the input", min_value=40,
                       max_value=50, value=45, step=1)
    N = st.slider("Decide how many samples (N): ", min_value=100, max_value=5000, value=500, step=100)
    st.markdown(f"We draw {N} samples "
                f"with the densest population around {center} with an uncertainty distribution of [normal distribution]"
                f"(https://en.wikipedia.org/wiki/Normal_distribution).")

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
    st.markdown(
        "**Next Step:** Use the panel on the left to choose an example and see how we apply these analysis to the outcomes "
        "from various real-world examples.")
    st.markdown("We will learn tools like: ")
    st.markdown("1. Influence Diagram \n"
                "2. Sensitivity Analysis \n"
                "3. Cumulative Probability")


def show_ad_budget():

    # set up layout
    st.title("Welcome to the CMO Lab")
    st.markdown("As a **Marketing leader** of a famous sneaker company, you might wonder how "
                "to best allocate your advertising budget to get the most sales return. Here are some additional context: ")
    st.markdown("1. You can deploy $20,000 to $50,000 this year \n"
                "2. You need to help manage price and cost making and selling each shoe\n"
                "3. Your goal is to maximize overall profit (sales revenue minus cost)")
    st.markdown("_**Credit**: this example is built on content from this "
                "[incredible book](https://www.amazon.ca/Management-Science-Art-Modeling-Spreadsheets/dp/0470530677) "
                "and my own professional experience._")
    
    st.markdown("***")

    st.markdown("This simulation will focus on the following: ")
    st.markdown("1. How to design a simulation with an **Influence Diagram** \n"
                "2. How to interpret the outcomes in the context of business decisioning \n")
    
    st.markdown("***")
    st.markdown("** INFLUENCE DIAGRAM **")
    st.markdown("Before we dive into the simulation, let's breakdown the problem with an Influence Diagram. "
                "It helps us to conceptualize the key simulation components: inputs, key factors and "
                "relationships, and outcomes.")

    st.markdown("Here are the general steps to define an Influence Diagram: ")
    st.markdown("1. Define a **quantitative objective** \n"
                "2. Identify the **controllable inputs** that are deterministic or with uncertainty \n"
                "3. Map out the **key factors** and relationships from inputs to output \n"
                "4. Identify the **non-trivial relationships** (e.g. f(x): advertising budget to unit sold) \n"
                "5. Get past data to represent the factors and approximate the relationships; make sensible assumptions "
                "if needed")
    
    image = Image.open('./asset/Influence-Diagram-Ad-Budget.png')
    st.image(image, caption='Influence Diagram of Ad Budget Problem', format='PNG',
             use_column_width=True)

    st.markdown("***")
    
    st.markdown("** SIMULATION **")

    st.markdown("Price and cost are factors with **uncertainty**. They can only be controlled to some degree due to, "
                "for example, seasonality or relationship with suppliers. "
                "So, this is where uncertainty comes in. ")

    st.markdown("Let's choose the **averages of price and cost** for our simulation. We will assume both of these factors "
                "have a triangular probability distribution")

    unit_price = st.slider(label="Choose an Average Unit Price",
                          max_value=50,
                          min_value=20,
                          step=5)

    unit_cost = st.slider(label="Choose an Average Unit Cost",
                          max_value=35,
                          min_value=10,
                          step=5)

    st.markdown("Next, let's decide how many experiments (e.g. _campaigns_ in a marketing context) we want to run. "
                "In general, the more experiment we run, the less noise there will be. But having more experiment "
                "trades off computation time, specially in more complex cases.")

    N = st.slider(label="Number of experiment",
                          max_value=10000,
                          min_value=2500,
                          value=5000,
                          step=1000)

    st.markdown(f"Due to uncertainty, here is a spectrum of price and cost if we'd quote the vendors {N} times.")

    price_item, cost_item = helpers.get_items_ad_triangular(unit_price, unit_cost, N)
    hist_data = [price_item, cost_item]
    group_label = ['Unit Price', 'Unit Cost']
    fig = ff.create_distplot(hist_data, group_label, bin_size=[0.5, 0.5], curve_type='normal')
    st.plotly_chart(fig)

    st.markdown("Finally, let's choose a **budget**. This is a deterministic factor since we can fully control it.")
    ad_budget = st.slider(label="Choose a Advertising Budget ($'000)",
                          max_value=50,
                          min_value=20,
                          step=1)

    # Calculate Profit
    st.markdown("***")
    st.markdown("** OUTCOME **")
    st.markdown(f"This is a spectrum of outcomes if you run **{N} campaigns** with **${ad_budget*1000} budget** "
                f"when the average unit prices is at **${unit_price}** and unit cost is at **${unit_cost}**.")
    profit_item, prob_profit = helpers.ad_calc_profit(price_item, cost_item, ad_budget)
    hist_data = [profit_item]
    group_label = ['estimated profit']
    fig = ff.create_distplot(hist_data, group_label, bin_size=[3000], curve_type='normal')
    st.plotly_chart(fig)
    
    # Analysis
    st.markdown("***")
    st.markdown("** ANALYSIS **")
    st.markdown("So, what does this mean? Here are some key highlights: ")
    st.text(f"Average Profit: ${sum(profit_item) / len(profit_item): .2f}")
    st.text(f"Probability of break-even (make over $0 profit): {prob_profit*100: .2f}%")
    st.text(f"Average Return (ROI) of Marketing Budget: "
            f"{(sum(profit_item) / len(profit_item) - ad_budget*1000) *100 / (ad_budget*1000): .2f}%")
    
    st.markdown("***")
    st.markdown("If you were in the CMO's shoes, a few fruit for thoughts:")
    st.markdown(
                "1. what is the minimum budget allocation to make a positive ROI? \n"
                "2. what are the right price and cost? (note that it will be difficult and expensive to lock in "
                "the highest price and lowest cost) \n"
                "3. what are some tactical and simples ways to improve ROI? \n")

def show_starbucks_operation():

    # set up layout
    st.title("Welcome to the COO Lab")
    st.markdown("Coming soon ...")



def show_corporate_valuation():
    st.title("Welcome to the CFO Lab")
    st.markdown("Coming soon ...")