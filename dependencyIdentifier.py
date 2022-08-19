import xml.etree.ElementTree as xml
import glob

path = "../../../.m2/repository"

text_files = glob.glob(path + "/**/*.jar", recursive = True)
file1 = open("m2_dependencies.txt","w")
  
file1.writelines(text_files)
print("All jar in m2_dependencies.txt file")
file1.close()
#    find ./ -name "*.jar" >> test.txt
print("---------------------------------------------------")
file2 = open("m2_dependencies.txt","r")
file3 = open("missing_dependencies.txt","w")
readfile = file2.read()
#print(readfile,"******************")
pom = xml.parse('pom.xml')

nsmap = {'m': 'http://maven.apache.org/POM/4.0.0'}
for mapping in pom.findall('//m:dependencies/m:dependency', nsmap):
    groupId  = mapping.find('m:groupId', nsmap).text
    artifactId  = mapping.find('m:artifactId', nsmap).text
    version = mapping.find('m:version', nsmap).text
    
    dependency_name=artifactId+"-"+version+".jar"
    dependency_path=groupId.replace(".","/")+"/"+artifactId+"/"+version+"/"+dependency_name
    # checking condition for string found or not
    if dependency_name in readfile: 
        print(dependency_name, 'Found In File')
    else: 
        print(dependency_name , 'Not Found')
        file3.write(dependency_path+";") 
  
# closing a file
file2.close()
file3.close()

