<html>
<head>
</head>
<body>
<h2>Installation</h2>
<div>
  <code>git clone https://github.com/SpartzOSS/bitdata.git</code><br>
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

<h2>License</h2>
<p>(The MIT License)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
</p>
