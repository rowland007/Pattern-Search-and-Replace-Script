import re

#Paragraph provided for search and replace

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

#Using the findall function, get all of the instances of non alphanumeric characters in the string assigned to 'lorem_ipsum'
#Output to the console, the number of non-alphanumeric characters.  Hint:  use the len function

#Using the findall function, get all of the instances of 'sit-amet' or 'sit:amet' characters in the string assigned to 'lorem_ipsum'
#Assign the outcome to a variable named 'occurrance_sit_amet'

#Output to the console, the number of sit-amet or sit:amet occurrances.  Hint:  use the len function


#Replace sit:amet and sit-amet with sit amet using the sub funciton
#Assign the outcome to a variable named 'replace_results'


#Using the findall function, get all of the instances of 'sit amet' in the string assigned to 'replace_results'
#Assign the outcome to a variable named 'occurrance_sit_amet'

#Output to the console, the number of sit amet occurrances.  Hint:  use the len function


