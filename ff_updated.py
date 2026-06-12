import requests
import hmac
import hashlib
import base64
import time
import math
import json

# ===== Token Generator =====
SECRET = "GAMESKINBOFFIDCHECKERSECURITYPROTOCOL"

def generate_token(uid: str) -> str:
    timestamp_ms = int(time.time() * 1000)
    time_block = math.floor(timestamp_ms / 30000)
    nonce = hmac.new(
        SECRET.encode(),
        str(time_block).encode(),
        hashlib.sha256
    ).hexdigest()[:32]
    signature = hmac.new(
        nonce.encode(),
        f"{uid}|{timestamp_ms}".encode(),
        hashlib.sha256
    ).hexdigest()
    raw = f"{uid}|{timestamp_ms}|{signature}"
    return base64.b64encode(raw.encode()).decode()


# ===== Session Setup =====
session = requests.Session()
session.headers.update({
    'authority': 'gameskinbo.com',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
    'x-api-client': 'gameskinbo-web',
    'referer': 'https://gameskinbo.com/free_fire_id_checker',
})


# ===== Display Helpers =====
def section(title):
    print(f"\n{'─'*38}")
    print(f"  {title}")
    print(f"{'─'*38}")

def field(label, value, default="N/A"):
    print(f"  {label:<24}: {value if value not in [None, '', 'null'] else default}")

def rank_name(rank_id):
    ranks = {
        300: "Bronze", 301: "Bronze I", 302: "Bronze II", 303: "Bronze III",
        304: "Silver", 305: "Silver I", 306: "Silver II", 307: "Silver III",
        308: "Gold", 309: "Gold I", 310: "Gold II", 311: "Gold III",
        312: "Platinum", 313: "Platinum I", 314: "Platinum II", 315: "Platinum III",
        316: "Diamond", 317: "Diamond I", 318: "Diamond II", 319: "Diamond III",
        320: "Heroic", 321: "Heroic I", 322: "Heroic II", 323: "Grandmaster",
    }
    return ranks.get(rank_id, f"Rank {rank_id}")

def format_date(iso_str):
    if not iso_str:
        return "N/A"
    return iso_str[:10]  # YYYY-MM-DD

def pet_name_from_raw(data):
    # pet_name field or raw_data PetInfo
    if data.get("pet_name"):
        return data["pet_name"]
    try:
        raw = json.loads(data.get("raw_data", "{}"))
        return raw.get("PetInfo", {}).get("name", None)
    except:
        return None

def pet_type_from_id(pet_id):
    pets = {
        1300000101: "Ottero 🦦",
        1300000102: "Falco 🦅",
        1300000103: "Poring 🟡",
        1300000104: "Detective Panda 🐼",
        1300000105: "Shiba 🐕",
        1300000106: "Spirit Fox 🦊",
        1300000107: "Mechanical Pup 🤖",
        1300000108: "Kitty 🐱",
        1300000109: "Moony 🐰",
        1300000110: "Mr. Waggor 🐧",
        1300000111: "Dreki 🐉",
        1300000112: "Pumpkin 🎃",
    }
    return pets.get(pet_id, f"Pet ID: {pet_id}")

def gender_label(g):
    return "Male 👦" if g == "Gender_MALE" else "Female 👧" if g == "Gender_FEMALE" else "N/A"


