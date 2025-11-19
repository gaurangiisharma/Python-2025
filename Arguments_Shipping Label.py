# ----- *ARGS & **KWARGS -----
print(f"Shipping Label")
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" and "pobox" in kwargs:
        print(f"Street: {kwargs.get('street')}")
        print(f"Apt:{kwargs.get('apt')}")
        print(f"PO box: {kwargs.get('pobox')}")
    elif "apt" in kwargs:
        print(f"Street: {kwargs.get('street')}")
        print(f"Apt:{kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"PO box: {kwargs.get('pobox')}")
    else:
        print(f"Street: {kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')}"
          f"\nZip code: {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants","III",
               street="123 Fake St.",
               pobox="#1001",
               apt="100",
               city="Detroit",
               state="Michigan",
               zip="54321")