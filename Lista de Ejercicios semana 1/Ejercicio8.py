password = input("Escriba la contraseña: ")
newPassword = input("Escriba nuevamente la contraseña: ")

if password.upper() == newPassword.upper():
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas no coinciden")
