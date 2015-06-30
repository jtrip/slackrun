# slackrun
Tools for playing Shadowrun with Slack and the help of a BeagleBone Black.

## Current State
_functional, limited_  
charm.py has unique settings, uses a simple dict from untangle to get character data, and sends the post.

I will be keeping things in a generally running state however there will be some big changes to how to use the separate tools and some convergence.

## actionTemplate.py
_not implemented_  
This file is for users/players to copy and create their own unique actions. They only need to know what Attribute and Skill and roll will use and they can add information like the character's name and other flavor text, which is a great time to put custom emoji to work.
 
This needs a gerenalized execution method, which I am referring to as:  

    runnerAction 
  
I might want to update this to combine multiple related actions like different uses of the same item... maybe.
