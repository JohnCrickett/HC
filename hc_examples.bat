@echo off
@echo Calculating journey times
@echo -------------------------
@echo Route: "New York" "Liverpool"
@python router.py --network ./data/network.txt --journeytime "Buenos Aires" "New York" "Liverpool"

@echo Route: "Buenos Aires" "Casablanca" "Liverpool"
python router.py --network ./data/network.txt --journeytime "Buenos Aires" "Casablanca" "Liverpool"

@echo Route: "Buenos Aires" "Cape Town" "New York" "Liverpool" "Casablanca"
python router.py --network ./data/network.txt --journeytime "Buenos Aires" "Cape Town" "New York" "Liverpool" "Casablanca"

@echo Route: "Buenos Aires" "Cape Town" "Casablanca" &
python router.py --network ./data/network.txt --journeytime "Buenos Aires" "Cape Town" "Casablanca"

@echo . & echo Finding the shortest journey time
@echo ---------------------------------
@echo Route from "Buenos Aires" to "Liverpool"
python router.py --network ./data/network.txt --shortesttime "Buenos Aires" "Liverpool"

@echo Route from "New York" to "New York"
python router.py --network ./data/network.txt --shortesttime "New York" "New York"

@echo . & echo Finding the number of routes within a stop limit
@echo ------------------------------------------------
@echo Routes from Liverpool to Liverpool with a maximum number of 3 stops
python router.py --network ./data/network.txt --hoplimit Liverpool Liverpool

@echo Routes from Buenos Aires to Liverpool where exactly 4 stops are made
python router.py --network ./data/network.txt --hoplimit "Buenos Aires" Liverpool

@echo . & echo Finding the number of routes within a time limit
@echo ------------------------------------------------
@echo Routes from Liverpool to Liverpool where the journey time is less than or equal to 25 days
python router.py --network ./data/network.txt --timelimit Liverpool Liverpool 25