import csv, sys


def Tambons():

    filename = 'tambons.csv'

    with open(filename, newline='') as f:
        #reader = csv.reader(f)
        reader = csv.DictReader(f)
        try:
            all = {}
            for n, row in enumerate(reader):
                all[row['TA_ID']] = {
                    "id": row['TA_ID'],
                    "tambon": {
                        "en": row['TAMBON_E'],
                        "th": row['TAMBON_T']
                    },
                    "amphoe": {
                        "en": row['AMPHOE_E'],
                        "th": row['AMPHOE_T']
                    },
                    "jhangwat": {
                        "en": row['CHANGWAT_E'],
                        "th": row['CHANGWAT_T']
                    },
                    "geo": {
                        "lat": float(row['LAT']),
                        "lon": float(row['LONG'])
                    }
                }

        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
        return all


if __name__ == "__main__":
    #print(Tambons()['810402'])
    t = Tambons()
    print(len(t))
