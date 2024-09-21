# import another_module
# print(another_module.another_variable)
#
#
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkOliveGreen")
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_column("Rank", ["3", "2", "1"])
table.align["Pokemon Name"] = "c"
table.align["Type"] = "l"
table.sortby = "Rank"
table.default_color = "Green"
table.get_json_string()
print(table)

