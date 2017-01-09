from requests import get

apiUrl = "http://www.nhtsa.gov/webapi/api/SafetyRatings"
apiParam = ""
outputFormat = "?format=json"

# Combine all three variables to make up the complete request URL
response = get(apiUrl + apiParam + outputFormat)

# code below is only to handle JSON response object/format
# use equivalent sets of commands to handle xml response object/format
json_obj = response.json()

# Load the Result (vehicle collection) from the JSON response
print('------------------------------', '           Result			 ',
      '------------------------------', sep="\n")
for objectCollection in json_obj['Results']:
    # Loop each vehicle in the vehicles collection
    for safetyRatingAttribute, safetyRatingValue in objectCollection.items():
        print(safetyRatingAttribute, ": ", safetyRatingValue)
# After running this example, feel free to explore the results below
print(json_obj)
