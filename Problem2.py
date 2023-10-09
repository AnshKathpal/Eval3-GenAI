members = [
    {"name" : "Alice", "prefered_genre" : "Romance"},
    {"name" : "Alice", "prefered_genre" : "Romance"}
]

books = [
    {"title" : "Love in the rain", "genre" : "Romance"},
    {"title" : "Historical Time", "genre" : "History"}
]

output = []

for member in members:
    for book in books:
        if member["prefered_genre"] == book["genre"]:
            output.append({"member" : member["name"], "book" : book["Title"]})

            print(output)