# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

# def print_kwargs(name,skill):
def print_kwargs(**kwargs):
       for key,value in kwargs.items():
              print(f"{key}: {value}")
       # print("Name", name, "and Skill is", skill)


print_kwargs(name="Chirag", skill="React")
print_kwargs(name="Ravindra",skill="Python",age=19)
