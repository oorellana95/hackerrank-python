import time


def truckTour(petrolpumps):
    starting_index, petrol = 0, 0

    for i in range(len(petrolpumps)):
        next_pump_kms = petrolpumps[i][1]
        petrol += petrolpumps[i][0]

        if next_pump_kms <= petrol:
            petrol -= next_pump_kms

        else:
            petrol = 0
            starting_index = i + 1

    return starting_index


if __name__ == '__main__':
    start = time.time()
    petrolpumps = [[1, 5], [10, 3], [3, 4]]
    print(truckTour(petrolpumps))
    end = time.time()
    print(end - start)
