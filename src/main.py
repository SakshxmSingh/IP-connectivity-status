import subprocess

ip_file = open("IP_addresses.txt", "r+")
ip_list = ip_file.readlines()

ip_output = [['','','','','']]*len(ip_list)

while True:
    for index in range(len(ip_list)):
        try:
            ip_list[index] = ip_list[index].split()
        except:
            pass

        ip_output[index][0] = ip_list[index][1]
        ip_output[index][1] = ip_list[index][0]

        # os.system("ping " +ip[0]+ " -c 5 -q")
        command = "ping " + ip_list[index][0] + " -c 5 -q"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = process.communicate()

        stdout = stdout.split("\n")

        stdout[3] = stdout[3].split(", ")
        stdout[3][2] = stdout[3][2].split()

        if stdout[3][2][0] == '100.0%':
            ip_output[index][2] = 'Inactive'
            ip_output[index][3] = '-'
            ip_output[index][4] = stdout[3][2][0]

        elif stdout[3][2][0] == '0.0%':
            ip_output[index][2] = 'Active'
            try:
                stdout[4] = stdout[4].split(" = ")
                stdout[4] = stdout[4][1].split("/")
            except: 
                pass
            ip_output[index][3] = stdout[4][1]
            ip_output[index][4] = stdout[3][2][0]

        else:
            ip_output[index][2] = 'Packet Loss'
            try:
                stdout[4] = stdout[4].split(" = ")
                stdout[4] = stdout[4][1].split("/")
            except: 
                pass
            ip_output[index][3] = stdout[4][1]
            ip_output[index][4] = stdout[3][2][0]
            

        print(ip_output[index])

