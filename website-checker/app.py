print("🔍 Website URL Checker")
value = input("\nEnter a website URL: ")
if value.startswith("https"):
    print("This website uses HTTPS - (secure) 🤝")
elif value.startswith("http"):
    print("This website uses HTTP - (not secure) 💣💣")
else:
    print("This doesnt look like a complete url")
