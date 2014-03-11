<html>
<head>
</head>
<body>
<h2>Installation</h2>
<div>
  <code>git clone https://github.com/wesmadrigal/bitdata.git</code><br>
  <code>python setup.py install</code><br>
</div>
<h2>Usage</h2>
<div>
  <p>The BitlyData class exposes all of the Data API endpoints available to bit.ly developers.  They are named the same way, as well.  For example, the "hot_phrases" endpoint that bit.ly exposes is similarly named hot_phrases as an instance method of the DatBit object.</p>
  <p>One thing you will have to do is sign up with bit.ly as a developer and get an access token, as the DatBit class's __init__ method takes one as a required parameter on instantiation.</p>
  <p>Go get your access token <a href="https://bitly.com/a/oauth_apps">here</a></p>
  <code>from bitdata.bitdata import BitData</code>
  <br>
  <code>bitly = BitData("tokenyouretrieved")</code>
  <br>
  <code>hot_phrases = bitly.hot_phrases()</code>  
</div>
