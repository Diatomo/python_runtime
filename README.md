

This was an example program for an application. It is searches for a particular string recursively through nested directories.

Author :: Charles Stevenson  
Date :: 02.18.2019


To Run :: 

	'python main.py <options> <path>'

	path (e.g. '~/Documents')

	Optional Filters ::

	-f <pattern>
	pattern (e.g. '.mp3')

	-s <size>
	size (e.g. '5000')

	successful execution may look like:

	'python main.py -f mp3 -s 5000 ./testDir'
 
 Write unit tests for the above. Demonstrate your code coverage and justify it (i.e. why is this good enough)

 	The test are good enough to fit the features sought by the coding problem. The tests cover:

	It covers constructing the pathFinder Object
	It covers filenames which can be any string.
	It covers sizes from small negative value to large positive ones.

	They do not cover:

	User execution error: 
		however there are some try catch blocks in the input handler that attempts
		to explain to the user what they may've done incorrectly.

	Symbolically linked files:
		This was an exception found when I started pointing the pathfinder at different directories. It is written
		into the search algorithm to ignore symbolically linked files when there sizes cannot be obtained. I.e.
		they don't exist in recursed directory.

	User production environment:
		Because I don't have access to a client or user environment. I cannot fully test the results of pointing
		this at directories on a user environment to mine exception to the algorithm. Also because I don't fully
		understand the expectation of wild directories I cannot fully understand the results of a search. I.e.
		how large they are going to be or what file names exist.

	Memory:
		With the above. I did not test the memory constraints of the output array. They do not test what happens
		when the memory is exceeded in the output array.

	Therefore, I think they are good enough to illustrate the expected outputs and how the algorithm functions. However;
	they would not be comprehensive to distribute to users with different environments.


Demonstrate execution time.  How might this be improved?

	Execution time is output at the end of the script. From run-time to when it finishes a search.
	I realize that the execution time is calculating by the total time the program is open to when it
	closees. Therefore, if a computer is under a lot of stress the runtime with lengthen. However; for
	application purposes it gives a good estimate on its execution.

	The execution could be improved in many different ways.

	1) Instead of recursively searching through the entire directory structure recursively. It maybe 
	wise to map out which directories to search. This could be done with a heuristic, maybe files 
	with particular names would be searched first and if no files are found to search the remaining directories. 
	If a subdirectory contains X amount of files search that directory first before searching in a directory 
	with Y amount of files etc... Or perhaps if one is looking for a file size, only check directories greater than
	the parameterized file size.

	2) In a similar vein, instead of pointing to a root structure, perhaps a term that maps to a set of paths
	could help a search in filtering out unecessary steps. 
=======
# python_runtime
