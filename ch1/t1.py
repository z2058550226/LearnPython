print("You can experiment with code within IDLE's shell. Cool, eh?")

if 43 > 42:
    print("Don't panic!")

movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]

print(movies[0])

print(len(movies))

cast = ["Cleese", 'Palin', 'Jones', "Idle"]

print(cast)
print(len(cast))  # 4
print(cast[1])
cast.append("Gilliam")
print(cast)  # ['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']
cast.pop()
print(cast)  # ['Cleese', 'Palin', 'Jones', 'Idle']
cast.extend(["Gilliam", "Chapman"])
print(cast)  # ['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam', 'Chapman']
cast.remove("Chapman")
print(cast)  # ['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']
cast.insert(0, "Chapman")
print(cast)  # ['Chapman', 'Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']

# Build-in for loop
fav_movies = ["The Holy Grail", "The Life of Brian"]

for each_flick in fav_movies:
    print(each_flick)

count = 0
while count < len(movies):
    print(movies[count])
    count = count + 1

# Store list within lists
movies = [
    "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
    [
        "Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]
    ]
]

print(movies[4][1][3])  # Eric Idle

names = ['Michael', 'Terry']
isinstance(names, list)  # True

num_names = len(names)
isinstance(num_names, list)  # False

for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)