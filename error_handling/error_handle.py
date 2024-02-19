file = open('youtube.txt','w')
try:
    file.write("Hello python")
finally:
    file.close() 

with open('youtube.txt','w') as file:
    file.write("Chai aur python")          