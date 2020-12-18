# get user email address
email = input("What is your email_address?: ").strip()

# slice out user name
user = email[:email.index("@")]
print(user)

# slice domain name
domain = email[email.index("@")+1:]
print(domain)

# format message
string = "Your username is {} and the domain is {}"
output = string.format(user, domain)

# display output message
print(output)