from house_info import HouseInfo


class ParticleData(HouseInfo):
    def _conver_data(self,data):
        recs = []
        for rec in data:
            recs.append(float(rec))
        return recs
    
