from migadu_api import MigaduAPI

def main():
    api_key = "" # TODO use environment variable later 
    domain = "" # pud.gg
    api = MigaduAPI(api_key, domain)

    while True:
        print("\n1. New email\n2. Delete email\n3. Quit")
        choice = input("Options: ")
        if choice == "1":
            local_part = input("Set email name (without @): ")
            password = input("Set password: ")
            result = api.create_mailbox(local_part, password)
            print("Created:", result)
        elif choice == "2":
            local_part = input("Name of email to delete (without @): ")
            success = api.delete_mailbox(local_part)
            print("Deleted." if success else "Failed to delete.")
        elif choice == "3":
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()