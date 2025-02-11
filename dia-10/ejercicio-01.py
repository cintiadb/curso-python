def my_function():
    result = 3 * 2
    return result

def format_name(f_name, l_name):
    #para escribir documentacion
    """take a first and ladt name and format it to return the title case version of the name"""
    if f_name == "" or l_name == "":
        return"You didn't provide valid input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
#el return es el final de la funcion nada funciona despues del return

print(format_name(input("What is your first name?"),input("What is your last name?")))





