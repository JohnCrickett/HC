# HC
Loads a network from a CSV file and performs various operations on it.

Developed and tested using Python 3.5.2 

##Testing:
to run all unit tests use:  
`python -m unittest discover test`

To run individual unit tests use:  
`python ./test/test_<name>.py`


##Usage:
For help  
`python router.py --help`

To calculate the travel time of a journey:  
`python router.py --network ./data/network.txt --journeytime "New York" "Liverpool"`

To calculate the shortest route between two locations:  
`python router.py --network ./data/network.txt --shortesttime "New York" "Casablanca"`


## Examples:
To run the examples (on Windows) a batch file is provided:  
`hc_examples.bat`

To run the examples (on Linux) a batch file is provided:  
`hc_examples.sh`
