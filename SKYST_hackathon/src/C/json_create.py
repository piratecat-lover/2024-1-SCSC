import json

def create_json(txt_file, talkslist, selectslist, brancheslist, endslist):
    """
    Creates a plot.json file from the given text file by reading lines and combining them to appropriate locations.
    """

    backgroundImg=""
    objectImg=""
    
    # Open the text file
    file = open(txt_file, 'r', encoding="utf-8")
    lines = file.readlines()    

    # Iterate over lines
    count=0
    for idx, line in enumerate(lines):
        # Check if talk

        if line[0] =='0':
            id_val=int(line.split('_')[1])+count*100
            count+=1
            next_id=int(line.split('_')[1])+count*100
            if line.split('_')[2]!="NULL\n":
                name_str=line.split('_')[2]
            else:
                name_str=""

            i=1
            scripts=""
            # Add scripts
            while(lines[idx+i][0] not in ["0", "1", "3", "#"]):
                scripts+=(lines[idx+i])
                i+=1
                if idx+i>=len(lines):
                    break

            if lines[idx+2][0] == "#":        # when scene ends
                div = []
                next = []
                if len(lines[idx+2].split('_')) > 1 :
                    branch_info = lines[idx+2].split('_')
                    next_id += 1000000
                    for i in range(int(branch_info[1])-1):
                        div.append(int(branch_info[i+2+int(branch_info[1])]))
                    for i in range(int(branch_info[1])):    
                        next.append(100+int(branch_info[2+i]))
                    branch = {
                        "type" : 2,
                        "id" : next_id,
                        "div": div,
                        "next" : next
                    }
                    brancheslist.append(branch)
                    count = 0
                else:
                    count = 0
                    next_id=int(line.split('_')[1])+101

            scripts = scripts.replace("\n", "")
            name_str = name_str.replace("\n", "")

            # Create a talk dictionary
            talk = {
                "type": 0,
                "id": id_val,
                "name": name_str,
                "background": "1.png",
                "object": "2.png",
                "script": scripts,
                "next": next_id
            }
            talkslist.append(talk)
        
        # check if select
        elif line[0] =='1':
            id_val=int(line.split('_')[1])+count*100
            count+=1
            next_id=int(line.split('_')[1])+count*100
            if line.split('_')[2]!="NULL\n":
                name_str=line.split('_')[2]
            else:
                name_str=""
            i=1
            selects=[]
            points=[]

            # Add scripts
            while(lines[idx+i+1][0] not in ["0", "1", "3", "#"]):
                selects.append(lines[idx+i+1].split('_')[0])
                points.append(int(lines[idx+i+1].split('_')[1]))
                i+=1
                if idx+i+1>=len(lines):
                    break

            scripts = lines[idx+1].replace("\n", "")
            name_str = name_str.replace("\n", "")

            if(lines[idx+1][0] == "#"):        # when scene ends
                next_id += 1

            # Create a select dictionary
            select = {
                "type": 1,
                "id": id_val,
                "name": name_str,
                "background": "1.png",
                "object": "2.png",
                "script": scripts,
                "select": [[scr, pnt] for scr, pnt in zip(selects, points)],
                "next": next_id
            }
            selectslist.append(select)
        
        # check if ending
        elif line[0]=='3':
            id_val=int(line.split('_')[1])+count*100
            i=1
            scripts=""
            # Add scripts
            while(lines[idx+i][0] not in ["0", "1", "3", "#"]):
                scripts+=(lines[idx+i])
                i+=1
                if idx+i>=len(lines):
                    break
            
            scripts = scripts.replace("\n", "")
            count = 0
            # Create an ending dictionary
            end = {
                "type": 3,
                "id": id_val,
                "background": "1.png",
                "script": scripts,
            }
            endslist.append(end)
            



# Write the dictionaries to a json file
def main():
    # create dictionaries to store data
    talkslist= []
    selectslist = []
    brancheslist = []
    endslist = []
    
    create_json("C-Lang.txt", talkslist, selectslist, brancheslist, endslist)
    with open('plot.json', 'w', encoding="utf-8") as file:
        json.dump(talkslist + selectslist + brancheslist + endslist, file, indent = 2, ensure_ascii=False)

if __name__ == "__main__":
    main()