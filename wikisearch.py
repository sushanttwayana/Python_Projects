# pip install wikipedia

import wikipedia

query = wikipedia.page("Machine Learining")
# prints the summary of the provided content
print(query.summary)