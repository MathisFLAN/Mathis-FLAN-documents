def palindrome(Mot):
    MotDefini = []
    MotInverse = []

    position = 0

    for i in Mot:
        MotDefini.append(i)
        position = position + 1

    while position != 0:
        position = position - 1
        MotInverse.append(MotDefini[position])

    if MotDefini == MotInverse:
        print(f"Le mot '{Mot}' est un palindrome.")
    else:
        print(f"Le mot '{Mot}' n'est pas un palindrome.")


#autres manières de faire ce programme

#def palindrome(Mot):
#    MotDefini = list(Mot)
#    MotInverse = MotDefini[::-1]  # Inverse la liste

#    if MotDefini == MotInverse:
#        print(f"Le mot '{Mot}' est un palindrome.")
#   else:
#        print(f"Le mot '{Mot}' n'est pas un palindrome.")



palindrome('ruine')
palindrome('level')