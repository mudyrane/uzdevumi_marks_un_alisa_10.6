# Prasam lietotājam ievadīt krāsu

rasa = input("Ievadi krāsu (rozā, dzeltenā, sarkanā, zaļā, zilā): ").lower()

# 2. Pārbaudām krāsu un pasakām, kurš varonis tas ir

if rasa == "dzeltenā":
    print("Tas ir Sūklis Bobs!")

elif rasa == "rozā":
    print("Tas ir Patriks Stars!")

elif rasa == "sarkanā":
    print("Tas ir misters Krabs!")

elif rasa == "zaļā":
    print("Tas ir Planktons!")

elif rasa == "zilā":
    print("Tas ir Skvidvards!")

else:
    print("Piedod, šādu krāsu nepazīstu. Mēģini vēlreiz!")
