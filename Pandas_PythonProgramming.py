#import Quandl
import pandas as pd
import pickle

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]

def grab_initial_state_data():
    states = state_list()

    #frame creation 
    main_df = pd.DataFrame()

grab_initial_state_data()
