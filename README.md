# slackrun
Tools for playing Shadowrun with Slack and the help of a BeagleBone Black.  

## Current State
_functional, limited_  
Action.oy has been added to take custom actionInfo and it can currently be tested with:
- LanaCharm.py

charm.py is depreciated.  


## actionTemplate.py
_functional, not fully implemented_  
This file is for users/players to copy and create their own unique actions.
 They only need to know what Attribute and Skill and roll will use and they can add information
 like the character's name and other flavor text, which is a great time to put custom emoji to work.  
 
each unique action calls:  
 
    Action.runner(action_info)

which is currently being done by having main return the action_info:  

    if __name__ == '__main__':
        # action_info = main()

        try:
            Action.runner(main())
        except:
            print('ERROR - Action.runner() failed')

  
I might want to update this to combine multiple related actions like different uses of the same item... maybe.  

## ToDo
- implement flavor text in action_info

- Chatty: 
 - send messages live
 - NPCs actions

- Web Interface
 - User Management
 - Action Display
 - Action creation
    
- Build Action Library
    