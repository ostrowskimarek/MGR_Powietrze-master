stationId = (0)
lista = (1,2,3)
for stationId in range(lista.index(stationId)):
#    print(lista.index(stationId))
    stationId + 1

    print(stationId)
# STANOWISKA POMIAROWE
url = ("https://api.gios.gov.pl/pjp-api/rest/station/sensors/" + stationId)
print(url)

