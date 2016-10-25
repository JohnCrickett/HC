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