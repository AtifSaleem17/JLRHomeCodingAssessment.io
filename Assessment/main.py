# importing the ergast API module after installation
import ergast_py

def best_performances():
    # initialise the object/instance of the Ergast class in order to access the API data
    ergast = ergast_py.Ergast()
    # dictionary contain the circuits where each 2023 constructor best performed at
    performances = dict()
    # list of 2023 constructors
    constructors_list = list()
    # building the query with function calls to fetch 2023 constructors
    constructors_2023 = ergast.season(2023).get_constructors()
    # inserting 2023 constructors' ids and names
    for x in range(len(constructors_2023)):
        constructors_list.append(constructors_2023[x].constructor_id)
    # fetching data of each constructor of 2023 for all the seasons (2023 - 1950)
    for constructor in constructors_list:  # loop for 2023 constructors
        for season in range(2023, 2019, -1):  # loop for seasons
            try:
                # building the query with function calls to fetch 2023 constructors' results
                results = ergast.season(season).constructor(constructor).get_results()
                # only if constructor raced in the season
                if len(results) != 0:
                    # selecting only highest performance results after sorting in descending order
                    results.sort(key=lambda results : results.results[0].points, reverse=True)
                    # inserting the constructors and their corresponding values
                    if constructor not in performances:
                        performances[constructor] = [results[0].results[0].constructor.name,
                                                     results[0].circuit.circuit_name,
                                                     results[0].results[0].points,
                                                     season]
                    # updating performance
                    else:
                        if performances[constructor][2] < results[0].results[0].points:
                            # updating circuit name
                            performances[constructor][1] = results[0].circuit.circuit_name
                            # updating points
                            performances[constructor][2] = results[0].results[0].points
                            # updating season
                            performances[constructor][3] = season

            except Exception as e:
                print("ERROR: ", e.args[0], "-->", constructor.title(), "'s data not found  season ", season)

    return performances


if __name__ == "__main__":

    performances = best_performances()
    for performance in performances:
        print(performances[performance][0], "has best performed at",
              performances[performance][1], "with",
              performances[performance][2], "points in",
              performances[performance][3])
