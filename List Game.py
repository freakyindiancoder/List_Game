#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Function to Displays The current Game List
def display_game(game_list):
    print('The current game list is :')
    print(game_list)


# In[2]:


#Function to Choose the position to update
def pos_choice():
    
    choice = 'Wrong choice'
    
    while choice not in ['0','1','2']:
        
        choice = input('Enter your choice (0,1,2) ')
        
        if choice not in ['0','1','2']:
            print(f'choice should be either (0,1,2): ')
        else:
            return int(choice)


# In[3]:


#Function to update game_list
def replacement(game_list,position):
    
    replace = input('Enter the string to be replaced: ')
    
    game_list[position] = replace
    print(game_list)
    return game_list


# In[4]:


#Function to continue game or to end game
def continue_game():
    choice = 'wrong'
    
    while choice not in ['y','n']:
        
        choice = input('Do you wish to continue the game (y or n): ')
        
        if choice not in ['y','n']:
            print('the choice should be y or n')
    if choice == 'y':
        return True
    else:
        return False


# In[5]:


#Now lets Build Logic of the Game
game_on = True
game_list = [0,1,2]

#Unless the game_on == False the game will be continued:
while game_on:
    
    #display the game list
    display_game(game_list)
    
    #Assing the position to pos_choice or you can call directly
    position = pos_choice()
    
    #Update the Game list Using the Position Chosen and Value given as input
    game_list = replacement(game_list,position)
    
    #Ask user to continue or not and assign that boolean to game_on:(if true then game continue,if it is false game exits)
    game_on = continue_game()


# In[ ]:




