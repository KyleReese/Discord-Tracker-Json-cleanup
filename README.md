# Discord-Tracker-Json-cleanup
A python script to separate messages from a long single line json file created by Discord History Tracker.

The browser script [Discord History Tracker](https://dht.chylex.com/) will parse and save the contents of a discord channel to a json file. 
However, this json file is created as a single line in the text file making it near impossible to process when saving the history of a large channel.

This script will create a new file filled with all of the messages of the discord channel separated by newlines. 
This allows for easy parallel processing of the text as in my use case of creating a word cloud out of over 2 million messages.

