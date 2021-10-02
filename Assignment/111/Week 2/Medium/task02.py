def replace_domain(email, new, old = "kaaj.com"):
    if(old in email):
        email = email.replace(old, new)
        return "Changed: "+  email
    else:
        return "Unchanged: "+ email
        
e = input("Enter email: ")
n = input("Enter new domain: ")
o = input("Enter old domain: ")
print(replace_domain(e, n, o))