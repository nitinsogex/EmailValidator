# 📧 Email Validator

A simple **Python-based Email Validator** that checks the validity of an email address with detailed feedback explaining *why* it’s invalid.

---

## 🚀 Features

✅ Checks for:
- Missing or multiple `@` symbols  
- Empty or malformed username / domain  
- Consecutive or trailing special characters (e.g., `..`, `--`, `++`, `.-`, etc.)  
- Invalid domain or top-level domain (TLD) format  
- Disallowed characters in username or domain  
- Leading or trailing special symbols (`.`, `+`, `_`, `-`)  

✅ Returns clear human-readable messages  
✅ Works without any external dependencies (only Python’s built-in `re` module)  
✅ Fully interactive — enter emails repeatedly until you quit  

---

## 🧠 Example Output

```bash
Enter an email: nitin--.--@gmail.com
Multiple special characters consecutively not allowed in local part.

Enter an email: sdf+++@g.com
Multiple special characters consecutively not allowed in local part.

Enter an email: nitin@gmail.com
✅ Email looks valid.

Enter an email (or 'q' to quit): q
Goodbye!

```
------
# 🧑‍💻 Author
## Nitin Soge

* 📧 Reach me for suggestions, ideas, or improvements!
---
## 📝 License

* This project is released under the MIT License — you’re free to use, modify, and distribute it with attribution.
---
## ⭐ If you found this helpful, please star the repository on GitHub!