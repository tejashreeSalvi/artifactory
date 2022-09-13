import xml.etree.ElementTree as xml
import glob
import requests

path = "../../../.m2/repository"
m2_dependencies = ""
text_files = glob.glob(path + "/**/*.jar", recursive = True)
for element in text_files: 
        m2_dependencies += element+";"
#find ./ -name "*.jar" >> test.txt
print("---------------------------------------------------")
file1 = open("missing_dependencies.txt","w")
file2 = open("dependencies_compID.txt","w")
pom = xml.parse('pom.xml')

nsmap = {'m': 'http://maven.apache.org/POM/4.0.0'}
for mapping in pom.findall('//m:dependencies/m:dependency', nsmap):
    groupId  = mapping.find('m:groupId', nsmap).text
    artifactId  = mapping.find('m:artifactId', nsmap).text
    version = mapping.find('m:version', nsmap).text
    
    dependency_name=artifactId+"-"+version+".jar"
    dependency_path=groupId.replace(".","/")+"/"+artifactId+"/"+version+"/"+dependency_name
    dependency_compID="gav://"+groupId+":"+artifactId+":"+version
    # checking condition for string found or not
    print(dependency_name , 'Not Found')
#     file1.write(dependency_path+";") 
#     file2.write(dependency_compID+"\n") 

    url = f"https://artifactmanager.jfrog.io/artifactory/thirdparty-mvn-local/{dependency_path}"
    response = requests.get(url=url, headers={"Authorization": "Basic Oportun:Salvi@2502"})
    print("Response:", response)
    if response.status_code == 404:
        file1.write(dependency_path+";") 
        file2.write(dependency_compID+"\n")
  
# closing a file
file1.close()
file2.close()

