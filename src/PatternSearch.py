"""
Program:		Pattern Search
Author:			Randall Rowland
Class:			IT-140-Q3788 Introduction to Scripting 18EW3
Instructor:		Angel D. Cross
Date:			15 Feb 2018
Description:    The task for this project is to create a simple pattern search script.
                The script emphasizes the importance of regular expressions and their utility for searching, replacing,
                and managing large volumes of textual data.

Input:          stdin
Output:         stdout
Known bugs/missing features:

Modifications:
Date                Comment
----    ------------------------------------------------
"""
import re

# Provided paragraphs for search and replace
original_text='''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

# Find all the non-alphanumeric characters in the string assigned to 'lorem_ipsum' and
# Output the number to the console
pattern = '[^a-zA-Z0-9]'
results = re.findall(pattern, lorem_ipsum)
# print(len(results))

# Find all of the instances of 'sit-amet' or 'sit:amet' characters in the string assigned to 'lorem_ipsum'
# Output  the number of sit-amet or sit:amet occurrences to the console.
pattern2 = 'sit[-:]amet'
occurrence_sit_amet = re.findall(pattern2, lorem_ipsum)
# print(len(occurrence_sit_amet))

# Replace sit:amet and sit-amet with 'sit amet' using the sub function
substitution = "sit amet"
replace_results = re.sub(pattern2, substitution, lorem_ipsum)

# Find all of the instances of 'sit amet' characters in the string assigned to replace_results
# Output the number of occurrences to the console.
occurrence_sit_amet = re.findall(substitution, replace_results)
print(len(occurrence_sit_amet))
