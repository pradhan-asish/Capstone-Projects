from house_info import HouseInfo


class TemperatureData(HouseInfo):
    def _convert_data(self,data):
        recs = []
        for rec in data:
            recs.append(int(rec,base=10))
        return recs
    def get_data_by_area(self,rec_area):
        pass
