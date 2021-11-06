from house_info import HouseInfo

class HumidityData(HouseInfo):
    def _conver_data(self,data):
        recs = []
        for rec in data:
            recs.append(float(rec)*100)
    def get_data_by_area(self,rec_area=0):
        recs = super().get_data_by_area("humidity",rec_area)
        return self._convert_data(recs)
