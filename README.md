Option 1: Direct creation from terminal

```bash
# Create the README.md file with content
cat > README.md << 'EOF'
# 🔫 Free Fire UID to INFO

A powerful Python script that extracts detailed player information from any Free Fire UID using the GameSkinbo API.

## ✨ Features

- 🆔 **Basic Profile** - Name, Gender, Level, EXP, Likes, Honor & Credit Score
- 📊 **Rank Statistics** - BR & CS ranks, rank points, max ranks achieved
- 🏆 **Guild Information** - Guild name, level, members, leader details
- 🐾 **Pet Details** - Pet name, type, level, experience, skin ID
- 💎 **Account Assets** - Equipped avatar, banner, outfit, weapon
- 📅 **Timeline** - Account creation date & last login
- 🌍 **Multi-Region Support** - 12+ regions including Advance Server
- 🔐 **Auto Token Generation** - Secure API authentication

## 🌍 Supported Regions

| Code | Region |
|------|--------|
| ind  | 🇮🇳 India |
| sg   | 🇸🇬 Singapore |
| id   | 🇮🇩 Indonesia |
| br   | 🇧🇷 Brazil |
| us   | 🇺🇸 USA |
| th   | 🇹🇭 Thailand |
| vn   | 🇻🇳 Vietnam |
| tw   | 🇹🇼 Taiwan |
| me   | 🌍 Middle East |
| pk   | 🇵🇰 Pakistan |
| bd   | 🇧🇩 Bangladesh |
| adv  | 🔥 Advance Server |

## 📋 Requirements

- Python 3.6+
- `requests` library

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/ibr4himkh4lil/Free-Fire-UID-to-INFO.git

# Navigate to directory
cd Free-Fire-UID-to-INFO

# Install required package
pip install requests
```

🚀 Usage

```bash
python ff_updated.py
```

Steps:

1. Select option 1 to check a UID
2. Enter the Free Fire UID (numbers only)
3. Choose the player's region from the list
4. View the complete player information

📸 Output Example

```
──────────────────────────────────────
  🆔 UID Verification
──────────────────────────────────────
  UID                      : 1234567890
  Nickname                 : ProPlayer
  Gender                   : Male 👦
  Region                   : ind
  Account Level            : 85
  EXP                      : 1,234,567
  Likes                    : 15,432
  Honor Score              : 5200
  Credit Score             : 100
  Account Created          : 2021-03-15
  Last Login               : 2026-06-12

──────────────────────────────────────
  📊 Rank & Stats
──────────────────────────────────────
  BR Rank                  : Grandmaster
  BR Rank Points           : 4200
  BR Max Rank              : Grandmaster
  CS Rank Points           : 3100
  CS Max Rank              : Heroic

──────────────────────────────────────
  🏆 Guild Information
──────────────────────────────────────
  Guild Name               : Elite Squad
  Guild Level              : 10
  Guild Members            : 45/50

──────────────────────────────────────
  ✅ Check Complete!
──────────────────────────────────────
```

⚠️ Disclaimer

This tool is for educational purposes only. Use it responsibly and only check UIDs you own or have permission to inspect. The developer is not responsible for any misuse of this script.

📝 License

MIT License - Free for personal and educational use.

👨‍💻 Author

ibr4himkh4lil

---

⭐ Star this repository if you found it useful!
EOF

Add to git

git add README.md

Commit

git commit -m "Add README.md with documentation"

Push to GitHub

git push origin main

```

---

### Option 2: Complete step-by-step commands

```bash
# 1. Initialize git (if not already done)
git init

# 2. Add your Python file
git add ff_updated.py

# 3. Create and add README
echo "# Free Fire UID to INFO - Player Info Checker" > README.md
echo "" >> README.md
echo "Python script to extract Free Fire player details from UID. Supports 12+ regions." >> README.md

# 4. Commit both files
git commit -m "Initial commit: FF UID checker script and README"

# 5. Add remote origin (replace with your repo URL)
git remote add origin https://github.com/ibr4himkh4lil/Free-Fire-UID-to-INFO.git

# 6. Push to GitHub
git branch -M main
git push -u origin main
```

Option 3: One-liner (fastest)

```bash
echo "# 🔫 Free Fire UID to INFO\n\nPython script to extract player details from any Free Fire UID.\n\n## Usage\n\`\`\`bash\npython ff_updated.py\n\`\`\`\n\n## Features\n- Profile info (name, level, gender)\n- Rank stats (BR & CS)\n- Guild details\n- Pet information\n- 12+ regions supported\n\n## Requirements\n\`\`\`bash\npip install requests\n\`\`\`" > README.md && git add README.md && git commit -m "Add README" && git push
```
