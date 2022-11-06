class Set:
    def ans(self, list_m: list[dict]):
        dico = dict()
        for data in list_m:
            for key, value in data.items():
                if dico.get(value):
                    dico[value].append(key)
                    continue
                dico[key] = [value]
        print(dico)
 
 
Set().ans(
    [
        {"Dg set": "Diesel generator"},
        {"Organization": "Organisation"},
        {"Group": "Organization"},
        {"Orange": "Kinnu"},
        {"Orange": "narangi"},
    ]
)