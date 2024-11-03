import sys
import streamlit
import random


@streamlit.dialog('The Winner is...')
def display_winner(winner):
    streamlit.title(winner)

streamlit.title('STONE PAPER SCISSOR')
no_of_matches=int(streamlit.number_input(label='Enter the no of matches: ',min_value=1,step=1))
if streamlit.button('GO'):
    streamlit.session_state.tot_matches=no_of_matches
    streamlit.session_state.no_of_matches=0
    streamlit.session_state.cpu=0
    streamlit.session_state.player=0
# if 'no_of_matches' not in streamlit.session_state:
#     streamlit.session_state.no_of_matches=0
cpu=random.choice(['stone','paper','scissor'])

stone=streamlit.button('stone')
paper=streamlit.button('paper',key='paper')
scissor=streamlit.button('scissor',key='scissor')

if 'tot_matches' in streamlit.session_state:
    if streamlit.session_state.no_of_matches<streamlit.session_state.tot_matches:
        if stone:
            streamlit.session_state.no_of_matches+=1
            streamlit.text(cpu)
            if cpu=='paper':
                streamlit.title('CPU Won')
                streamlit.session_state.cpu+=1
                streamlit.image('stone_paper.gif')
            elif cpu=='scissor':
                streamlit.title('Player Won')
                streamlit.session_state.player+=1
                streamlit.image('stone_scissor.gif')
            else:
                streamlit.title('DRAW')
        if paper:
            streamlit.session_state.no_of_matches+=1
            streamlit.text(cpu)
            if cpu=='scissor':
                streamlit.title('CPU Won')
                streamlit.session_state.cpu+=1
                streamlit.image('paper_scissor.gif')
            elif cpu=='stone':
                streamlit.session_state.player+=1
                streamlit.title('Player Won')
                streamlit.image('paper_stone.gif')
            else:
                streamlit.title('DRAW')
        if scissor:
            streamlit.session_state.no_of_matches+=1
            streamlit.text(cpu)
            if cpu=='paper':
                streamlit.session_state.cpu+=1
                streamlit.title('Player Won')
                streamlit.image('scissor_paper.gif')
            elif cpu=='stone':
                streamlit.session_state.player+=1
                streamlit.title('CPU Won')
                streamlit.image('scissor_stone.gif')
            else:
                streamlit.title('DRAW')
    else:
        # if 'tot_matches' in streamlit.session_state:
        if streamlit.session_state.player<streamlit.session_state.cpu:
            display_winner('CPU')
        elif streamlit.session_state.player>streamlit.session_state.cpu:
            display_winner('Player')
        else:
            display_winner('Draw')