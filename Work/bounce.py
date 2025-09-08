# bounce.py
#
# Exercise 1.5
initial_height = 100
# without round()
# for i in range(1, 11):
#     bounce_height = initial_height * 0.6
#     initial_height = bounce_height
#     print(i, bounce_height)

# if use round()
for i in range(1, 11):
    bounce_height = round(initial_height * 0.6, 4)
    initial_height = bounce_height
    print(i, bounce_height)