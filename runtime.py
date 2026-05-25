import os

INSTALLED_APPS = {}

# =========================
# LECTOR DE .MAZOXPKG
# =========================
def load_pkg(path):
    if not os.path.exists(path):
        print("App no encontrada:", path)
        return None

    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# =========================
# INTERPRETE SIMPLE
# =========================
def run_pkg(content):

    lines = content.splitlines()

    for line in lines:

        line = line.strip()

        if line.startswith("PRINT"):
            text = line.replace("PRINT", "").strip().strip('"')
            print(text)

        elif line.startswith("name:"):
            name = line.split(":",1)[1].strip()
            INSTALLED_APPS["name"] = name

        elif line.startswith("version:"):
            version = line.split(":",1)[1].strip()
            INSTALLED_APPS["version"] = version

# =========================
# INSTALAR APP
# =========================
def install_app(path):

    print("Installing:", path)

    content = load_pkg(path)

    if content:
        run_pkg(content)
        print("✔ Installed successfully")

# =========================
# EJECUTAR MAZO OS
# =========================
if __name__ == "__main__":

    while True:
        cmd = input("MAZO-X> ")

        if cmd.startswith("install"):
            path = cmd.split(" ",1)[1]
            install_app(path)

        elif cmd == "exit":
            break

        else:
            print("Unknown command")
