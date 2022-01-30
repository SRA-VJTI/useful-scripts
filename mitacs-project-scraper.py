import requests
import json
import csv

url = "https://globalink.mitacs.ca/api/sasprojectlistpaging"

# change the "keyword\":\"robotics\" here
payload = "{\"HostProvince\":null,\"HostUniversity\":null,\"LanguageUsed\":[\"Anglais\",\"English\",\"Both English and French\",\"Either French or English\"],\"keyword\":\"robotics\",\"FirstName\":null,\"LastName\":null,\"AcademicDiscipline\":null,\"Location\":null,\"PreferredBackgroundCollection\":null,\"offset\":0,\"limit\":81}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

programs = json.loads(response.text.encode('utf8'))["rows"]

print(len(programs))

data_file = open('data_file.csv', 'w') 
  
csv_writer = csv.writer(data_file) 

csv_writer.writerow(["Project ID", "Project Title", "Project Description", "College", "Student Roles", "Student Skills", "Prof Name"])

for i in programs:
    csv_writer.writerow([i["ProjectID"], i["ProjectTitle"], i["projectDescription"], i["HostUniversity"], i["StudentRoles"], i["StudentSkills"], i["Professor.FirstName"]+ " " + i["Professor.LastName"]])

data_file.close()
