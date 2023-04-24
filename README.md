<h1>Selenium Automated Test Tranzact using Python</h1>
<p>This Python script is a Selenium test designed to automate the process of creating an account, logging in, and adding items to the cart in the EverShop.io website.</p>

<h2>WARNING ⚠ </h2>
<li>This script will not work correctly unless the shopping cart is empty.</li>
<li>This script will only reach the process of selecting a payment method, it doesn't place the order.</li>
<li>Due to the website constantly changing, I have found that the visible products are not always the same, and therefore, this script will only work with the version of the web app the SCRIPT was developed with.</li>
<li>Make sure that the credentials used in the script are from an existing account, do this by signing into the account. (I have noticed that the web app deletes the users when is being updated.</li>

<h2>Installation</h2>
<ul>
<li>Install Python (3.11.3 or higher) on your system.</li>

<li>Use Chrome version 112</li>

<li>Use ChromeDriver 112.0.5615.49</li>

<li>Create a folder in C:/SeleniumDrivers AND add chromedriver files to it</li>

<li>Install Selenium WebDriver using pip:</li>
</ul>

    pip install selenium

<li>Download and install the latest version of the Chrome WebDriver (https://sites.google.com/a/chromium.org/chromedriver/downloads)</li>

<h2>Usage</h2>
<li>Set the path to the Chrome WebDriver in the PATH variable in line 7 of the script.</li>
<li>Run the script in your preferred IDE or command-line tool.</li>
<li>The script will automatically navigate to the EverShop.io website, create an account, log in, add items to the cart, fill out address information and select payment method.</li>

<h2>Requirements</h2>
This script requires the following packages to be installed:

<li>os: It's used to add the chrome webdriver to the PATH</li>
<li>selenium: It's used to do the automated tests.</li>
<li>time: It's used for the time.sleep() function</li>

<h2>License</h2>
This script is licensed under the MIT License - see the LICENSE file for details.
