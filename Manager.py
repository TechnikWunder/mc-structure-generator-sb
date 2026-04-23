import OllamaManager, RconManager, ModellManager

def main():

    rcon_password = input("Enter the RCON password: ")
    if rcon_password == "":
        print("Invalid input")
        main()

    user_input = input("do you want to use an optimized modell for generating minecraft structures? default is yes (y/n): ")

    if user_input.lower() in ["y", "Y", ""]:
        custom_modell = True
    elif user_input.lower() in ["n", "N"]:
        custom_modell = False
    else:
        print("Invalid input")
        main()
    
    modell_input = input("Enter the model name: ")
    if modell_input == "":
        print("Invalid input")
        main()
    
    if custom_modell == True:
        modell = "mc-builder-sb-" + modell_input
    else:
        modell = modell_input

    ModellManager.download_modell(modell_input)
    if custom_modell == True:
        ModellManager.create_modell(modell)
    
    generate_structure(modell_input, rcon_password)

def generate_structure(modell_input, rcon_password):
    user_prompt = input("Enter your request (or type 'exit' to quit): ")

    if user_prompt.lower() == "exit":
        return

    print("Generating Structure...")

    ai_response = OllamaManager.request_modell(modell_input, user_prompt)

    print("Structure Generated, Placing Blocks...")

    blocks = ai_response.split(", ")

    for block in blocks:
        print(block)
        RconManager.send_command("setblock " + block, "localhost", 25575, rcon_password)

    print("Structure Placed!")

    generate_structure(modell_input, rcon_password)

main()