# encoding=utf-8
import requests
import json
import os


# 得到文件里的内容
def GetList(fileAddress):
    myfile = open(fileAddress, 'r')
    myFileContent = myfile.readlines()
    myfile.close()
    return myFileContent


def AddChild(firstName, middleName, lastName, groupId):
    url = 'http://api2.learning-genie.com/api/v1/students'
    header = {
        'Host': 'http://test.web.learning-genie.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'http://test.web.learning-genie.com/',
        'Host': 'test.api2.learning-genie.com',
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'X-UID': 'e7799744-3f52-e711-9a01-067b83821db4'
    }
    postdata = {"birthDate": "11/02/2016", "currentTime": "2017-06-05 10:35:04.611", "enrollmentDate": "06/01/2017",
                "firstName": firstName, "gender": "MALE", "groupId": groupId, "lastName": lastName,
                "middleName": middleName, "withdrawnDate": "06/07/2017"}
    req = requests.post(url, data=json.dumps(postdata), headers=header)
    print(req.text)


if __name__ == "__main__":
    while 1:
        s = input("1. Add Child\n2. Other:\nInput your chek : ")
        if s == "1":
            path = os.path.dirname(os.path.dirname(os.path.abspath("AddChildPostBodyJsonContorller.py")))
            childName = GetList(path + "\\resourse\m.txt")

            groupId = input("Input groupId : ")
            childCount = input("Add child count : ")
            i = 0
            for name in childName:
                i = i + 1
                if int(childCount) < i:
                    print("Stop")
                    break
                name = name.strip('\n').split()
                firstName = ""
                middleName = ""
                lastName = ""
                if len(name) > 2:
                    firstName = name[0]
                    middleName = name[1]
                    lastName = name[2]
                elif len(name) > 1:
                    firstName = name[0]
                    lastName = name[1]
                else:
                    firstName = name[0]
                AddChild(firstName, middleName, lastName, groupId);
        else:
            print("1")
