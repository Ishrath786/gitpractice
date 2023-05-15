import os
import urllib.request

# Specify the URLs of the downloads
eclipse_url = "https://www.eclipse.org/downloads/download.php?file=/oomph/epp/2021-12/R/eclipse-inst-jre-win64.exe"
visualstudio_url = "https://aka.ms/vs/16/release/vs_community.exe"
intellij_url = "https://download-cf.jetbrains.com/idea/ideaIC-2021.1.1.exe"
java_url = "https://jdk.java.net/16/"
s3browser_url = "https://s3browser.com/download.aspx"
chrome_url = "https://www.google.com/chrome/"
git_url = "https://github.com/git-for-windows/git/releases/download/v2.31.1.windows.1/Git-2.31.1-64-bit.exe"
docker_url = "https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe"
node_js_url = "https://nodejs.org/dist/v16.3.0/node-v16.3.0-x64.msi"
jmeter_url = "https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-5.4.1.zip"



# Define the output directories and filenames
downloads_dir = "downloads"
eclipse_file = "eclipse.exe"
visualstudio_file = "vs_community.exe"
intellij_file = "intellij.exe"
java_file = "java.exe"
angular_file = "angular.txt"
s3browser_file = "s3browser.exe"
chrome_file = "chrome.exe"
git_file = "Git-2.31.1-64-bit.exe"
docker_file = "Docker Desktop Installer.exe"
node_js_file = "node.msi"
jmeter_file =  "jmeter.zip"



# Create the downloads directory if it doesn't exist
if not os.path.exists(downloads_dir):
    os.mkdir(downloads_dir)

# Download the files using urllib
urllib.request.urlretrieve(eclipse_url, os.path.join(downloads_dir, eclipse_file))
urllib.request.urlretrieve(visualstudio_url, os.path.join(downloads_dir, visualstudio_file))
urllib.request.urlretrieve(intellij_url, os.path.join(downloads_dir, intellij_file))
urllib.request.urlretrieve(java_url, os.path.join(downloads_dir, java_file))
urllib.request.urlretrieve(s3browser_url, os.path.join(downloads_dir, s3browser_file))
urllib.request.urlretrieve(chrome_url, os.path.join(downloads_dir, chrome_file))
urllib.request.urlretrieve(git_url, os.path.join(downloads_dir, git_file))
urllib.request.urlretrieve(docker_url, os.path.join(downloads_dir, docker_file))
urllib.request.urlretrieve(node_js_url, os.path.join(downloads_dir, node_js_file))
urllib.request.urlretrieve(jmeter_url, os.path.join(downloads_dir, jmeter_file))



# Display a message when done
print("download complete.")
password = "test123"
