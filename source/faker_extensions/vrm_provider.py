import random
import string

from faker import Faker
from faker.providers import BaseProvider
import rstr


class VrmProvider(BaseProvider):

    number_plate_age = (*range(51, 69), *range(2, 20))

    number_plate_regions = [
        "AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AJ", "AK", "AL", "AM", "AN", "AO", "AP", "AR", "AS", "AT", "AU",
        "AV", "AW", "AX", "AY", "BA", "BB", "BC", "BD", "BE", "BF", "BG", "BH", "BJ", "BK", "BL", "BM", "BN", "BO", "BP",
        "BR", "BS", "BT", "BU", "BV", "BW", "BX", "BY", "CA", "CB", "CC", "CD", "CE", "CF", "CG", "CH", "CJ", "CK", "CL",
        "CM", "CN", "CO", "CP", "CR", "CS", "CT", "CU", "CV", "CW", "CX", "CY", "DA", "DB", "DC", "DD", "DE", "DF", "DG",
        "DH", "DJ", "DK", "DL", "DM", "DN", "DO", "DP", "DR", "DS", "DT", "DU", "DV", "DW", "DX", "DY", "EA", "EB", "EC",
        "ED", "EE", "EF", "EG", "EH", "EJ", "EK", "EL", "EM", "EN", "EO", "EP", "ER", "ES", "ET", "EU", "EV", "EW", "EX",
        "EY", "FA", "FB", "FC", "FD", "FE", "FF", "FG", "FH", "FJ", "FK", "FL", "FM", "FN", "FP", "FR", "FS", "FT", "FV",
        "FW", "FX", "FY", "GA", "GB", "GC", "GD", "GE", "GF", "GG", "GH", "GJ", "GK", "GL", "GM", "GN", "GO", "GP", "GR",
        "GS", "GT", "GU", "GV", "GX", "GY", "HA", "HB", "HC", "HD", "HE", "HF", "HG", "HH", "HJ", "HK", "HL", "HM", "HN",
        "HO", "HP", "HR", "HS", "HT", "HU", "HV", "HX", "HY", "HW", "KA", "KB", "KC", "KD", "KE", "KF", "KG", "KH", "KJ",
        "KK", "KL", "KM", "KN", "KO", "KP", "KR", "KS", "KT", "KU", "KV", "KW", "KX", "KY", "LA", "LB", "LC", "LD", "LE",
        "LF", "LG", "LH", "LJ", "LK", "LL", "LM", "LN", "LO", "LP", "LR", "LS", "LT", "LU", "LV", "LW", "LX", "LY", "MA",
        "MB", "MC", "MD", "ME", "MF", "MG", "MH", "MJ", "MK", "ML", "MM", "MN", "MO", "MP", "MR", "MS", "MT", "MU", "MV",
        "MW", "MX", "MY", "NA", "NB", "NC", "ND", "NE", "NF", "NG", "NH", "NJ", "NK", "NL", "NM", "NN", "NO", "NP", "NR",
        "NS", "NT", "NU", "NV", "NW", "NX", "NY", "OA", "OB", "OC", "OD", "OE", "OF", "OG", "OH", "OJ", "OK", "OL", "OM",
        "ON", "OO", "OP", "OR", "OS", "OT", "OU", "OV", "OW", "OX", "OY", "PA", "PB", "PC", "PD", "PE", "PF", "PG", "PH",
        "PJ", "PK", "PL", "PM", "PN", "PO", "PP", "PR", "PS", "PT", "PU", "PV", "PW", "PX", "PY", "RA", "RB", "RC", "RD",
        "RE", "RF", "RG", "RH", "RJ", "RK", "RL", "RM", "RN", "RO", "RP", "RR", "RS", "RT", "RU", "RV", "RW", "RX", "RY",
        "SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SJ", "SK", "SL", "SM", "SN", "SO", "SP", "SR", "SS", "ST", "SU",
        "SV", "SW", "SX", "SY", "VA", "VB", "VC", "VD", "VE", "VF", "VG", "VH", "VJ", "VK", "VL", "VM", "VN", "VO", "VP",
        "VR", "VS", "VT", "VU", "VV", "VW", "VX", "VY", "WA", "WB", "WC", "WD", "WE", "WF", "WG", "WH", "WJ", "WK", "WL",
        "WM", "WN", "WO", "WP", "WR", "WS", "WT", "WU", "WV", "WW", "WX", "WY", "YA", "YB", "YC", "YD", "YE", "YF", "YG",
        "YH", "YJ", "YK", "YL", "YM", "YN", "YO", "YP", "YR", "YS", "YT", "YU", "YV", "YW", "YX", "YY"]

    def vrm_number(self):
        age = random.choice(self.number_plate_age)
        region = random.choice(self.number_plate_regions)
        rnd_str = ''.join(random.choices(string.ascii_uppercase, k=3))
        return "{}{} {}".format(region, age, rnd_str)


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(VrmProvider)

    vin = fake.vrm_number()
    print(vin)


if __name__ == '__main__':
    main()
