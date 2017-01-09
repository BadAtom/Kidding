from requests import get


class _NHTSA:
    url = "http://webapi.nhtsa.gov/api/SafetyRatings"
    get_format = "?format=json"
    last_response = 0
    last_result = 0
    last_result_type = 0
    status_code = 0

    def __init__(self):
        self.response = lambda uri: get(self.url + uri + self.get_format)

    def __years(self):
        return ""

    def __year(self, model_year):
        return "/" + str(model_year)

    def __make(self, model_year, maker):
        return self.__year(model_year) + "/" + str(maker)

    def __model(self, model_year, maker, model):
        return self.__make(model_year, maker) + "/" + str(model)

    def __by_id(self, car_id):
        return "/vehicleid/" + str(car_id)

    def _status(self):
        return self.status_code < 300

    def _bad_status(self):
        print("Server respond error:" + self.status_code)

    def printer(self, my_list, sep="\t"):
        counter = 1
        my_list.sort()
        for item in my_list:
            print(item, end=sep if counter != 5 else "\n")
            counter = (counter + 1) if counter != 5 else 1
        print(end="\n" if counter != 1 else "")

    def result_out(self):
        if self.last_result_type == 1:
            print("List of years from server:")
            years = []
            for year in self.last_result['Results']:
                years.append(year['ModelYear'])

            self.printer(years)
        elif self.last_result_type == 2:
            print("Make from this year:")
            makes = []
            for make in self.last_result['Results']:
                makes.append(make['Make'])

            self.printer(makes, ", ")
        elif self.last_result_type == 3:
            pass
        elif self.last_result_type == 4:
            pass
        elif self.last_result_type == 5:
            pass
        else:
            print("No such result", self.last_result_type)

    def years(self):
        response = self.response(self.__years())
        self.status_code = response.status_code
        if self._status():
            self.last_response = response
            self.last_result = response.json()
            self.last_result_type = 1

            self.result_out()
        else:
            self._bad_status()

    def year(self):
        year = input("Please choose a year: ")
        response = self.response(self.__year(year))
        self.status_code = response.status_code
        if self._status():
            self.last_response = response
            self.last_result = response.json()
            self.last_result_type = 2

            self.result_out()
        else:
            self._bad_status()

if __name__ == "__main__":
    work_api = _NHTSA()
    # work_api.year()
    print(work_api.response(work_api._NHTSA__year(2007)).json())
    print(work_api.response(work_api._NHTSA__make(2011, "TOYOTA")).json())
    print(work_api.response(work_api._NHTSA__model(2011, "TOYOTA", "COROLLA")).json())
