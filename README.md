<h1>Email Validator</h1>

<p>This script is a Python program that validates email addresses. It uses the "validate_email" library to check the validity of an email address, and the "tqdm" library to display a progress bar while processing a list of email addresses.</p>

<h2>Getting Started</h2>

<p>These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.</p>

<h3>Prerequisites</h3>

<p>You will need to install the following libraries:</p>
<ul>
  <li>validate_email</li>
  <li>tqdm</li>
  <li>colorama</li>
</ul>

<p>You can install them using pip by running:</p>

<pre>pip install requirements.txt</pre>

<h3>Running the script</h3>

<p>To run the script, you will need to provide an input file containing a list of email addresses, one per line, and an output file. The script will then check the validity of the email addresses in the input file and write valid addresses to the output file.</p>

<p>You can run the script by executing the following command in your terminal:</p>

<pre>python email_checker.py</pre>

<p>The script will prompt you to enter the input file name or a string containing email addresses separated by commas , output file name and delay time.</p>

<h3>Example</h3>

<ul>
  <li>Input file name :  <code>emails.txt</code></li>
  <li>Output file name : <code>valid_emails.txt</code></li>
  <li> delay time : <code>5</code> </li>
</ul>

<pre>
python main.py
Enter input file Name or email addresses separated by commas: emails.txt
Enter output file Name: valid_emails.txt
Enter delay in seconds: 5
</pre>

<h2>Important Note</h2>

<p>Please note that this script uses the SMTP protocol to connect to the email server of the domain associated with the email address, which requires port 25 to be open. However, in some cases, port 25 might be blocked by a firewall or an ISP (Internet Service Provider) to prevent spam and unwanted email. If the script can't connect to the email server on port 25, it will not be able to check the validity of the email address and will return an error. So if you are running the script on a local machine, make sure that the port 25 is open and not blocked by any firewall or security software, otherwise, you may not be able to validate the emails.</p>


<h2>License</h2>

<p>This project is licensed under the <a href="https://opensource.org/licenses/BSD-3-Clause">BSD 3-Clause License</a> - see the <a href="LICENSE">LICENSE</a> file for details</p>

