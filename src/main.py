import subprocess
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Table Window")
# root.geometry("500x500")

ip_file = open("IP_addresses.txt", "r+")
ip_list = ip_file.readlines()

for index in range(len(ip_list)):
    ip_list[index] = ip_list[index].split()

ip_output = []
for index in range(len(ip_list)):
    ip_output.append(['','','','',''])

def update_table():
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

        # print(ip_output[index])
        # print(ip_output)


        # Clear the existing table data
        table.delete(*table.get_children())

        # Insert the new data into the table
        for index, row in enumerate(ip_output):
            table.insert("", "end", text=index+1, values=row)

        # Schedule the next update
        root.after(50, update_table)


table = ttk.Treeview(root, columns=("Host Name", "IP Address", "Status", "Response Time", "Packet Loss"))
table.heading("#0", text="ID")
table.heading("Host Name", text="Host Name")
table.heading("IP Address", text="IP Address")
table.heading("Status", text="Status")
table.heading("Response Time", text="Response Time")
table.heading("Packet Loss", text="Packet Loss")

# Add some sample data
for i in range(len(ip_list)):
    table.insert("", "end", text=i+1, values=(ip_list[i][1], ip_list[i][0], "Checking...", "-", "-"))

# Pack the Treeview widget
table.pack()

# Start the update loop
root.after(50, update_table)

# Run the Tkinter event loop
root.mainloop()
