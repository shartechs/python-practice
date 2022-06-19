# Initializing variable 
s = set()

# Add elements to s
s.add(1)
s.add(2)
s.add(3)
s.add(3)
s.add(4)

s.remove(4)

print(s)

print(f"Set S has {len(s)} elements")