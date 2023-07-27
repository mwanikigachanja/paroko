if __name__ == "__main__":
    db_file = "parishioner_management.db"
    manager = ParishionerManager(db_file)

    # Adding a parishioner
    manager.add_parishioner("John Doe", "123 Main St", "john@example.com", "2023-01-15", "2023-05-20")

    # Editing a parishioner
    manager.edit_parishioner(1, "John Doe", "456 Elm St", "john.doe@example.com", "2023-01-15", "2023-05-20")

    # Deleting a parishioner
    manager.delete_parishioner(1)

    # Retrieving parishioners by ID
    parishioner = manager.get_parishioner_by_id(2)
    print(parishioner)

    # Searching parishioners by name, address, or contact
    search_results = manager.search_parishioners("John")
    print(search_results)

    # Getting all parishioners
    all_parishioners = manager.get_all_parishioners()
    print(all_parishioners)

