import itertools 
admins = ['admin', 'bob', 'sam']
users = ['falcon', 'winter soldider', 'karli']
name = input("name: ")
def names(name):
    i = 0
    level_name=None
    while name == admins[i]:
        i=i+1
        level_name= "admin: "+name
        print(level_name)
        if level_name == None:
            continue
        else:
            return level_name  
    while name == users[i]     :
        i=i+1
        level_name = "user: "+name
        print(level_name)  
        if level_name == None:
            continue
        else:
            return level_name  
a = names(name)
print(a)
# for admin,user in zip(admins,users).items():

#     print(admin, user)
#     if name == admin:
#         print("admin name: ",name)
#         exit
#     elif name == user:
#         print("user name: ",name)
#         exit
#     else:
#         print("guest name: ",name)
#         exit
# for i in range (len(admins)):
#     if name == admins[i]:
#         print("admin name: ",name)
#         exit
#     elif name == users[i]:
#         print("user name: ",name)
#         exit
#     else:
#         print("guest name: ",name)
#         exit
      



      # for i in range (len(admins)):
    #     if name == admins[i]:
    #         print("admin name: ",name)
    #         return redirect(url_for('admin'))
    #         continue
    #     elif name == users[i]:
    #         print("user name: ",name)
    #         return redirect(url_for('user',user_name= name))
    #         continue
    #     else:
    #         print("guest name: ",name)
    #         return redirect(url_for('guest', guest_name=name))
    #         continue
    # for admin_var in admins:
    #     if name == admin_var:
    #         return redirect(url_for('admin'))
    #     else:
    #          return redirect(url_for('guest', guest_name=name))

    # for user_var in users:
    #     if name == user_var:
    #         return redirect(url_for('user',user_name= name))
    #     else:
    #         return redirect(url_for('guest', guest_name=name))
    # print(itertools.zip_longest(admins, users))
    # for (admin_var, users_var) in itertools.zip_longest(admins, users):
    #     print(admin_var,users_var)
    #     if name == admin_var:
    #         print("name ",name)
    #         print('admin var ',admin_var)
    #         return redirect(url_for('admin'))
    #     elif name == users_var:
    #         print("name: ",name)
    #         print("user_var: ",user_var)
    #         return redirect(url_for('user', user_name=name))
    #     else:
    #         return redirect(url_for('guest', guest_name=name))