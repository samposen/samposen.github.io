document.write('<div id="cu-identity">');
	document.write('<div id="cu-logo">');
document.write('<a id="insignia-link" href="http://www.cornell.edu/"><img src="//www.cornell.edu/img/cu_logo_unstyled.gif" alt="Cornell University" width="263" height="75" border="0" /></a>');                     
/*<!--		document.write('<a id="insignia-link" href="http://www.cornell.edu/"><img src="./images/layout/unit_signature.png" alt="Cornell University" width="283" height="75" border="0" /></a>'); -->*/
		document.write('<div id="unit-signature-links">');
			document.write('<a id="cornell-link" href="http://www.cornell.edu/">Cornell University</a>');
			document.write('<a id="unit-link" href="http://www.lepp.cornell.edu/~sep93/index.html">Home</a>');
		document.write('</div>');
	document.write('</div>');
	
	/*<!-- 
		The search-form div contains a form that allows the user to search 
		either pages or people within cornell.edu directly from the banner.
	-->*/
	document.write('<div id="search-form">');
		document.write('<form action="http://www.cornell.edu/search/" method="get" enctype="application/x-www-form-urlencoded">');
			document.write('<div id="search-input">');
				document.write('<label for="search-form-query">SEARCH CORNELL:</label>');
				document.write('<input type="text" id="search-form-query" name="q" value="" size="20" />');
				document.write('<input type="submit" id="search-form-submit" name="submit" value="go" />');
			document.write('</div>');

			document.write('<div id="search-filters">');
					document.write('<input type="radio" id="search-filters1" name="tab" value="" checked="checked" />');
					document.write('<label for="search-filters1">Pages</label>');
				
					document.write('<input type="radio" id="search-filters2" name="tab" value="people" />');
					document.write('<label for="search-filters2">People</label>');
					
					document.write('<a href="http://www.cornell.edu/search/">more options</a>');
			document.write('</div>');
		document.write('</form>');
	document.write('</div>');
document.write('</div>');
