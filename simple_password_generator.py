import random
import pyfiglet

print("--------------------------------------------------")
ascii_banner = pyfiglet.figlet_format("PASSWORD GENERATOR")
print(ascii_banner)
print("--------------------------------------------------")
print("Hello! Let's generate a password")

### Liste de caractères qui vont définir le mot de passe
characters = "!@#$%^&*()"
nums = "0123456789"
majCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minCharacters = "abcdefghijklmnopqrstuvwxyz"

### Demande à l'utilisateur la longeur du mot de passe
passwordLength = int(input("Quelle est la longueur du mot de passe à générer ? "))

### Génération du mot de passe aléatoire
newPassword = ""
for x in range(passwordLength):
    ### Sélection aléatoire du type de caractère
    char_type = random.choice(["characters", "nums", "majCharacters", "minCharacters"])
    
    ### Sélection aléatoire d'un caractère du type de caractère choisi
    if char_type == "characters":
        newPassword += random.choice(characters)
    elif char_type == "nums":
        newPassword += random.choice(nums)
    elif char_type == "majCharacters":
        newPassword += random.choice(majCharacters)
    elif char_type == "minCharacters":
        newPassword += random.choice(minCharacters)

### Affichert le mot de passe généré
print("\n Voici votre mot de passe généré :", newPassword)