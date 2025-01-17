from bs4 import BeautifulSoup

# Load the HTML content
html_content = '''
<!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast</title>
</head>
<body>
    <h4>5-Day Weather Forecast</h4>
    <table>
        <thead>
            <tr>
                <th>Day</th>
                <th>Temperature</th>
                <th>Condition</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Monday</td>
                <td>25°C</td>
                <td>Sunny</td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td>22°C</td>
                <td>Cloudy</td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td>18°C</td>
                <td>Rainy</td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td>20°C</td>
                <td>Partly Cloudy</td>
            </tr>
            <tr>
                <td>Friday</td>
                <td>30°C</td>
                <td>Sunny</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
'''

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract table rows
rows = soup.find('tbody').find_all('tr')

# Initialize lists to store extracted data
data = []

# Parse each row and extract details
for row in rows:
    cols = row.find_all('td')
    day = cols[0].text
    temperature = int(cols[1].text.replace('°C', ''))
    condition = cols[2].text
    data.append({"day": day, "temperature": temperature, "condition": condition})

# Display the weather data
print("Weather Data:")
for entry in data:
    print(f"Day: {entry['day']}, Temperature: {entry['temperature']}°C, Condition: {entry['condition']}")

# Find the day(s) with the highest temperature
max_temp = max(data, key=lambda x: x['temperature'])['temperature']
hottest_days = [entry['day'] for entry in data if entry['temperature'] == max_temp]
print(f"\nDay(s) with the highest temperature ({max_temp}°C): {', '.join(hottest_days)}")

# Find the day(s) with "Sunny" condition
sunny_days = [entry['day'] for entry in data if entry['condition'] == "Sunny"]
print(f"Day(s) with Sunny condition: {', '.join(sunny_days)}")

# Calculate the average temperature
average_temp = sum(entry['temperature'] for entry in data) / len(data)
print(f"\nAverage Temperature for the week: {average_temp:.2f}°C")
