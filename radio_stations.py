states_needs = {'al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'fl', 'ga', 'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky',
                'la', 'me', 'md', 'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd',
                'oh', 'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy'}

stations = {}
stations['kone'] = {"id", "nv", "ut"}
stations['ktwo'] = {"wa", "id", "mt"}
stations['kthree'] = {"or", "nv", "ca"}
stations['kfour'] = {"nv", "ut"}
stations['kfive'] = {"ka", "az"}
stations['ksix'] = {'al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'fl'}
stations['kseven'] = {'ct', 'de', 'fl', 'ga', 'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me'}
stations['keight'] = {'la', 'me', 'md', 'ma', 'mi', 'mn', 'ms'}
stations['knine'] = {'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd'}
stations['kten'] = {'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx'}
stations['keleven'] = {'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv'}
stations['ktvelv'] = {'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy'}

final_stations = set()

while states_needs:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needs & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    final_stations.add(best_station)
    states_needs -= states_covered

print(final_stations)
