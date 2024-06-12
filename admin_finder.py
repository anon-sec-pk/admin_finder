import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random
from colorama import init, Fore, Style
import os

# Initialize colorama
init()

# Default list of common admin paths
default_admin_paths = [
    'admin', 'admin/login', 'admin/index', 'admin/home', 'admin.php', 'admin.html',
    'administrator', 'admin1', 'admin2', 'admin3', 'admin4', 'admin5', 'admin6',
    'admin7', 'admin8', 'admin9', 'login', 'adminarea', 'bb-admin', 'adminLogin',
    'admin_area', 'panel-administracion', 'instadmin', 'memberadmin', 'administratorlogin',
    'adm', 'admin/account', 'admin_area/admin', 'admincontrol', 'adminpanel', 'adminpanel.html',
    'admin_login', 'admin/admin', 'admin_login.html', 'cpanel', 'controlpanel', 'admin/cp',
    'admincontrol.asp', 'admincontrol.html', 'admincp', 'adminarea/login', 'admin_login.asp',
    'admin_area/admin.html', 'webadmin', 'adminsite', 'adminpanel.php', 'admin_control', 'sysadmin',
    'adminpage', 'panel', 'adm.php', 'adm.html', 'admin.asp', 'admin.js', 'admin.jsp',
    'admin.py', 'admin.cgi', 'myadmin', 'secretadmin', 'hiddenadmin', 'manage', 'manager',
    'useradmin', 'sysadmin', 'systemadmin', 'secureadmin', 'adminportal', 'admincontrolpanel',
    'rootadmin', 'superadmin', 'superuser', 'authadmin', 'moderator', 'mod', 'admin-dashboard',
    'dashboard', 'admin_dashboard', 'adminarea.php', 'admin_area.php', 'adminhome', 'admin_home',
    'admin/home.php', 'adminarea/login.php', 'adminlogin', 'admin/logon', 'admin/logon.php',
    'admin/secure', 'adminsecure', 'adminaccess', 'admin_access', 'accessadmin', 'admin/config',
    'admin/configuration', 'admin_console', 'adminconsole', 'login.php', 'adminpage', 'admin-area',
    'admincontrolpanel', 'admin_panel', 'admin.html', 'admin_site', 'admin123', 'cp/admin',
    'backend', 'cms-admin', 'admincontrol', 'admin_index', 'cpadmin', 'adminweb', 'adminweb.php',
    'adminweb.html', 'system_admin', 'panel_admin', 'admin_panel.html', 'admin_panel.php',
    'manager_admin', 'adminarea.asp', 'adminarea.jsp', 'adminarea.html', 'adminarea.cgi',
    'secureadmin.php', 'adminhome.php', 'adminportal.html', 'adminportal.php', 'adminpanel.cgi',
    'adminpanel.asp', 'adminpanel.jsp', 'admindashboard', 'admininterface', 'controlcenter',
    'admincontrolcenter', 'adminpage.html', 'adminpage.php', 'rootcontrol', 'siteadmin', 
    'adminzone', 'superadminpanel', 'webcontrol', 'webadminpanel', 'adminhomepage', 
    'controlroom', 'adminroom', 'adminsection', 'admindesk', 'adminsystem', 'admincontrolsystem', 
    'admininterface.php', 'admininterface.html', 'adminportal.cgi', 'adminportal.asp',
    'adminportal.jsp', 'siteadmin.php', 'siteadmin.html', 'webmaster', 'adminmaster', 
    'adminmaster.php', 'adminmaster.html', 'controlpanel.php', 'controlpanel.html', 
    'admincenter', 'admincenter.php', 'admincenter.html', 'adminzone.php', 'adminzone.html',
    'sitecontrol', 'superusercontrol', 'mainadmin', 'mainadmin.php', 'mainadmin.html',
    'adminsite', 'adminsite.php', 'adminsite.html', 'adminconsole.php', 'adminconsole.html',
    'adminlogin.html', 'adminlogin.php', 'rootadmin.php', 'rootadmin.html', 'secure/admin',
    'webadmin/login', 'webadmin/index', 'management', 'management/login', 'management/index',
    'management/admin', 'adminhome/index', 'adminhome/login', 'managerlogin', 'admindashboard.php',
    'admindashboard.html', 'secure/controlpanel', 'secure/login', 'secure/index'
]

# Function to load admin paths from a file
def load_admin_paths(filename):
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            paths = file.read().splitlines()
            return paths if paths else default_admin_paths
    else:
        return default_admin_paths

# Random user-agents list to mimic different browsers
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15'
]

# Function to check if admin page exists
def check_admin_page(url, path):
    full_url = f"{url}/{path}"
    headers = {'User-Agent': random.choice(user_agents)}
    try:
        response = requests.get(full_url, headers=headers, timeout=5)
        if response.status_code == 200:
            return full_url
    except requests.RequestException:
        pass
    return None

# Function to find admin page using threading
def find_admin_page(url, paths):
    results = []
    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = {executor.submit(check_admin_page, url, path): path for path in paths}
        for future in as_completed(futures):
            path = futures[future]
            try:
                result = future.result()
                if result:
                    print(Fore.GREEN + f"[+] Admin page found at: {result}" + Fore.RESET)
                    results.append(result)
                    with open("admin_finder_results.txt", "a") as log_file:
                        log_file.write(f"{result}\n")
                else:
                    print(Fore.RED + f"[-] No admin page at: {url}/{path}" + Fore.RESET)
            except Exception as exc:
                                print(f"[!] Exception for {url}/{path}: {exc}")
    return results

def main():
    print(Style.BRIGHT + Fore.BLUE + """
   
 █████  ██████  ███    ███ ██ ███    ██     ██   ██  █████   ██████ ██   ██ 
██   ██ ██   ██ ████  ████ ██ ████   ██     ██   ██ ██   ██ ██      ██  ██  
███████ ██   ██ ██ ████ ██ ██ ██ ██  ██     ███████ ███████ ██      █████   
██   ██ ██   ██ ██  ██  ██ ██ ██  ██ ██     ██   ██ ██   ██ ██      ██  ██  
██   ██ ██████  ██      ██ ██ ██   ████     ██   ██ ██   ██  ██████ ██   ██ 
                                                                            
                                                                            

    """ + Style.RESET_ALL)
    print("Admin Panel Finder Tool")
    print("=======================\n")
    url = input("Enter the website URL (e.g., http://example.com): ").strip()
    if not url.startswith('http'):
        url = 'http://' + url
    
    # Allow user to choose their own admin directories file
    admin_file = input("Enter the path to your admin directories file (leave empty for default): ").strip()
    admin_paths = load_admin_paths(admin_file) if admin_file else default_admin_paths
    
    print("\n[+] Finding admin pages...\n")
    start_time = time.time()
    results = find_admin_page(url, admin_paths)
    elapsed_time = time.time() - start_time
    if results:
        print("\n[+] Admin pages found:")
        for result in results:
            print(Fore.GREEN + result + Fore.RESET)
    else:
        print("\n[-] No admin pages found.")
    print(f"\n[+] Scan completed in {elapsed_time:.2f} seconds.")
    print("[+] Results have been logged to admin_finder_results.txt")

if __name__ == "__main__":
    main()

