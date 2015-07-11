# slackrun

[![Join the chat at https://gitter.im/jtrip/slackrun](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/jtrip/slackrun?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)  

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
- ~~continue to improve ToDo list~~
- implement flavor text in action_info

- Web interface
    - initial simple action list test
    - user management
    - character management
    - action creation

- BeagleBone interfac
    - GPIO
    - DotStar RGB LEDs

- Slack listener
    - interpret messages to call actions
    - interpret messages to generic rolls/checks

- Chatty: 
    - send messages live
    - NPCs actions
    - npc avatar image library    

- Web Interface
    - User Management
    - Action Display
    - Action creation
    
- Build Action Library
    
- _combat stacker_