a,b,c = [1,2,3]

print(f"Simple unpacking {a}, {b}, {c}")

d,e,*f = [4,5,6,7,8,9]

print(f"Extended unpacking {d}, {e}, {f}")

a, _ = [1,2] # _ is anonimus when i dont need the value

# unpack nested structures
data = ("Gav", (12, 17))

name, (age, fav_number) = data
print(f"Nested unpacking {name}, {age}, {fav_number}")



https://www.youtube.com/watch?v=6ViGc5NgdSw