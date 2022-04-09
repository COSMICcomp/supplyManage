import json
print("Welcome to supplyManage by Cosmos ./Code\nType in .{help} to get started with commands")

initcmd = input("./: ")

if initcmd == ".{help}":
    print(
        "Welcome to supplyManage\n"
        "Start by creating chain: ./create{}\n"
        "Add product to chain by ./chain/pro\n"
        "Add chain type by: ./chain/type\n"
        "Add destination by: ./chain/desti\n"
        "To read a chain from exported file: help cmd: --read-help"
        "Right now, only one chain works. Multiple can be added, but system will fail"
        "Type ./chain/log for all lists printed\n"
        "Now rerun program to load\n"
    )
while True:
  if initcmd == "./create{}":
    ask = input("Name of Chain: ")
    chain = ask
    chainpro = [] # List of products 
    chaintype = [] # List of Types
    destichain = [] # final place of products
    print("Chain {} is made.".format(chain))
    initcmd = input("./: ")
  
  elif initcmd == "./{}/pro".format(chain):
    productname = input("Name of Product: ")
    chainpro.append(productname)
    initcmd = input("./: ")
  
  elif initcmd == "./{}/type".format(chain):
    typepro = input("Shipping Type: ")
    chaintype.append(chaintype)
    initcmd = input("./: ")
  
  elif initcmd == "./{}/desti".format(chain):
    prodesti = input("Final Place of Product: ")
    destichain.append(prodesti)
    initcmd = input("./: ")
  
  elif initcmd == "./{}/log".format(chain):
    asklogprint = input("We are going to export as a txt file. y or n")
    if asklogprint == "n":
      initcmd = input("./: ")
    elif asklogprint == 'y':
      with open("DataProducts.txt", 'w') as savepro:
        savepro.write(json.dumps(chainpro))
        savepro.write('\n')
        savepro.write(json.dumps(chaintype))
        savepro.write('\n')
        savepro.write(json.dumps(destichain))
        savepro.write('\n')
      initcmd = input("./: ")
    else:
      print("Invalid Response")
      initcmd = input("./: ")
  elif initcmd == "./read":
    with open("DataProducts.txt") as radpro:
      lines = radpro.readlines()
    askuserifwanttoprintread = input("Do you want to print all or append to new list: 1 or 2")
    if askuserifwanttoprintread == "1":
      print(lines)
    elif askuserifwanttoprintread == "2":
      newlist = []
      newlist.append(lines)
      asku = input("Done, do you want to export as DataProducts.txt? y or n")
      if asku == "n":
        print("Okay")
        initcmd = input("./: ")
      elif asku == 'y':
        with open("DataProducts.txt", "w") as wrote:
          wrote.write(json.dumps(newlist))
          initcmd = input("./: ")
      else:
        print("Invalid")
        initcmd = input("./: ")
    else:
      print("Invalid")
      initcmd = input("./: ")
  elif initcmd == '--read-help':
    print(
      "To Read a file type: ./read"
      "Make sure that the exported file is named DataProducts.txt"
      "Make sure that it is a valid file exported from the ./chain/log command"
    )
    initcmd = input("./: ")
  else:
    print("Invalid Command")