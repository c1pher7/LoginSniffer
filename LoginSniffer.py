import requests
from termcolor import colored
import os
import time

creator = colored("https://github.com/kazovskyy/", "green")
time.sleep(0.20)
os.system("clear")
print(colored("------------------------------", "red"))
print("Bem vindo ao LoginSniffer")
print(f"criador: {creator}")
print(colored("------------------------------", "red"))
print()
print()
print("exemplo de como por url: testphp.vulnweb.com")
run = input(colored("site alvo: ", "yellow"))
print()
print(f"Qual protocolo o site {run} usa? ")
print()
print(colored("[01] http", "yellow"))
print(colored("[02] https", "yellow"))
print()
protocolo = input("select: ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/96.0.4664.45 Safari/537.36"
}


login_pages_name = [
    "/login",
    "/login.html",
    "/login.php",
    "/user",
    "/user.html",
    "/user.php",
    "/users",
    "/users.html",
    "/users.php",
    "/usuarios",
    "/usuarios.html",
    "/usuarios.php",
    "/entrar",
    "/entrar.html",
    "/entrar.php",
    "/admin",
    "/admin.html",
    "/admin.php",
    "/login_admin",
    "/login_admin.html",
    "/login_admin.php",
    "/admin_login",
    "/admin_login.html",
    "/admin_login.php",
    "/admin_panel",
    "/admin_panel.html",
    "/admin_panel.php",
    "/admin_area",
    "/admin_area.html",
    "/admin_area.php",
    "/admin_dashboard",
    "/admin_dashboard.html",
    "/admin_dashboard.php",
    "/admin_access",
    "/admin_access.html",
    "/admin_access.php",
    "/login_admin_access",
    "/login_admin_access.html",
    "/login_admin_access.php",
    "/admin_controls",
    "/admin_controls.html",
    "/admin_controls.php",
    "/admin_settings",
    "/admin_settings.html",
    "/admin_settings.php",
    "/secure_admin",
    "/secure_admin.html",
    "/secure_admin.php",
    "/admin_site",
    "/admin_site.html",
    "/admin_site.php",
    "/admin_portal",
    "/admin_portal.html",
    "/admin_portal.php",
    "/admin_privileges",
    "/admin_privileges.html",
    "/admin_privileges.php",
    "/admin_console",
    "/admin_console.html",
    "/admin_console.php",
    "/admin_section",
    "/admin_section.html",
    "/admin_section.php",
    "/admin_auth",
    "/admin_auth.html",
    "/admin_auth.php",
    "/admin_zone",
    "/admin_zone.html",
    "/admin_zone.php",
    "/admin_tools",
    "/admin_tools.html",
    "/admin_tools.php",
    "/admin_page",
    "/admin_page.html",
    "/admin_page.php",
    "/admin_access_page",
    "/admin_access_page.html",
    "/admin_access_page.php",
    "/admin_controls_login",
    "/admin_controls_login.html",
    "/admin_controls_login.php",
    "/admin_security",
    "/admin_security.html",
    "/admin_security.php",
    "/admin_zone_login",
    "/admin_zone_login.html",
    "/admin_zone_login.php",
    "/admin_account",
    "/admin_account.html",
    "/admin_account.php",
    "/admin_settings_page",
    "/admin_settings_page.html",
    "/admin_settings_page.php",
    "/admin_area_auth",
    "/admin_area_auth.html",
    "/admin_area_auth.php",
    "/admin_login_portal",
    "/admin_login_portal.html",
    "/admin_login_portal.php",
    "/admin_tools_page",
    "/admin_tools_page.html",
    "/admin_tools_page.php"
]


if protocolo == "01" or protocolo == "1":
    print()
    print()
    for url in login_pages_name:
       loginpage200 = colored(f"http://{run}{url}", "green")
       loginpage404 = colored(f"http://{run}{url}", "red")
       full_url = f"http://{run}{url}"
       
       response = requests.get(full_url, headers=headers)
       
       if response.status_code == 200:
           print(f"[!] url válida: {loginpage200}")
           quit
       else:
           print(f"[+] erro 404: {loginpage404} ")
    print()
    print(colored(f"Fim, todas as urls foram testadas!"))


if protocolo == "02" or protocolo == "2":
    print()
    print()
    for url in login_pages_name:
       loginpage200 = colored(f"https://{run}{url}", "green")
       loginpage404 = colored(f"https://{run}{url}", "red")
       full_url = f"http://{run}{url}"

       response = requests.get(full_url, headers=headers)

       if response.status_code == 200:
           print(f"[!] url válida: {loginpage200}")
           quit
       else:
           print(f"[+] erro 404: {loginpage404} ")
    print()
    print(colored(f"Fim, todas as urls foram testadas!"))


if protocolo == " " or protocolo == "":
    print()
    print()
    for url in login_pages_name:
       loginpage200 = colored(f"http://{run}{url}", "green")
       loginpage404 = colored(f"http://{run}{url}", "red")
       full_url = f"http://{run}{url}"

       response = requests.get(full_url, headers=headers)

       if response.status_code == 200:
           print(f"[!] url válida: {loginpage200}")
           quit
       else:
           print(f"[+] erro 404: {loginpage404}")
