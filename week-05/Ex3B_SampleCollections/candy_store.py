tuple_1 = ('lollipop', 'skittles', 'air heads')
tuple_2 = ('strawberry', 'mango', 'cherry')

candy_combinations = set()


candy_combinations.add(tuple_1[0] + " " + tuple_2[0])
candy_combinations.add(tuple_1[1] + " " + tuple_2[1])
candy_combinations.add(tuple_1[2] + " " + tuple_2[2])


print("Today’s candy options include:")
print(candy_combinations)

#After priting this multiple times I noticed that the order of the items changed each time.