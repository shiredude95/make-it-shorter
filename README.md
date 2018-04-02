www.makeitshorter.net

# Shorter.

version. 0.2.4


# What is Shorter.?
Shorter. is a chrome extension that allows you to select text from any web-page and returns a shortened version of it.

# What do you mean shortened?

Shorter. takes your selected text, processes it and finds the most important parts of input that gives you an overall idea of the selection without having to read the entire selection

#  How do I use this?

Select the text you want (normally more than 2 lines) and right click to get the menu.Click on Make It Shorter to view the summary.

  
#  How does this work?

Shorter. takes your selected text and ranks each sentence in the text according to its relevance in the selection. It employs the TF-IDF principle to score each sentence with respect to words present in it and their importance in relation to the selection. Using a two pass method to first find out the Top-N sentences in the first pass followed by finding out the highest scoring sentence in every N-th bracket ensures the context as well as scores are factored in while summarizing.