# ===== Main Checker =====
def check_ff_uid(uid: str, region: str = "ind"):
    token = generate_token(uid)
    url = f"https://gameskinbo.com/api/ff_id_checker?uid={uid}&token={token}&region={region}"

    try:
        res = session.get(url, timeout=10)
        data = res.json()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return

    if "name" not in data:
        print(f"\n❌ UID {uid} পাওয়া যায়নি! (Region: {region.upper()})")
        return

    # ── 🆔 Basic Info ──────────────────────────────
    section("🆔 UID Verification")
    field("UID", uid)
    field("Nickname", data.get("name"))
    field("Gender", gender_label(data.get("gender")))
    field("Region", data.get("region"))
    field("Account Level", data.get("level"))
    field("EXP", f"{data.get('exp', 0):,}" if data.get('exp') else None)
    field("Likes", f"{int(data.get('likes', 0)):,}" if data.get('likes') else None)
    field("Honor Score", data.get("honor_score"))
    field("Credit Score", data.get("credit_score"))
    field("Prime Level", data.get("prime_level"))
    field("Signature", data.get("signature"))
    field("Release Version", data.get("release_version"))
    field("Account Created", format_date(data.get("created_at")))
    field("Last Login", format_date(data.get("last_login")))

    # ── 📊 Rank & Stats ────────────────────────────
    section("📊 Rank & Stats")
    field("BR Rank", data.get("br_rank"))
    field("BR Rank Points", data.get("br_rank_point"))
    field("BR Max Rank", rank_name(data.get("br_max_rank")) if data.get("br_max_rank") else None)
    field("CS Rank Points", data.get("cs_rank_point"))
    field("CS Max Rank", rank_name(data.get("cs_max_rank")) if data.get("cs_max_rank") else None)
    field("Equipped BP Badges", data.get("equipped_bp_badges"))
    field("Season ID", data.get("season_id"))

    # ── 🏆 Guild Info ──────────────────────────────
    section("🏆 Guild Information")
    field("Guild Name", data.get("guild_name"))
    field("Guild ID", data.get("guild_id"))
    field("Guild Level", data.get("guild_level"))
    field("Guild Members", f"{data.get('guild_member')}/{data.get('guild_capacity')}" if data.get('guild_member') else None)
    field("Guild Leader", data.get("guild_leader_name"))
    field("Leader UID", data.get("guild_leader_uid"))
    field("Leader Level", data.get("guild_leader_level"))
    field("Leader Likes", f"{data.get('guild_leader_likes', 0):,}" if data.get('guild_leader_likes') else None)
    field("Leader BR Rank", rank_name(data.get("guild_leader_br_rank")) if data.get("guild_leader_br_rank") else None)
    field("Leader Region", data.get("guild_leader_region"))

    # ── 🐾 Pet Info ────────────────────────────────
    section("🐾 Pet Details")
    pet_id = data.get("pet_id")
    field("Pet Name", pet_name_from_raw(data))
    field("Pet Type", pet_type_from_id(pet_id) if pet_id else None)
    field("Pet Level", data.get("pet_level"))
    field("Pet Experience", f"{data.get('pet_exp', 0):,}" if data.get('pet_exp') else None)
    field("Pet Selected", "Yes ✅" if data.get("pet_is_selected") else "No")
    field("Pet Skin ID", data.get("pet_skin_id"))

    # ── 💎 Account Info ────────────────────────────
    section("💎 Account Details")
    field("Account Type", "Pro" if data.get("account_type") == 1 else str(data.get("account_type")))
    field("Equipped Avatar ID", data.get("equipped_avatar_id"))
    field("Equipped Banner ID", data.get("equipped_banner_id"))
    field("Equipped Outfit", data.get("equipped_outfit"))
    field("Equipped Weapon", data.get("equipped_weapon"))

    print(f"\n{'─'*38}")
    print(f"  ✅ Check Complete! (Source: {data.get('source', 'API')})")
    print(f"{'─'*38}\n")


# ===== Region Selector =====
REGIONS = {
    "1":  ("ind", "🇮🇳 India"),
    "2":  ("sg",  "🇸🇬 Singapore"),
    "3":  ("id",  "🇮🇩 Indonesia"),
    "4":  ("br",  "🇧🇷 Brazil"),
    "5":  ("us",  "🇺🇸 USA"),
    "6":  ("th",  "🇹🇭 Thailand"),
    "7":  ("vn",  "🇻🇳 Vietnam"),
    "8":  ("tw",  "🇹🇼 Taiwan"),
    "9":  ("me",  "🌍 Middle East"),
    "10": ("pk",  "🇵🇰 Pakistan"),
    "11": ("bd",  "🇧🇩 Bangladesh"),
    "12": ("adv", "🔥 Advance Server"),
}

def select_region():
    print("\n🌐 Region Select করো:")
    for k, (code, name) in REGIONS.items():
        print(f"  [{k:>2}] {name}")
    choice = input("  Choice (default=1): ").strip() or "1"
    return REGIONS.get(choice, ("ind", "India"))[0]


# ===== Main Loop =====
print("\n" + "="*38)
print("  🎮 FF ID Checker - Full Version")
print("="*38)

while True:
    print("\n[1] UID Check করো")
    print("[2] Exit")
    cmd = input("Choice: ").strip()

    if cmd == "2" or cmd.lower() == "q":
        print("\nGoodbye! 👋")
        break
    elif cmd == "1":
        uid = input("\nUID দাও: ").strip()
        if not uid.isdigit():
            print("❌ শুধু সংখ্যা!")
            continue
        region = select_region()
        check_ff_uid(uid, region)
    else:
        print("❌ Invalid choice!")
