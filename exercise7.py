def prompt_user(person_num):
    print("How far did person {} run (in metres)?".format(person_num))
    distance = float(input())
    print("How long (in minutes) did person {} run take to run {} metres?".format(person_num, distance))
    mins = float(input())
    return {
      "id": person_num,
      "distance": distance,
      "minutes": mins,
      "speed": distance / (mins * 60)
    }

persons = []
speeds = []
for i in range(1,4):
    person = prompt_user(i)
    persons.append(person)
    speeds.append(person["speed"])

# descending order
persons_sorted_by_speed = sorted(persons, key = lambda i: i['speed'], reverse=True)
print(persons_sorted_by_speed)
max_speed_person = persons_sorted_by_speed[0]
print(max_speed_person)
max_speed = max_speed_person["speed"]
print(max_speed)

itIsATie = True
for speed in speeds:
    if max_speed != speed:
        itIsATie = False

if itIsATie:
    print("Everyone tied at {} m/s".format(max_speed))
else:
    person2 = persons_sorted_by_speed[1]
    person2_speed = person2["speed"]
    if max_speed != person2_speed:
        print("Person {} was the fastest at {} m/s".format(max_speed_person["id"],max_speed_person["speed"]))
    else:
        print("Well done everyone!")
