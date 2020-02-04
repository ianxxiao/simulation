import simpy
from sims import AdSim


def main():
    ad = AdSim()
    ad.run_sim()
    ad._set_budget(50000)
    ad.run_sim()


if __name__ == '__main__':
    main()
