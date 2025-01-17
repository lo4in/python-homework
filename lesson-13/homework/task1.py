import sqlite3

# Task 1: Database Creation
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# Define the Roster table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

# Task 2: Insert Data
cursor.executemany('''
INSERT INTO Roster (Name, Species, Age)
VALUES (?, ?, ?)
''', [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

# Task 3: Update Data
cursor.execute('''
UPDATE Roster
SET Name = "Ezri Dax"
WHERE Name = "Jadzia Dax"
''')

# Task 4: Query Data
cursor.execute('''
SELECT Name, Age
FROM Roster
WHERE Species = "Bajoran"
''')
bajoran_characters = cursor.fetchall()
print("Bajoran Characters:", bajoran_characters)

# Task 5: Delete Data
cursor.execute('''
DELETE FROM Roster
WHERE Age > 100
''')

# Bonus Task: Add Rank Column and Update Data
cursor.execute('''
ALTER TABLE Roster ADD COLUMN Rank TEXT
''')

cursor.executemany('''
UPDATE Roster
SET Rank = ?
WHERE Name = ?
''', [
    ("Captain", "Benjamin Sisko"),
    ("Lieutenant", "Ezri Dax"),
    ("Major", "Kira Nerys")
])

# Advanced Query: Retrieve sorted characters
cursor.execute('''
SELECT Name, Age, Rank
FROM Roster
ORDER BY Age DESC
''')
sorted_characters = cursor.fetchall()
print("Sorted Characters by Age:", sorted_characters)

# Commit changes and close connection
conn.commit()
conn.close()
