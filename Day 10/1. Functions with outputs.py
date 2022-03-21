def format_name(f_name,l_name):
    #f_name=input("What's your First name? ")
    #l_name=input("What's your last name?")
    formatted_f=f_name.title()
    formatted_l=l_name.title()
    return f"{formatted_f}, {formatted_l}"

print(format_name("geo", "mari"))