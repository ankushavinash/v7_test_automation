#a = driver.find_element(by=By.XPATH, value="//*[@id='v7rpcc']/pre").text
a = "captured text is : A2L Import Start 3/24/2022 5:23:19 AM 'Accept Modules without Q-Group')"
text = "Accept Modules without Q-Group"
print("captured text is : " + a)
if a.find(text):
    print("*******Modules uploaded successfully : " + text + " *********")
else:
    print("******** Modules upload failed **********")