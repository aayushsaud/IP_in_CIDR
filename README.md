<h1>IP Addresses within a CIDR</h1>
<p>This Python script allows you to input a CIDR block and prints each IP address within the specified network range.</p>

<h2>Requirements</h2>
<ul>
    <li>Python 3.x</li>
</ul>

<h2>Usage</h2>
<ol>
    <li><strong>Run the Script:</strong> Execute the script in your Python environment. You can run it from the command line or an IDE of your choice.</li>
    <li><strong>Input CIDR Block:</strong> When prompted, enter the CIDR block in the format <code>IP_ADDRESS/PREFIX_LENGTH</code>. For example, <code>192.168.1.0/24</code>.</li>
    <li><strong>Output:</strong> The script will print each IP address within the specified network range to the console.</li>
</ol>

<h2>Example</h2>
<pre>
Please enter the CIDR block (e.g., 192.168.1.0/24): 192.168.1.0/29
</pre>

<h2>Output:</h2>
<pre>
192.168.1.0
192.168.1.1
192.168.1.2
192.168.1.3
192.168.1.4
192.168.1.5
192.168.1.6
192.168.1.7
</pre>
