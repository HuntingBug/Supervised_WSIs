from xml.etree.ElementTree import parse
import numpy as np

def read_xml(slide_num, mask_level):
    ''' read xml files which has tumor coordinates list
        return coordinates of tumor areas

    Args:
        slide_num (int): number of slide used
        maks_level (int): level of mask
    '''

    path = './pre_dataset/annotation/A01.xml'
    xml = parse(path).getroot()
    coors_list = []
    coors = []
    for regions in xml.iter('Regions'):
        for region in regions:
            coors.append([round(float(region.get('X'))/(2**mask_level)),
                            round(float(region.get('Y'))/(2**mask_level))])
        coors_list.append(coors)
        coors=[]
    return np.array(coors_list)

coordinate = read_xml(1,1)
print(coordinate)