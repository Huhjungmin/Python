persons = [ "Kim", "Park", "Lee", "Choi"]
restaurants = [ "Korean", "American", "French", "Chinese"]

persons = [ "Kim", "Park", "Lee"] 
restaurants = [ "Korean", "American", "French"]

for person in persons:
    for restaurant in restaurants:
        print(person + "이"+ restaurant+" 식당을방문")

