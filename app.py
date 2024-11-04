import random
import string

def generar_contraseña(longitud):
    if longitud < 4:
        raise ValueError("La longitud debe ser al menos de 4 caracteres para incluir todos los tipos de caracteres")
    
    # Aseguramos incluir al meno,jhb,jhb,jbs una letra mayúscula, minúscula, un dígito y un símbolo
    contraseña = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    
    # Concatenamos todos los caracteres posibles
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    
    # Agregamos más caracteres aleatorios hasta alcanzar la longitud deseada
    contraseña += [random.choice(caracteres) for _ in range(longitud - 4)]
    
    # Mezclamos los caracteres para evitar un patrón fijo al principio
    random.shuffle(contraseña)

    # Convertimos la lista en una cadena de texto y la retornamos
    return ''.join(contraseña)

# Solicitamos al usuario la longitud deseada para la contraseña
try:
    longitud = int(input("Introduce la longitud que deseas para tu contraseña: "))  

    # Generamos y mostramos la contraseña
    print(f"Tu contraseña generada es: {generar_contraseña(longitud)}")
except ValueError as e:
    print(f"Error: {e}")