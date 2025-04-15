import random
print("MUSIC RECOMMENDER")
genres = {
    "rock": ['Queen', 'king', 'AC/DC'],
    'pop': ['Burna', 'seyi vibe', 'davido'],
    "hip-hop":  ['Burna', 'seyi vibe', 'wizkid'],
}
value = input("what genre would you like ? (rock/pop/hip-hop): ")
if value not in genres:
   print("sorry , i dont know this genre")
else:
   print(f"check out {random.choice(genres[value])}")

