def format_name(f_name, l_name):
    formated_f = f_name.title()
    formated_l = l_name.title()
    return f"{formated_f} {formated_l}"


formated_string = format_name(f_name="masoud", l_name="mashayekh")
print(formated_string)