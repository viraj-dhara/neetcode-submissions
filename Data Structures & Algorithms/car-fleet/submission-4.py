class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [list(item) for item in zip(position, speed)]
        cars.sort(key = lambda item : item[0], reverse=True)
        
        #print(cars)
        # number_of_fleets = 0

        i = 0
        while i <= len(cars) - 2 :

            curr_car_time = (target - cars[i][0]) / cars[i][1]
            behind_car_time = (target - cars[i+1][0]) / cars[i+1][1]

            while behind_car_time <= curr_car_time :
                cars.pop(i+1)
                if i <= len(cars) - 2 : behind_car_time = (target - cars[i+1][0]) / cars[i+1][1] 
                # elif i == len(cars) - 1 and ( (target - cars[-1][0]) / cars[-1][1] ) <= curr_car_time : car.pop
                else : break
            
            i += 1

        return len(cars)


## Rough:
# time = length/speed
# length = target - position

# behind car            i+1
# curr car              i
