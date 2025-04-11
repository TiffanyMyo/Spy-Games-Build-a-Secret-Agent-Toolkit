def SecureVault():
    with open("notes.txt","r") as note:
        read = note.read()
        return read