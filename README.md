To turn in homework 2, create files (and subdirectories if needed) in
this directory, add and commit those files to your cloned repository,
and push your commit to your bare repository on GitHub.

Add any general notes or instructions for the TAs to this README file.
The TAs will read this file before evaluating your work.

Using POST Request
I am using POST requests because as we are submitting data from our web page to te server to be processed, it is better to use POST request. Also, I don't want the parameters
to be show in the request url when sending the request to the server. Get is used when you usually want to retrieve something, but here we are passing parameters and want to
compute/ process something using parameters. Basically we can do the same thing using POST and GET, but POST is more secured as user cannot see what parameters are
passed and modify them in the request

Some additional points:
When user clicks 'equal', then the final result is displayed. Then if a user clicks any operator including equal, immediately after previous equal, then the display
shows message 'Error: select a number first'.
When a parameter isn't passed in the request, then the message 'MALFORMED' is shown.
If the inputs for calculation can't be converted to integer, then error message 'Invalid number' is shown.
If consecutive operators are selected, then the last selected operator is considered. In this case, if the operator '=' is selected as the very 1st operato
with only one operand, and then another operator is immediately selected then the 2nd operator overrides the = operator.
If division by zero is tried then error message invalid is displayed.

Some CSS code referred from the 1st homework.