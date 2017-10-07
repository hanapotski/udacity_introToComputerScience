# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url', 
# and therefore still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

start_link = page.find('<a href=')     #find link index
link_text = page[start_link:]     #extract <a href="http://udacity.com">
url_first_index = link_text.find('"') + 1     #find index of h in http, + 1 to remove "
url_last_index = link_text.find('"', url_first_index)     #find index of last "
url = link_text[url_first_index:url_last_index]     #extract url from link text


print url


#Dave's solution
start_link = page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote + 1)
url = page[start_quote + 1: end_quote]